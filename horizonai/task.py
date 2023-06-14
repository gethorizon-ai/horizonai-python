"""Defines methods for Task objects."""

import horizonai
from . import base
import time
import requests


def list_tasks():
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._get(endpoint="/api/tasks", headers=headers)
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
    headers = {"Content-Type": "application/json",
               "X-Api-Key": horizonai.api_key}
    payload = {
        "name": name,
        "task_type": task_type,
        "project_id": project_id,
        "allowed_models": allowed_models,
    }
    response = base._post(endpoint="/api/tasks/create",
                          json=payload, headers=headers)
    return response


def get_task(task_id):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    headers = {"X-Api-Key": horizonai.api_key}
    response = base._get(endpoint=f"/api/tasks/{task_id}", headers=headers)
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
    headers = {"Content-Type": "application/json",
               "X-Api-Key": horizonai.api_key}
    payload = {
        "task_id": task_id,
        "objective": objective,
        "openai_api_key": horizonai.openai_api_key,
        "anthropic_api_key": horizonai.anthropic_api_key,
    }
    response = base._post(endpoint="/api/tasks/generate",
                          json=payload, headers=headers)
    return response


def deploy_task(task_id, inputs, log_deployment=False):
    if horizonai.api_key == None:
        raise Exception("Must set Horizon API key.")
    if horizonai.openai_api_key == None and horizonai.anthropic_api_key == None:
        raise Exception("Must set LLM provider API key.")
    headers = {"Content-Type": "application/json",
               "X-Api-Key": horizonai.api_key}
    payload = {
        "task_id": task_id,
        "inputs": inputs,
        "openai_api_key": horizonai.openai_api_key,
        "anthropic_api_key": horizonai.anthropic_api_key,
        "log_deployment": log_deployment,
    }
    for i in range(10):
        try:
            response = base._post(
                endpoint="/api/tasks/deploy", json=payload, headers=headers)
            break
        except requests.exceptions.ConnectionError:
            # If the request fails due to a connection error (e.g., server is down),
            # it will wait 10 seconds and then try again, upto 10 times
            if i < 9:
                time.sleep(10)
        except Exception as e:
            # If any other exception occurs, we raise it immediately without retrying
            raise e
    else:
        raise Exception(
            "Max retries exceeded. Please contact support at team@gethorizon.ai")
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
