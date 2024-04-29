import os
import json
from decouple import config
from pathlib import Path
import streamlit as st


def hide_deploy_button():
    hide_deploy_button_css = """
    <style>
        /* Replace .element-class with the actual class name or ID of the deploy button */
        .stDeployButton{
            display: none;
        }
    </style>
    """
    # Inject the CSS with the markdown component
    st.markdown(hide_deploy_button_css, unsafe_allow_html=True)


def load_task_definitions():
    with open(Path(config("PROJECT_ROOT")) / "app" / "tasks" / "task_definitions.json") as f:
        return json.load(f)


def load_workflow_definition(workflow_alias: str, workflow_version: str):
    with open(Path(config(
            "PROJECT_ROOT")) / "app" / "workflows" / f"{workflow_alias}_{workflow_version}/flow_definition.json") as f:
        return json.load(f)


def get_alias_and_version(workflow_path: str) -> dict:
    version = workflow_path.split("_")[-1]
    alias = workflow_path[0:workflow_path.index(version) - 1]
    return {
        "alias": alias,
        "version": version,
        "label": workflow_path
    }


def list_workflows():
    workflows = [f for f in os.listdir(Path(config("PROJECT_ROOT")) / "app" / "workflows") if
                 os.path.isdir(Path(config("PROJECT_ROOT")) / "app" / "workflows" / f)]
    return [
        get_alias_and_version(workflow) for workflow in workflows
    ]
