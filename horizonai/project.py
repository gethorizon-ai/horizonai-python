"""Defines methods for Project objects."""
from base import api_key, _get, _post, _delete


def list_projects():
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = _get(endpoint="/api/projects", headers=headers)
    return response


def create_project(name):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": api_key}
    data = {"name": name}
    response = _post(
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
    response = _get(
        endpoint=f"/api/projects/{project_id}", headers=headers)
    return response


def delete_project(project_id):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = _delete(
        endpoint=f"/api/projects/{project_id}", headers=headers)
    return response
