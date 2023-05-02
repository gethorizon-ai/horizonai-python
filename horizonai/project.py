"""Defines methods for Project objects."""

from . import base


def list_projects():
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = base._get(endpoint="/api/projects", headers=headers)
    return response


def create_project(name):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": api_key}
    data = {"name": name}
    response = base._post(
        endpoint="/api/projects/create",
        json=data,
        headers=headers,
    )
    return response


def get_project(project_id):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = base._get(endpoint=f"/api/projects/{project_id}", headers=headers)
    return response


def delete_project(project_id):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = base._delete(endpoint=f"/api/projects/{project_id}", headers=headers)
    return response
