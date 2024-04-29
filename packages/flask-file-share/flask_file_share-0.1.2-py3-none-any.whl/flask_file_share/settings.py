"""
File: settings.py
-----------------

Settings for the File Sharing Flask application.

Description:
    This file contains configuration settings for the File Sharing Flask application. It defines constants
    such as DEBUG mode, base directory, upload folder, data file path, static folder, templates folder,
    allowed hosts, and session lifetime. It also loads environment variables from a .env file if it exists.

Usage:
    The settings are used throughout the application to configure various aspects such as file paths, session
    lifetime, and debugging mode.

Attributes:
    - DEBUG (bool): A boolean flag indicating whether the application is running in debug mode.
    - USERNAME_STR (str): The environment variable name for the username.
    - PASSWORD_STR (str): The environment variable name for the password.
    - SECRET_KEY_STR (str): The environment variable name for the secret key.
    - USERNAME (str): The username used for authentication.
    - PASSWORD (str): The password used for authentication.
    - SECRET_KEY (str): The secret key used for encryption.
    - BASE_DIR (Path): The base directory path of the application.
    - UPLOADS_DATA_DIR (Path): The directory path for storing uploaded data.
    - UPLOAD_FOLDER (Path): The directory path for storing uploaded files.
    - DATA_FILE (Path): The path to the JSON file used for storing data.
    - STATIC_FOLDER (Path): The directory path for static files.
    - TEMPLATES_FOLDER (Path): The directory path for template files.
    - ALLOWED_HOSTS (List[str]): A list of allowed hostnames or IP addresses.
    - PERMANENT_SESSION_LIFETIME_MINUTES (float): The session timeout duration in minutes.
"""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv  # pylint: disable=E0401

# Load environment variables from .env file if it exists
_DOTENV_PATH = ".env"
if os.path.exists(_DOTENV_PATH):
    logging.info("loading .env file")
    load_dotenv(_DOTENV_PATH)
else:
    logging.warning(".env file not found")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

USERNAME_STR = "FFS_USERNAME"
PASSWORD_STR = "FFS_PASSWORD"
SECRET_KEY_STR = "FFS_SECRET_KEY"

# Set values for username, password, and secret key
if not DEBUG:
    _cdt1 = USERNAME_STR in os.environ
    _cdt2 = PASSWORD_STR in os.environ
    _cdt3 = SECRET_KEY_STR in os.environ
    # Raise error if DEBUG is False and username, password, or secret key is not provided
    if not _cdt1 or not _cdt2 or not _cdt3:
        raise ValueError(
            "You must provide USERNAME, PASSWORD, and SECRET_KEY in production mode (DEBUG=False).")

    USERNAME = os.environ[USERNAME_STR]
    PASSWORD = os.environ[PASSWORD_STR]
    SECRET_KEY = os.environ[SECRET_KEY_STR]

if DEBUG:
    USERNAME = os.getenv(USERNAME_STR, "default_username")
    PASSWORD = os.getenv(PASSWORD_STR, "default_password")
    SECRET_KEY = os.getenv(SECRET_KEY_STR, "default_secret_key")

    logging.debug("DEBUG: %s", DEBUG)
    logging.debug("USERNAME: %s", USERNAME)
    logging.debug("PASSWORD: %s", PASSWORD)
    logging.debug("SECRET_KEY: %s", SECRET_KEY)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

UPLOADS_DATA_DIR = Path(os.getenv("UPLOADS_DATA_DIR", os.getcwd() + "/uploads")).resolve()
UPLOADS_DATA_DIR.mkdir(exist_ok=True)

UPLOAD_FOLDER = Path(os.getenv("UPLOAD_FOLDER", UPLOADS_DATA_DIR / "files")).resolve()
UPLOAD_FOLDER.mkdir(exist_ok=True)

DATA_FILE = Path(os.getenv("DATA_FILE", UPLOADS_DATA_DIR / "data.json")).resolve()
assert DATA_FILE.parent.exists()

STATIC_FOLDER = (BASE_DIR / "static").resolve()
if not STATIC_FOLDER.exists() or STATIC_FOLDER.is_file():
    raise NotADirectoryError(f"STATIC_FOLDER={STATIC_FOLDER} does not exists as a folder")

TEMPLATES_FOLDER = (BASE_DIR / "templates").resolve()
if not TEMPLATES_FOLDER.exists() or TEMPLATES_FOLDER.is_file():
    raise NotADirectoryError(f"TEMPLATES_FOLDER={TEMPLATES_FOLDER} does not exists as a folder")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Set the session timeout to 30 minutes (1800 seconds)
PERMANENT_SESSION_LIFETIME_MINUTES = float(os.getenv("PERMANENT_SESSION_LIFETIME_MINUTES", "30"))
assert PERMANENT_SESSION_LIFETIME_MINUTES > 0
