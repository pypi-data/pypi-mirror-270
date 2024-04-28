from pydantic import BaseModel, Field, model_validator
from typing import Optional
import uuid

class ModalCredentials(BaseModel):
    token_id : str
    token_secret : str

class RunpodCredentials(BaseModel):
    api_key : str

class CloudCredentials(BaseModel):
    modal_credentials : Optional[ModalCredentials] = None
    runpod_credentials : Optional[RunpodCredentials] = None

    @model_validator(mode="after")
    def atleast_one_credential(self):
        if not (self.modal_credentials or self.runpod_credentials):
            raise ValueError("At least one set of credentials should be specified.")
        return self

EXECUTION_TRADEOFFS = {
    "Cheapest",
    "Hour",
}
class JobSpec(BaseModel):
    job_id : str = Field(default_factory=lambda : f"job-{uuid.uuid4()}")
    cloud_credentials : Optional[CloudCredentials] = None
    input_url : str
    target_cost : float
    target_deadline : int # Specified as a unix timestamp
    model : str
    field : str
    execution_tradeoff : str
    huggingface_token : Optional[str] = None

    # @model_validator(mode="after")
    # def valid_execution_tradeoff(self):
    #     if self.execution_tradeoff not in EXECUTION_TRADEOFFS:
    #         raise ValueError(f"execution_tradeoff must be one off {EXECUTION_TRADEOFFS}")
    #     return self

class JobStatus(BaseModel):
    job_id : str = Field(default_factory=lambda : f"job-{uuid.uuid4()}")
    input_url : str
    target_cost : float
    target_deadline : int # Specified as a unix timestamp
    state : str

class JobExecutionOptionsInput(BaseModel):
    input_token_count : int
    output_token_count : int
    model : str

class JobExecutionTradeoffOption(BaseModel):
    option_name : str
    expected_cost : float
    expected_duration : int # In seconds
