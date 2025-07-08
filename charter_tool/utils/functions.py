import os
import json
import yaml
from datetime import datetime
import streamlit as st

def save_config_to_file(project_config):
    os.makedirs("configs", exist_ok=True)
    project_name = project_config.get("project_name", "untitled_project")
    safe_project_name = "".join(c for c in project_name.lower() if c.isalnum() or c in (' ', '_')).replace(' ', '_')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"configs/{safe_project_name}_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(project_config, f, indent=2, default=str)
    st.toast(f"Configuration saved to `{filename}`")
    return filename

def load_config_from_file(filename):
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        st.error(f"Error loading config: {e}")
        return None

def load_charter():
    CHARTER_CONFIG_PATH = "configs/project_charter.yaml"
    if os.path.exists(CHARTER_CONFIG_PATH):
        with open(CHARTER_CONFIG_PATH, 'r') as file:
            return yaml.safe_load(file)
    return {}

def save_charter(data):
    CHARTER_CONFIG_PATH = "configs/project_charter.yaml"
    os.makedirs(os.path.dirname(CHARTER_CONFIG_PATH), exist_ok=True)
    with open(CHARTER_CONFIG_PATH, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
