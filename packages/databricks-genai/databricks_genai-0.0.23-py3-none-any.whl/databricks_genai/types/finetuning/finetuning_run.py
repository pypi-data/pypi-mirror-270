"""
A Databricks finetuning run
"""

from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Tuple

from mcli.api.exceptions import MAPIException
from mcli.api.schema.generic_model import DeserializableModel, convert_datetime
from mcli.utils.utils_string_functions import camel_case_to_snake_case

# pylint: disable=cyclic-import
from databricks_genai.types.common import ObjectList
from databricks_genai.types.finetuning.finetune_config import FinetuneConfig
from databricks_genai.types.finetuning.utils import PROGRESS, seconds_to_str
from databricks_genai.types.run_status import RunStatus


@dataclass()
class FinetuningEvent(DeserializableModel):
    """ Finetuning Run Event """
    type: str
    time: datetime
    message: str

    @classmethod
    def from_mapi_response(cls, response: Dict[str, Any]) -> 'FinetuningEvent':
        """Load the formatted run event from MAPI response.
        """
        args = {camel_case_to_snake_case(key): value for key, value in response.items()}
        return cls(
            type=args['event_type'],
            time=args['event_time'],
            message=args['event_message'],
        )

    def is_terminal_state(self):
        return self.type in ["COMPLETED", "FAILED", "STOPPED", "CANCELED"]


@dataclass()
class FinetuningRun(DeserializableModel):
    """A Databricks finetuning run

    Args:
        name: The name of the finetuning run
        created_by: The user email of who created the run
        model: The model to finetune
        train_data_path: The path to the training data
        register_to: The location to the registered model
        experiment_path: The path to save the MLflow experiment
        task_type: The type of finetuning task to run
        eval_data_path: The path to the eval data
        eval_prompts: The list of prompts to use for eval
        custom_weights_path: The path to a custom model checkpoint to use for finetuning
        training_duration: The total duration of the finetuning run
        learning_rate: The peak learning rate to use for finetuning
        context_length: The maximum sequence length to use
        data_prep_cluster_id: The id of the cluster used for data prep
        created_at: The time the run was created
        started_at: The time the run was started
        estimated_end_time: The estimated time the run will complete
        completed_at: The time the run was completed
        details: The current run event
    """

    name: str
    status: RunStatus
    created_by: str

    # User inputs
    model: Optional[str] = None
    save_folder: Optional[str] = None
    train_data_path: Optional[str] = None
    register_to: Optional[str] = None
    experiment_path: Optional[str] = None
    task_type: Optional[str] = 'INSTRUCTION_FINETUNE'
    eval_data_path: Optional[str] = None
    eval_prompts: Optional[List[str]] = None
    custom_weights_path: Optional[str] = None
    training_duration: Optional[str] = None
    learning_rate: Optional[float] = None
    context_length: Optional[int] = None
    # we do not include validate_inputs as this is not sent to MAPI nor stored anywhere
    data_prep_cluster_id: Optional[str] = None

    # holds the current run event
    details: Optional[str] = None

    # Lifecycle
    created_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    estimated_end_time: Optional[datetime] = None
    formatted_eta: Optional[str] = None
    completed_at: Optional[datetime] = None

    # Details
    submitted_config: Optional[FinetuneConfig] = None
    events: Optional[List[FinetuningEvent]] = None

    # MLflow
    experiment_id: Optional[str] = None
    run_id: Optional[str] = None

    _required_properties: Tuple[str] = tuple([
        'id',
        'name',
        'status',
        'createdByEmail',
        'createdAt',
        'updatedAt',
    ])

    @property
    def run_progress(self) -> str:
        if self.status == RunStatus.RUNNING and self.started_at is not None and self.estimated_end_time is not None:
            total_time = (self.estimated_end_time - self.started_at).total_seconds()
            elapsed_time = (datetime.now(timezone.utc) - self.started_at).total_seconds()
            percentage = min(int((elapsed_time / total_time) * 100), 100)
            return f"{RunStatus.RUNNING} {PROGRESS[int(percentage / 10)]}({percentage}%)"
        return f"{self.status}"

    # hyperparameters: Hyperparameters ## todo

    @classmethod
    def from_mapi_response(cls, response: Dict[str, Any]) -> 'FinetuningRun':
        """Load the finetuning run from MAPI response.
        """
        missing = set(cls._required_properties) - set(response)
        if missing:
            raise MAPIException(
                status=HTTPStatus.BAD_REQUEST,
                message='Missing required key(s) in response to deserialize FinetuningRun '
                f'object: {", ".join(missing)} ',
            )
        started_at = convert_datetime(response['startedAt']) if response.get('startedAt', None) else None
        completed_at = convert_datetime(response['completedAt']) if response.get('completedAt', None) else None
        estimated_end_time = convert_datetime(response['estimatedEndTime']) if response.get('estimatedEndTime',
                                                                                            None) else None

        args = {
            'name': response['name'],
            'created_at': convert_datetime(response['createdAt']),
            'started_at': started_at,
            'completed_at': completed_at,
            'status': RunStatus.from_string(response['status']),
            'details': response.get('reason', ''),
            'created_by': response['createdByEmail'],
            'estimated_end_time': estimated_end_time
        }

        if estimated_end_time is not None:
            args['estimated_end_time'] = estimated_end_time

        details = response.get('details', {})
        if len(details) > 0:
            args['model'] = details.get('model')
            args['save_folder'] = details.get('saveFolder')
            args['train_data_path'] = details.get('trainDataPath')
            args['eval_data_path'] = details.get('evalDataPath')
            args['eval_prompts'] = details.get('evalPrompts')
            args['custom_weights_path'] = details.get('customWeightsPath')
            args['training_duration'] = details.get('trainingDuration')
            args['learning_rate'] = details.get('learningRate')
            args['context_length'] = details.get('contextLength')
            experiment_tracker = details.get('experimentTracker')
            if experiment_tracker is None or experiment_tracker.get('mlflow') is None:
                raise MAPIException(
                    status=HTTPStatus.NOT_FOUND,
                    message=
                    'Missing MLflow experimentTracker, which is a required field to deserialize FinetuningRun object',
                )
            mlflow_config = experiment_tracker.get('mlflow')
            args['register_to'] = mlflow_config.get('modelRegistryPath')
            args['experiment_path'] = mlflow_config.get('experimentPath')
            args['experiment_id'] = mlflow_config.get('mlflowExperimentId')
            args['run_id'] = mlflow_config.get('mlflowRunId')

            config_copy = deepcopy(details)
            # Remove events from details to keep only config properties
            if 'formattedFinetuningEvents' in config_copy:
                del config_copy['formattedFinetuningEvents']

            if 'dataPrepConfig' in config_copy:
                if 'clusterId' in config_copy['dataPrepConfig']:
                    args['data_prep_cluster_id'] = config_copy['dataPrepConfig']['clusterId']
                del config_copy['dataPrepConfig']
            args['submitted_config'] = FinetuneConfig.from_mapi_response(config_copy)

            formatted_finetuning_events = [
                FinetuningEvent.from_mapi_response(event) for event in details.get('formattedFinetuningEvents', [])
            ]
            args['events'] = sorted(formatted_finetuning_events, key=lambda x: x.time)

            # Don't show ETA during checkpoint upload
            if args['estimated_end_time'] is not None:
                found = next((event for event in args['events'] if event.type == 'TRAIN_FINISHED'), None)
                if found is not None:
                    args['estimated_end_time'] = None

        if args['estimated_end_time'] is not None:
            time_left = (args['estimated_end_time'] - datetime.now(timezone.utc)).total_seconds()
            if time_left <= 0:
                args['estimated_end_time'] = None
            else:
                args['formatted_eta'] = seconds_to_str(time_left)

        return cls(**args)

    def refresh(self) -> 'FinetuningRun':
        """Refetches the finetuning run from the API

        Returns:
            FinetuningRun: The updated finetuning run
        """

        # pylint: disable=import-outside-toplevel, cyclic-import
        from databricks_genai.api.finetuning.get import get
        return get(self)

    def cancel(self) -> int:
        """Cancel the finetuning run

        Returns:
            int: Will return 1 if the run was cancelled, 0 if it was already cancelled
        """

        # pylint: disable=import-outside-toplevel, cyclic-import
        from databricks_genai.api.finetuning.cancel import cancel
        return cancel(self)

    def delete(self) -> int:
        """Delete the finetuning run

        Returns:
            int: Will return 1 if the run was deleted, 0 if it was already deleted
        """

        # pylint: disable=import-outside-toplevel, cyclic-import
        from databricks_genai.api.finetuning.delete import delete
        return delete(self)

    def get_events(self) -> ObjectList[FinetuningEvent]:
        """Get events for the finetuning run

        Returns:
            List[FinetuningEvent]: A list of finetuning events. Each event has an event
                type, time, and message.
        """

        # pylint: disable=import-outside-toplevel, cyclic-import
        from databricks_genai.api.finetuning.get_events import get_events
        return get_events(self)
