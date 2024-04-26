from datetime import datetime
import json
import os
import sys
import uuid
import appdirs
import logging
from pathlib import Path
from colorama import Fore, Style
from dotenv import load_dotenv
import threading
import asyncio
import pkg_resources
from PIL import Image
from plyer import notification

# Load environment variables from .env file
load_dotenv()

# Get application URL and API path from environment variables
APP_URL = os.getenv("APP_URL", "https://devassistant.tonet.dev")
API_PATH = os.getenv("API_PATH", "api")
API_URL = f"{APP_URL}/{API_PATH}"

CALLBACK_URL=f"{os.getenv('CALLBACK_URL', APP_URL)}/{API_PATH}"

# Define the exclusive directory for dot files
app_name = "dev-assistant" if APP_URL == "https://devassistant.tonet.dev" else "dev-assistant-local"
DOTFILES_DIR = Path(appdirs.user_data_dir(app_name))
DOTFILES_DIR.mkdir(parents=True, exist_ok=True)

# Define file paths for token, user data, ably token and client id
TOKEN_FILE = DOTFILES_DIR / "auth_token"
USER_DATA_FILE = DOTFILES_DIR / "user_data"
ABLY_TOKEN_FILE = DOTFILES_DIR / "ably_token"
CLIENT_ID_FILE = DOTFILES_DIR / "client_id"
STATE = DOTFILES_DIR / "state.json"

# Get certificate file and key file paths from environment variables
CERT_FILE = os.getenv("CERT_FILE", "")
KEY_FILE = os.getenv("KEY_FILE", "")

# Function to print arguments and exit the program
def dd(*args):
    """
    Function similar to 'dump and die' from Laravel
    """
    for arg in args:
        print(arg)
    sys.exit(1)

# Function to get the client id
def get_client_id():
    try:
        # Try to read the client id from the file
        return CLIENT_ID_FILE.read_text()
    except FileNotFoundError:
        # If the file does not exist, generate a new client id
        client_id = str(uuid.uuid4())
        # Save the client id to the file
        CLIENT_ID_FILE.write_text(client_id)
        # Return the client id
        return client_id

# Get the client id
CLIENT_ID = get_client_id()
    
# Define headers for API requests
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "DevAssistantCLI/0.0.2",
}

# Function to flatten a dictionary
def flatten_dict(d, parent_key="", sep="."):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            # If the value is a dictionary, flatten it
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Function to print a JSON object
def print_json(request):
    print(json.dumps(request, indent=4))

# Function to get the current date and time TODO: Fix this, pls
def now():
    # Return just the date and time in a string format
    return Fore.LIGHTGREEN_EX + "\u203A " + Style.RESET_ALL # TODO: Fix this, pls

# Function to read the token from the file
def read_token():
    try:
        return TOKEN_FILE.read_text()
    except FileNotFoundError:
        # If the token file does not exist, return None
        return None

# Function to save the token to the file
def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token)

# Function to delete the token file
def delete_token():
    TOKEN_FILE.unlink()
    
class StateManager:
    def __init__(self):
        self.state_file = STATE
        self.state = self._load_state()

    def _load_state(self):
        try:
            with open(self.state_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error("State file not found, returning default state.")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from state file: {e}")
            return {}

    def _save_state(self):
        temp_file = f"{self.state_file}.tmp"
        with open(temp_file, 'w') as file:
            json.dump(self.state, file)
        os.rename(temp_file, self.state_file)

    def get_state(self):
        return self.state

    def set_state(self, state):
        # Update the current state with the provided state
        self.state.update(state)
        self._save_state()

    def clear_state(self):
        self.state = {}
        self._save_state()
        
    def get_or_set(self, key, default_value):
        if key not in self.state:
            self.state[key] = default_value
            self._save_state()
        return self.state[key]

    def delete_key(self, key):
        if key in self.state:
            del self.state[key]
            self._save_state()

    def has_key(self, key):
        return key in self.state

    def get_keys(self):
        return list(self.state.keys())

    def get_values(self):
        return list(self.state.values())

    def get_items(self):
        return list(self.state.items())