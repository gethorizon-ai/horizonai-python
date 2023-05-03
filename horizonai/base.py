"""Defines utility methods for API package."""

import requests
from urllib.parse import urljoin

# Base url for API calls
base_url = "https://35.164.129.93:5000"

# API keys for user to set
api_key = None
openai_api_key = None
anthropic_api_key = None


def _get(endpoint, headers=None):
    global base_url
    response = requests.get(urljoin(base_url, endpoint), headers=headers)
    return _handle_response(response)


def _post(endpoint, json=None, headers=None, files=None):
    global base_url
    response = requests.post(
        urljoin(base_url, endpoint),
        json=json,
        headers=headers,
        files=files,
    )
    return _handle_response(response)


def _delete(endpoint, headers=None):
    global base_url
    response = requests.delete(urljoin(base_url, endpoint), headers=headers)
    return _handle_response(response)


def _put(endpoint, json=None, headers=None):
    global base_url
    response = requests.put(urljoin(base_url, endpoint),
                            json=json, headers=headers)
    return _handle_response(response)


def _get_auth_headers():
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    return {"Authorization": f"Bearer {api_key}"}


def _handle_response(response):
    if response.status_code not in [200, 201]:
        raise Exception(
            f"Request failed with status code {response.status_code}: {response.text}"
        )
    if not response.text:
        return {"message": "Empty response"}
    return response.json()
