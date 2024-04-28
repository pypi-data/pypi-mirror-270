from lotgi._openai import OpenAI

__all__ = [
    "OpenAI",
]


from lotgi.rest_client import RestClient
from lotgi.tokens import estimate_token_usage
from lotgi.logging import init_logging
from lotgi.models import rest

import click
from tabulate import tabulate
from datetime import timedelta
from typing import Optional
import sys
import requests

@click.group
def cli():
    """
    Lotgi CLI tool.
    """
    init_logging()


def format_duration(duration_s : int) -> str:
    total_hours = duration_s // (60 * 60)
    minutes = (duration_s // 60) % 60
    seconds = duration_s % 60
    if total_hours > 0:
        return f"{total_hours}h{minutes}m{seconds}s"
    return f"{minutes}m{seconds}s"

def format_execution_options(options) -> str:
    columns = {
        "Tradeoff": [
            option.option_name for option in options
        ],
        "Estimated Price": [
            f"${option.expected_cost:.2f}" for option in options
        ],
        "Estimated Duration (s)": [
            format_duration(option.expected_duration) for option in options
        ],
    }
    return tabulate(columns, headers="keys")

def get_tradeoff() -> str:
    while True:
        selection = input(f"Select a tradeoff ({repr(rest.EXECUTION_TRADEOFFS)}): ")
        if selection in rest.EXECUTION_TRADEOFFS:
            return selection
        else:
            print(f"Invalid tradeoff. Select from {rest.EXECUTION_TRADEOFFS}")

@cli.command
@click.option("--model", required=True, help="The model to run inference with.")
@click.option("--input-url", required=True, help="The model to run inference with.")
@click.option("--field", required=True, help="The field within a row containing the data.")
@click.option("--tradeoff", required=True, default=None, help=f"The tradeoff ({rest.EXECUTION_TRADEOFFS}).")
def submit(model : str, input_url : str, field : str, tradeoff : Optional[str]):
    """
    Submit a new batch inference job.

    Your job file is expected to be formatted as a jsonl file. Each line corresponds to a request and should be a json object. Use the `--field` argument to specify which field of the json object contains the text to complete.

    For example, if a file stored at `example.com/dataset.jsonl` contains the contents

    ```\n
    {"my_completion_text": "hello"}\n
    {"my_completion_text": "lorem"}\n
    ```

    You can run `lotgi submit --model mistralai/Mistral-7B-Instruct-v0.2 --input-url example.com/dataset.jsonl --field "my_completion_text" --tradeoff Cheapest`. This will run the mistral-7b model against the inputs "hello" and "lorem", optimizing for cost.
    """
    client = RestClient()

    if tradeoff is None:
        print(f"Scanning job to estimate costs...")
        job_execution_options_input = estimate_token_usage(input_url=input_url, prompt="", model=model, field=field)
        options = client.job_exection_options(job_execution_options_input=job_execution_options_input)

        print(format_execution_options(options))
        tradeoff = get_tradeoff()


    result = client.submit_job(model=model, input_url=input_url, field=field, target_cost=-1, target_deadline=-1, execution_tradeoff=tradeoff)
    print("Success!")
    print(result)


@cli.command
def list():
    """
    List your batch inferences jobs.
    """
    client = RestClient()
    jobs = client.list_jobs()

    print(tabulate([job.model_dump() for job in jobs], headers="keys"))


@cli.command
@click.argument("job_id", required=True)
def get(job_id : str):
    """
    Get the results of a specific job.

    Job results are written to stdout. (Human readable text/errors are written to stderr).

    To store your job results, consider redirecting the job output to a file. `lotg get <job_id> > saved_job_results.jsonl`
    """
    client = RestClient()
    url = None
    try:
        url = client.get_job_results(job_id)
    except KeyError:
        print("Job not found!", file=sys.stderr, flush=True)
        sys.exit(1)
    assert url is not None

    result = requests.get(url)
    if not result.ok:
        print(f"Couldn't download result from {url}. {result.status_code} : {result.text}")
        sys.exit(1)

    print(result.text)

