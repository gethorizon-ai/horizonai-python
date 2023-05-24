"""Defines enabler methods."""

import horizonai
from . import base


def generate_synthetic_data(objective, num_synthetic_data, file_path):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    if horizonai.openai_api_key == None:
        raise Exception("Must set OpenAI API key.")

    headers = {"X-Api-Key": horizonai.api_key}
    payload = {
        "objective": objective,
        "num_synthetic_data": num_synthetic_data,
        "openai_api_key": horizonai.openai_api_key,
    }
    with open(file_path, "rb") as f:
        response = base._post(
            endpoint="/api/enablers/generate_synthetic_data",
            files={"original_dataset": f},
            data=payload,
            headers=headers,
        )
        return response
