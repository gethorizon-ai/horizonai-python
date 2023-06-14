"""Defines methods for Task objects."""

import horizonai
from . import base


def list_tasks(verbose: bool = False):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    payload = {"verbose": verbose}
    response = base._get(
        endpoint="/api/tasks",
        json=payload,
        headers=headers,
    )
    return response


def create_task(
    name: str,
    project_id: int,
    allowed_models: list,
    task_type: str = "text_generation",
):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    if type(allowed_models) != list or len(allowed_models) == 0:
        raise Exception("Must provide list with at least one allowed model.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    payload = {
        "name": name,
        "task_type": task_type,
        "project_id": project_id,
        "allowed_models": allowed_models,
    }
    response = base._post(
        endpoint="/api/tasks/create",
        json=payload,
        headers=headers,
    )
    return response


def get_task(task_id, verbose: bool = False):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    payload = {"verbose": verbose}
    response = base._get(
        endpoint=f"/api/tasks/{task_id}",
        json=payload,
        headers=headers,
    )
    return response


def delete_task(task_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._delete(endpoint=f"/api/tasks/{task_id}", headers=headers)
    return response


def get_task_confirmation_details(task_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._get(
        endpoint=f"/api/tasks/{task_id}/get_task_confirmation_details",
        headers=headers,
    )
    return response


def generate_task(task_id, objective):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    if horizonai.openai_api_key == None and horizonai.anthropic_api_key == None:
        raise Exception("Must set LLM provider API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    payload = {
        "task_id": task_id,
        "objective": objective,
        "openai_api_key": horizonai.openai_api_key,
        "anthropic_api_key": horizonai.anthropic_api_key,
    }
    response = base._post(endpoint="/api/tasks/generate", json=payload, headers=headers)
    return response


def deploy_task(task_id, inputs, log_deployment=False):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    if horizonai.openai_api_key == None and horizonai.anthropic_api_key == None:
        raise Exception("Must set LLM provider API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    payload = {
        "task_id": task_id,
        "inputs": inputs,
        "openai_api_key": horizonai.openai_api_key,
        "anthropic_api_key": horizonai.anthropic_api_key,
        "log_deployment": log_deployment,
    }
    response = base._post(
        endpoint="/api/tasks/deploy",
        json=payload,
        headers=headers,
    )
    return response


def upload_evaluation_dataset(task_id, file_path):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    with open(file_path, "rb") as f:
        response = base._post(
            endpoint=f"/api/tasks/{task_id}/upload_evaluation_dataset",
            files={"evaluation_dataset": f},
            headers=headers,
        )
        return response


def upload_output_schema(task_id, file_path):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    with open(file_path, "rb") as f:
        response = base._post(
            endpoint=f"/api/tasks/{task_id}/upload_output_schema",
            files={"output_schema": f},
            headers=headers,
        )
        return response


def view_deployment_logs(task_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._get(
        endpoint=f"/api/tasks/{task_id}/view_deployment_logs", headers=headers
    )
    return response


def get_active_prompt(task_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    payload = {"task_id": task_id}
    response = base._get(
        endpoint="/api/tasks/get_active_prompt",
        json=payload,
        headers=headers,
    )
    return response


def set_active_prompt(task_id, prompt_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"Content-Type": "application/json", "X-Api-Key": horizonai.api_key}
    payload = {"task_id": task_id, "prompt_id": prompt_id}
    response = base._put(
        endpoint="/api/tasks/set_active_prompt",
        json=payload,
        headers=headers,
    )
    return response
