"""Defines methods for Task objects."""

from . import base


def list_tasks():
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = base._get(endpoint="/api/tasks", headers=headers)
    return response


def create_task(
    name: str,
    task_type: str,
    project_id: int,
    allowed_models: list,
):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    if type(allowed_models) != list or len(allowed_models) == 0:
        raise Exception("Must provide list with at least one allowed model.")
    headers = {"Content-Type": "application/json", "X-Api-Key": api_key}
    payload = {
        "name": name,
        "task_type": task_type,
        "project_id": project_id,
        "allowed_models": allowed_models,
    }
    response = base._post(endpoint="/api/tasks/create", json=payload, headers=headers)
    return response


def get_task(task_id):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = base._get(endpoint=f"/api/tasks/{task_id}", headers=headers)
    return response


def delete_task(task_id):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = base._delete(endpoint=f"/api/tasks/{task_id}", headers=headers)
    return response


def get_task_confirmation_details(task_id):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    response = base._get(
        endpoint=f"/api/tasks/{task_id}/get_task_confirmation_details",
        headers=headers,
    )
    return response


def generate_task(task_id, objective):
    global api_key, openai_api_key, anthropic_api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": api_key}
    payload = {
        "task_id": task_id,
        "objective": objective,
        "openai_api_key": openai_api_key,
        "anthropic_api_key": anthropic_api_key,
    }
    response = base._post(endpoint="/api/tasks/generate", json=payload, headers=headers)
    return response


def deploy_task(task_id, inputs):
    global api_key, openai_api_key, anthropic_api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": api_key}
    payload = {
        "task_id": task_id,
        "inputs": inputs,
        "openai_api_key": openai_api_key,
        "anthropic_api_key": anthropic_api_key,
    }
    response = base._post(endpoint="/api/tasks/deploy", json=payload, headers=headers)
    return response


def upload_evaluation_dataset(task_id, file_path):
    global api_key
    if api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": api_key}
    with open(file_path, "rb") as f:
        response = base._post(
            endpoint=f"/api/tasks/{task_id}/upload_evaluation_dataset",
            files={"evaluation_dataset": f},
            headers=headers,
        )
        return response
