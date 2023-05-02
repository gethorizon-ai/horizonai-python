"""Defines methods for User objects."""

from . import base


def generate_new_api_key(email, password):
    data = {"email": email, "password": password}
    headers = {"Content-Type": "application/json"}
    response = base._post(
        endpoint="/api/users/generate_new_api_key",
        json=data,
        headers=headers,
    )
    return response
