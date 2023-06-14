"""Defines utility methods for API package."""

import horizonai
import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from urllib.parse import urljoin


MAX_RETRY_ATTEMPTS = 10
MIN_RETRY_WAIT_TIME = 4
MAX_RETRY_WAIT_TIME = 10


@retry(
    reraise=True,
    stop=stop_after_attempt(MAX_RETRY_ATTEMPTS),
    wait=wait_exponential(
        multiplier=1, min=MIN_RETRY_WAIT_TIME, max=MAX_RETRY_WAIT_TIME
    ),
    retry=retry_if_exception_type(requests.exceptions.ConnectionError),
)
def _get(endpoint, json=None, data=None, headers=None):
    response = requests.get(
        urljoin(horizonai.base_url, endpoint),
        json=json,
        data=data,
        headers=headers,
    )
    return _handle_response(response)


@retry(
    reraise=True,
    stop=stop_after_attempt(MAX_RETRY_ATTEMPTS),
    wait=wait_exponential(
        multiplier=1, min=MIN_RETRY_WAIT_TIME, max=MAX_RETRY_WAIT_TIME
    ),
    retry=retry_if_exception_type(requests.exceptions.ConnectionError),
)
def _post(endpoint, json=None, data=None, headers=None, files=None):
    response = requests.post(
        urljoin(horizonai.base_url, endpoint),
        json=json,
        data=data,
        headers=headers,
        files=files,
    )
    return _handle_response(response)


@retry(
    reraise=True,
    stop=stop_after_attempt(MAX_RETRY_ATTEMPTS),
    wait=wait_exponential(
        multiplier=1, min=MIN_RETRY_WAIT_TIME, max=MAX_RETRY_WAIT_TIME
    ),
    retry=retry_if_exception_type(requests.exceptions.ConnectionError),
)
def _delete(endpoint, headers=None):
    response = requests.delete(
        urljoin(horizonai.base_url, endpoint),
        headers=headers,
    )
    return _handle_response(response)


@retry(
    reraise=True,
    stop=stop_after_attempt(MAX_RETRY_ATTEMPTS),
    wait=wait_exponential(
        multiplier=1, min=MIN_RETRY_WAIT_TIME, max=MAX_RETRY_WAIT_TIME
    ),
    retry=retry_if_exception_type(requests.exceptions.ConnectionError),
)
def _put(endpoint, json=None, headers=None):
    response = requests.put(
        urljoin(horizonai.base_url, endpoint),
        json=json,
        headers=headers,
    )
    return _handle_response(response)


def _get_auth_headers():
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    return {"Authorization": f"Bearer {horizonai.api_key}"}


def _handle_response(response):
    if response.status_code not in [200, 201]:
        raise Exception(
            f"Request failed with status code {response.status_code}: {response.text}"
        )
    if not response.text:
        return {"message": "Empty response"}
    return response.json()
