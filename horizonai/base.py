"""Defines utility methods for API package."""

import horizonai
import requests
from urllib.parse import urljoin


def _get(endpoint, headers=None):
    response = requests.get(urljoin(horizonai.base_url, endpoint), headers=headers)
    return _handle_response(response)


def _post(endpoint, json=None, headers=None, files=None):
    response = requests.post(
        urljoin(horizonai.base_url, endpoint),
        json=json,
        headers=headers,
        files=files,
    )
    return _handle_response(response)


def _delete(endpoint, headers=None):
    response = requests.delete(urljoin(horizonai.base_url, endpoint), headers=headers)
    return _handle_response(response)


def _put(endpoint, json=None, headers=None):
    response = requests.put(
        urljoin(horizonai.base_url, endpoint), json=json, headers=headers
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
