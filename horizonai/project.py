"""Defines methods for Project objects."""

import horizonai
from . import base


def list_projects():
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._get(endpoint="/api/projects", headers=headers)
    return response


def create_project(name):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    data = {"name": name}
    response = base._post(
        endpoint="/api/projects/create",
        json=data,
        headers=headers,
    )
    return response


def get_project(project_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._get(endpoint=f"/api/projects/{project_id}", headers=headers)
    return response


def delete_project(project_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._delete(endpoint=f"/api/projects/{project_id}", headers=headers)
    return response
