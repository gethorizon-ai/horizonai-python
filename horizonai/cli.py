import horizonai
import os
import json
import click
import configparser
from requests.exceptions import HTTPError
import csv

config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.horizonai.cfg"))


def count_rows(file_path):
    """Count the number of rows in a csv file. subrtract 1 for the header row."""
    with open(file_path, "r") as f:
        return sum(1 for row in csv.reader(f)) - 1


@click.group()
def cli():
    """Command line interface for Horizon AI API.\n Start with running 'horizonai user api-key' to generate a new API key."""
    pass


@click.group()
def user():
    """Manage your User account and API key."""
    pass


@click.group()
def project():
    """Create and manage your Projects."""
    pass


@click.group()
def task():
    """Create and manage your Tasks."""
    pass


@click.group()
def enabler():
    """Enabler methods such as synthetic data generation."""
    pass


# User-related methods
# Generate new HorizonAI API key for user
@click.command(name="api-key")
@click.option("--email", prompt="Email", help="The email for the user.")
def generate_new_api_key(email):
    """Generate a new HorizonAI API key."""
    password = click.prompt("Password", hide_input=True, confirmation_prompt=False)
    try:
        result = horizonai.user.generate_new_api_key(email, password)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
        click.echo('\nRun "horizonai project create" command to create a project\n')
    except Exception as e:
        click.echo(str(e))


# Enabler-related methods
# Generate synthetic data
@click.command(name="synthetic-data")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--objective",
    prompt="Task Objective",
    help="State the objective of the your task.",
)
@click.option(
    "--file_path",
    prompt="File Path",
    help="The path to the file containing the original dataset.",
)
@click.option(
    "--num_synthetic_data",
    prompt="Number of synthetic data points to generate",
    help="Number of synthetic data points to generate.",
)
@click.option(
    "--openai_api_key",
    default=os.environ.get("OPENAI_API_KEY"),
    prompt="OpenAI API Key (text hidden)"
    if not os.environ.get("OPENAI_API_KEY")
    else False,
    help="The OpenAI API key for the user.",
    hide_input=True,
)
def generate_synthetic_data(
    objective, file_path, num_synthetic_data, horizonai_api_key, openai_api_key
):
    """Generate synthetic data."""
    horizonai.api_key = horizonai_api_key
    horizonai.openai_api_key = openai_api_key
    try:
        result = horizonai.enabler.generate_synthetic_data(
            objective, num_synthetic_data, file_path
        )
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Project-related methods
# List projects


@click.command(name="list")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
def list_projects(horizonai_api_key):
    """View a list of all your Projects."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.project.list_projects()
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Create project
@click.command(name="create")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--name", prompt="Project name", help="The name of the project to create."
)
def create_project(name, horizonai_api_key):
    """Create a new Project."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.project.create_project(name)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
        click.echo('\nRun "horizonai task generate" command to create a task\n')
    except Exception as e:
        click.echo(str(e))


# Get Project
@click.command(name="get")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--project_id", prompt="Project ID", help="The ID of the project to retrieve."
)
def get_project(project_id, horizonai_api_key):
    """Get details about a specific Project."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.project.get_project(project_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Delete Project
@click.command(name="delete")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--project_id", prompt="Project ID", help="The ID of the project to delete."
)
def delete_project(project_id, horizonai_api_key):
    """Delete an existing Project."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.project.delete_project(project_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Task-related methods
# List Tasks
@click.command(name="list")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
def list_tasks(horizonai_api_key):
    """View a list of all your Tasks."""
    horizonai.api_key = horizonai_api_key
    verbose = False
    if click.confirm(
        "Verbose output (show all prompts for each task, not just active prompt)?"
    ):
        verbose = True
    try:
        result = horizonai.task.list_tasks(verbose)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Create Task record and generate prompt for it
@click.command(name="generate")
def generate_task():
    """Create a new Task with the optimal prompt-model configuration."""
    click.echo("### Step 1/3 - Task Overview ###")
    # Get HorizonAI API key
    if os.environ.get("HORIZONAI_API_KEY"):
        horizonai.api_key = os.environ.get("HORIZONAI_API_KEY")
    else:
        horizonai.api_key = click.prompt(
            text="HorizonAI API key (text hidden)", hide_input=True
        )

    # Get project ID
    project_id = click.prompt("Project ID")

    # Get task name
    task_name = click.prompt("Task name")

    # Get objective
    objective = click.prompt("Task objective")

    # Get evaluation dataset
    dataset_file_path = click.prompt("Evaluation dataset file path (.csv)")
    num_rows = count_rows(dataset_file_path)
    if num_rows < 15:
        num_synthetic_data = 15 - num_rows
        generate_synthetic_data_confirmation = click.confirm(
            f"The evaluation dataset contains {num_rows} rows. A minimum of 15 rows is required for task generation evaluations. "
            f"Would you like to generate the remaining {num_synthetic_data} rows synthetically?"
        )

        if generate_synthetic_data_confirmation:
            num_synthetic_data_input = str(
                click.prompt(
                    "Enter the number of synthetic data rows to generate or hit enter to generate the default number.",
                    default=num_synthetic_data,
                    show_default=True,
                )
            )

            # Get OpenAI API key
            if os.environ.get("OPENAI_API_KEY"):
                horizonai.openai_api_key = os.environ.get("OPENAI_API_KEY")
            else:
                horizonai.openai_api_key = click.prompt(
                    text="OpenAI API Key (text hidden)", hide_input=True
                )

            """Generate synthetic data."""
            try:
                result = horizonai.enabler.generate_synthetic_data(
                    objective, num_synthetic_data, dataset_file_path
                )
                formatted_output = json.dumps(result, indent=4)
                click.echo(formatted_output)
            except Exception as e:
                click.echo(str(e))
        else:
            click.echo(
                "The task requires a minimum of 15 rows of data. "
                "Please try again with a larger data set "
                "or generate synthetic data using the 'horizonai task generate' "
                "or 'horizonai enabler synthetic-data' command."
            )
        return

    # Get output schema, if applicable
    output_schema_file_path = None
    if click.confirm("Add JSON schema for LLM output?"):
        output_schema_file_path = click.prompt(text="Output schema file path (.json)")

    click.echo("")
    click.echo("### Step 2/3 - Model Selection ###")

    # Ask user which models they'd like to include
    allowed_models = []
    if click.confirm("Include [OpenAI]-[gpt-3.5-turbo]?"):
        allowed_models.append("gpt-3.5-turbo")
    if click.confirm("Include [OpenAI]-[gpt-3.5-turbo-16k]?"):
        allowed_models.append("gpt-3.5-turbo-16k")
    if click.confirm("Include [OpenAI]-[text-davinci-003]?"):
        allowed_models.append("text-davinci-003")
    if click.confirm("Include [Anthropic]-[claude-instant-v1]?"):
        allowed_models.append("claude-instant-v1")
    if click.confirm("Include [Anthropic]-[claude-v1]?"):
        allowed_models.append("claude-v1")
    if len(allowed_models) == 0:
        raise Exception("Must select at least one model to include")

    # Set appropriate LLM API keys
    if (
        "gpt-3.5-turbo" in allowed_models
        or "gpt-3.5-turbo-16k" in allowed_models
        or "text-davinci-003" in allowed_models
    ):
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

    # Create task record
    try:
        task_creation_response = horizonai.task.create_task(
            name=task_name,
            project_id=project_id,
            allowed_models=allowed_models,
        )
        task_id = task_creation_response["task"]["id"]
    except Exception as e:
        click.echo("Failed in task creation")
        click.echo(str(e))
        return

    # Upload evaluation dataset
    try:
        upload_dataset_response = horizonai.task.upload_evaluation_dataset(
            task_id,
            dataset_file_path,
        )
    except Exception as e:
        # If uploading evaluation dataset fails, then delete previously created task
        horizonai.task.delete_task(task_id)
        click.echo("Failed in dataset upload")
        click.echo(str(e))
        return

    # Upload output schema, if applicable
    if output_schema_file_path:
        try:
            upload_output_schema_response = horizonai.task.upload_output_schema(
                task_id, output_schema_file_path
            )
        except Exception as e:
            horizonai.task.delete_task(task_id)
            click.echo("Failed in output schema upload")
            click.echo(str(e))
            return

    # Confirm key details of task creation (e.g., estimated cost) with user before proceeding
    try:
        task_confirmation_details_response = (
            horizonai.task.get_task_confirmation_details(task_id)
        )
        task_confirmation_details = task_confirmation_details_response[
            "task_confirmation_details"
        ]
    except Exception as e:
        # If error with getting task confirmation details, then clean up task record and evaluation dataset before raising exception
        horizonai.task.delete_task(task_id)
        click.echo("Failed in task confirmation details")
        click.echo(str(e))
        return

    click.echo("")
    click.echo("### Step 3/3 - Task confirmation ###")
    click.echo(
        "Please confirm the following parameters for your task creation request:"
    )
    click.echo("")
    click.echo(f"1) Task objective: {objective}")
    click.echo("")
    click.echo(f"2) Input variables: {task_confirmation_details['input_variables']}")
    click.echo(
        "* Inferred based on the headers of all but the right-most column in your evaluation dataset."
    )
    click.echo("")
    click.echo(f"3) Models considered: {allowed_models}")
    click.echo("")
    click.echo(
        f"4) Estimated LLM provider cost: ${task_confirmation_details['cost_estimate']['total_cost']['low']}-{task_confirmation_details['cost_estimate']['total_cost']['high']}"
    )
    click.echo(
        "* This is entirely the LLM provider cost and not a Horizon charge. Actual cost may vary."
    )
    click.echo("")

    # Cancel task creation if user does not give confirmation
    if not click.confirm("Proceed?"):
        # Delete task and evaluation dataset, and abort operation
        horizonai.task.delete_task(task_id)
        click.echo("Cancelled task creation.")
        return

    # Given user's confirmation, continue with task creation
    try:
        generate_response = horizonai.task.generate_task(task_id, objective)
        formatted_output = json.dumps(generate_response, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        # If error with generating task, then clean up task record before raising exception
        horizonai.task.delete_task(task_id)
        click.echo("Failed in task generation")
        click.echo(str(e))
        return


# Get Task
@click.command(name="get")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option("--task_id", prompt="Task ID", help="The ID of the task to retrieve.")
def get_task(task_id, horizonai_api_key):
    """Get details about a specific Task."""
    horizonai.api_key = horizonai_api_key
    verbose = False
    if click.confirm("Verbose output (show all prompts, not just active prompt)?"):
        verbose = True
    try:
        result = horizonai.task.get_task(task_id, verbose)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Delete Task
@click.command(name="delete")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option("--task_id", prompt="Task ID", help="The ID of the task to delete.")
def delete_task(task_id, horizonai_api_key):
    """Delete an existing Task."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.task.delete_task(task_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except HTTPError as e:
        click.echo(f"Error deleting task (HTTP Error): {str(e)}")
    except Exception as e:
        click.echo(f"Error deleting task: {str(e)}")


# Deploy a task
@click.command(name="deploy")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option("--task_id", prompt="Task ID", help="The ID of the task to deploy.")
@click.option(
    "--inputs", prompt="Inputs", help="The inputs to the task in JSON format."
)
def deploy_task(horizonai_api_key, task_id, inputs):
    """Deploy a Task based on provided input values."""
    horizonai.api_key = horizonai_api_key

    # Determine model provider for selected task
    try:
        task_details_response = horizonai.task.get_task(task_id)
        task_details = task_details_response["task"]
        model_name = task_details["prompts"][0]["model_name"]
    except Exception as e:
        click.echo(str(e))
        return

    # Get appropriate LLM provider API key
    if model_name in ["gpt-3.5-turbo", "text-davinci-003"]:
        if os.environ.get("OPENAI_API_KEY"):
            horizonai.openai_api_key = os.environ.get("OPENAI_API_KEY")
        else:
            horizonai.openai_api_key = click.prompt(
                text="OpenAI API Key (text hidden)", hide_input=True
            )
    elif model_name in ["claude-instant-v1", "claude-v1"]:
        if os.environ.get("ANTHROPIC_API_KEY"):
            horizonai.anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
        else:
            horizonai.anthropic_api_key = click.prompt(
                text="Anthropic API Key (text hidden)", hide_input=True
            )

    log_deployment = False
    if click.confirm("Log deployment?"):
        log_deployment = True
    try:
        inputs_dict = json.loads(inputs, strict=False)
        result = horizonai.task.deploy_task(task_id, inputs_dict, log_deployment)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Download task deployment logs
@click.command(name="view-logs")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--task_id",
    prompt="Task ID",
    help="The ID of the task to view logs for.",
)
def view_deployment_logs(horizonai_api_key, task_id):
    """View Task deployment logs."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.task.view_deployment_logs(task_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Get the current active prompt of a task
@click.command(name="get-active-prompt")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--task_id",
    prompt="Task ID",
    help="The ID of the task.",
)
def get_active_prompt(horizonai_api_key, task_id):
    """Get active prompt-model configuration for task."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.task.get_active_prompt(task_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Set the current active prompt of a task
@click.command(name="set-active-prompt")
@click.option(
    "--horizonai_api_key",
    default=os.environ.get("HORIZONAI_API_KEY"),
    prompt="HorizonAI API Key" if not os.environ.get("HORIZONAI_API_KEY") else False,
    help="The HorizonAI API key for the user.",
    hide_input=True,
)
@click.option(
    "--task_id",
    prompt="Task ID",
    help="The ID of the task.",
)
@click.option(
    "--prompt_id",
    prompt="Prompt ID",
    help="The ID of the prompt to set as the current prompt for the task.",
)
def set_active_prompt(horizonai_api_key, task_id, prompt_id):
    """Set active prompt-model configuration for task."""
    horizonai.api_key = horizonai_api_key
    try:
        result = horizonai.task.set_active_prompt(task_id, prompt_id)
        formatted_output = json.dumps(result, indent=4)
        click.echo(formatted_output)
    except Exception as e:
        click.echo(str(e))


# Add CLI commands to their respective groups
cli.add_command(user)
cli.add_command(project)
cli.add_command(task)
cli.add_command(enabler)

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
task.add_command(view_deployment_logs)
task.add_command(get_active_prompt)
task.add_command(set_active_prompt)

# Enabler-related commands
enabler.add_command(generate_synthetic_data)

# Enable auto-completion
try:
    import click_completion

    click_completion.init()
except ImportError:
    pass

if __name__ == "__main__":
    cli()
