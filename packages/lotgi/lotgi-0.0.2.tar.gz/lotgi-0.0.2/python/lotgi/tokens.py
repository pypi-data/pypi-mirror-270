from transformers import AutoTokenizer
import pandas as pd
from dataclasses import dataclass

from lotgi.models.rest import JobExecutionOptionsInput

@dataclass
class TokenUsageEstimate:
    input_tokens : str # We should be pretty confident this number is correct.
    output_tokens : str # This is an estimate


def estimate_token_usage(input_url : str, prompt : str, model : str, field : str) -> JobExecutionOptionsInput:
    tokenizer = AutoTokenizer.from_pretrained(model)

    inputs = pd.read_json(input_url, lines=True)

    num_prompt_tokens = len(tokenizer.encode(prompt))
    num_completions = len(inputs)

    def token_count(row) -> int:
        return len(tokenizer.encode(row))

    num_dataset_tokens = inputs[field].map(token_count).sum()

    return JobExecutionOptionsInput(
        model=model,
        input_token_count=(num_prompt_tokens * num_completions) + num_dataset_tokens,
        # TODO: This is an incredibly not-robust estimate.
        output_token_count=250 * num_completions,
    )
