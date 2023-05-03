import horizonai
import os
import json
import click
import configparser
from requests.exceptions import HTTPError


config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.horizonai.cfg"))


@click.group()
def cli():
    pass


@click.group()
def user():
    pass


@click.group()
def project():
    pass


@click.group()
def task():
    pass


@click.group()
def evaluation_dataset():
    pass


@click.group()
def prompt():
    pass


# User-related methods
# Generate new Horizon API key for user
@click.command(name="api-key")
@click.option("--email", prompt="Email", help="The email for the user.")
@click.password_option(
    "--password", prompt="Password", help="The password for the user."
)
def generate_new_api_key(email, password):
    try:
        result = horizonai.generate_new_api_key(email, password)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Project-related methods
# List projects
@click.command(name="list")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
def list_projects(horizon_api_key):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.list_projects()
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Create project
@click.command(name="create")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option(
    "--name", prompt="Project name", help="The name of the project to create."
)
def create_project(name, horizon_api_key):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.create_project(name)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Get Project
@click.command(name="get")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option(
    "--project_id", prompt="Project ID", help="The ID of the project to retrieve."
)
def get_project(project_id, horizon_api_key):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.get_project(project_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Update Project
@click.command(name="update")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option(
    "--project_id", prompt="Project ID", help="The ID of the project to update."
)
@click.option("--description", help="The new description for the project.")
@click.option("--status", help="The new status for the project.")
def update_project(project_id, horizon_api_key, description=None, status=None):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.update_project(project_id, description, status)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Delete Project
@click.command(name="delete")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option(
    "--project_id", prompt="Project ID", help="The ID of the project to delete."
)
def delete_project(project_id, horizon_api_key):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.delete_project(project_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Task-related methods
# List Tasks
@click.command(name="list")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
def list_tasks(horizon_api_key):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.list_tasks()
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Create Task record and generate prompt for it
@click.command(name="generate")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option("--name", prompt="Task name", help="The name of the task to create.")
@click.option(
    "--project_id",
    prompt="Associated project ID",
    help="The ID of the project that the task belongs to.",
)
# @click.option('--task_type', prompt='Task type', help='The type of the task to create.')
@click.option(
    "--task_type", default="text_generation", help="The type of the task to create."
)
@click.option(
    "--objective",
    prompt="Task objective",
    help="The objective of the task to generate.",
)
@click.option(
    "--file_path",
    prompt="Evaluation data file path",
    help="The path to the file containing the evaluation datasets to upload.",
)
def generate_task(
    name,
    project_id,
    task_type,
    objective,
    file_path,
    horizon_api_key,
):
    horizonai.api_key = horizon_api_key

    # Ask user which models they'd like to include
    allowed_models = []
    if click.confirm("Include [OpenAI]-[gpt-3.5-turbo]?"):
        allowed_models.append("gpt-3.5-turbo")
    if click.confirm("Include [OpenAI]-[text-davinci-003]?"):
        allowed_models.append("text-davinci-003")
    if click.confirm("Include [Anthropic]-[claude-instant-v1]?"):
        allowed_models.append("claude-instant-v1")
    if click.confirm("Include [Anthropic]-[claude-v1]?"):
        allowed_models.append("claude-v1")
    if len(allowed_models) == 0:
        raise Exception("Must select at least one model to include")

    # Set appropriate LLM API keys
    if "gpt-3.5-turbo" in allowed_models or "text-davinci-003" in allowed_models:
        if os.environ.get("OPENAI_API_KEY"):
            horizonai.openai_api_key = os.environ.get("OPENAI_API_KEY")
        else:
            horizonai.openai_api_key = click.prompt(
                text="OpenAI API Key (text hidden)", hide_input=True
            )
    if "claude-instant-v1" in allowed_models or "claude-v1" in allowed_models:
        if os.environ.get("ANTHROPIC_API_KEY"):
            horizonai.anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
        else:
            horizonai.anthropic_api_key = click.prompt(
                text="Anthropic API Key (text hidden)", hide_input=True
            )

    click.echo(
        f"Evaluating the following models for task generation: {allowed_models}")

    # Create task record
    try:
        task_creation_response = horizonai.create_task(
            name, task_type, project_id, allowed_models
        )
        task_id = task_creation_response["task"]["id"]
    except Exception as e:
        click.echo("Failed in task creation")
        click.echo(str(e))
        return

    # Upload evaluation dataset
    try:
        upload_dataset_response = horizonai.upload_evaluation_dataset(
            task_id, file_path
        )
    except Exception as e:
        # If uploading evaluation dataset fails, then delete previously created task
        horizonai.delete_task(task_id)
        click.echo("Failed in dataset upload")
        click.echo(str(e))
        return

    # Confirm key details of task creation (e.g., estimated cost) with user before proceeding
    try:
        task_confirmation_details_response = horizonai.get_task_confirmation_details(
            task_id
        )
        task_confirmation_details = task_confirmation_details_response[
            "task_confirmation_details"
        ]
    except Exception as e:
        # If error with getting task confirmation details, then clean up task record and evaluation dataset before raising exception
        horizonai.delete_task(task_id)
        click.echo("Failed in task confirmation details")
        click.echo(str(e))
        return

    click.echo("=====")
    click.echo(
        "Please confirm the following parameters for your task creation request:"
    )
    click.echo("")
    click.echo(f"1) Task objective: {objective}")
    click.echo("")
    click.echo(
        f"2) Input variables: {task_confirmation_details['input_variables']}")
    click.echo(
        "* Inferred based on the headers of all but the right-most column in your evaluation dataset."
    )
    click.echo("")
    click.echo(
        f"3) Estimated LLM provider cost: ${task_confirmation_details['cost_estimate']['total_cost']['low']}-{task_confirmation_details['cost_estimate']['total_cost']['high']}"
    )
    click.echo(
        "* This is entirely the LLM provider cost and not a Horizon charge. Actual cost may vary."
    )
    click.echo("=====")

    # Cancel task creation if user does not give confirmation
    if not click.confirm("Proceed with task creation?"):
        # Delete task and evaluation dataset, and abort operation
        horizonai.delete_task(task_id)
        click.echo("Cancelled task creation.")
        return

    # Given user's confirmation, continue with task creation
    try:
        click.echo("Proceeding with task creation...")
        generate_response = horizonai.generate_task(task_id, objective)
    except Exception as e:
        # If error with generating task, then clean up task record and evaluation dataset before raising exception
        horizonai.delete_task(task_id)
        click.echo("Failed in task generation")
        click.echo(str(e))
        return

    # Print task generation response
    click.echo("=====")
    formatted_output = json.dumps(generate_response, indent=4)
    click.echo(formatted_output)


# Get Task
@click.command(name="get")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option("--task_id", prompt="Task ID", help="The ID of the task to retrieve.")
def get_task(task_id, horizon_api_key):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.get_task(task_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Delete Task
@click.command(name="delete")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option("--task_id", prompt="Task ID", help="The ID of the task to delete.")
def delete_task(task_id, horizon_api_key):
    horizonai.api_key = horizon_api_key
    try:
        result = horizonai.delete_task(task_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except HTTPError as e:
        click.echo(f"Error deleting task (HTTP Error): {str(e)}")
    except Exception as e:
        click.echo(f"Error deleting task: {str(e)}")


# Deploy a task
@click.command(name="deploy")
@click.option(
    "--horizon_api_key",
    default=os.environ.get("HORIZON_API_KEY"),
    prompt="Horizon API Key" if not os.environ.get(
        "HORIZON_API_KEY") else False,
    help="The Horizon API key for the user.",
    hide_input=True,
)
@click.option("--task_id", prompt="Task ID", help="The ID of the task to deploy.")
@click.option(
    "--inputs", prompt="Inputs", help="The inputs to the task in JSON format."
)
@click.option(
    "--openai_api_key",
    default=os.environ.get("OPENAI_API_KEY"),
    prompt="OpenAI API Key (text hidden; type 'skip' if you're not using OpenAI)"
    if not os.environ.get("OPENAI_API_KEY")
    else False,
    help="The OpenAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--anthropic_api_key",
    default=os.environ.get("ANTHROPIC_API_KEY"),
    prompt="Anthropic API Key (text hidden; type 'skip' if you're not using Anthropic)"
    if not os.environ.get("ANTHROPIC_API_KEY")
    else False,
    help="The Anthropic API key for the user.",
    hide_input=True,
)
def deploy_task(task_id, inputs, horizon_api_key, openai_api_key, anthropic_api_key):
    horizonai.api_key = horizon_api_key
    horizonai.openai_api_key = openai_api_key
    horizonai.anthropic_api_key = anthropic_api_key
    try:
        inputs_dict = json.loads(inputs)
        result = horizonai.deploy_task(task_id, inputs_dict)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Add CLI commands to their respective groups
cli.add_command(user)
cli.add_command(project)
cli.add_command(task)

# User-related commands
user.add_command(generate_new_api_key)

# Project-related commands
project.add_command(list_projects)
project.add_command(create_project)
project.add_command(get_project)
project.add_command(delete_project)

# Task-related commands
task.add_command(list_tasks)
task.add_command(generate_task)
task.add_command(get_task)
task.add_command(delete_task)
task.add_command(deploy_task)

# Enable auto-completion
try:
    import click_completion

    click_completion.init()
except ImportError:
    pass

if __name__ == "__main__":
    cli()
