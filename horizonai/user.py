"""Defines methods for User objects."""

from .base import _post


def generate_new_api_key(email, password):
    data = {"email": email, "password": password}
    headers = {"Content-Type": "application/json"}
    response = _post(
        endpoint="/api/users/generate_new_api_key",
        json=data,
        headers=headers,
    )
    return response
