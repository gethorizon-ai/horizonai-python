# Horizon AI Python Library

The Horizon AI Python library provides convenient access to a command line interface (CLI) and the Horizon AI API for applications written in the Python language.

## Installation
Run `pip install horizonai` on the command line.

## Overview

Building production applications using Large Language Models (LLMs) requires expertise and manual effort across prompt engineering, model selection, and supporting infrastructure (e.g., continuous optimization, vector DBs).

Horizon AI provides a hosted API to abstract and simplify the deployment of production LLM applications. You specify your objective in a plain English statement and upload an evaluation dataset, then Horizon programmatically identifies, configures, and manages the best LLM and prompt for your unique use case. After this is done, Horizon gives you an API that you can call to get outputs for your generative AI use case. All the configuration details (e.g., LLM selected, LLM parameters, prompt string) are accessible.

## Documentation

Please see [here](https://docs.gethorizon.ai) for full documentation on:
- Getting started (installation, setting up the environment, simple examples)
- How-To examples (demos, integrations, helper functions)
- Reference (full API docs)

## Usage

1. Create an account [here](https://app.gethorizon.ai/login)
2. Create a Horizon API key: run `horizon user api-key` on the command line
3. Generate a Task: run `horizon task generate` on the command line
4. Deploy your task: run `horizon task deploy` on the command line or call `horizonai.deploy_task` from the Python package
