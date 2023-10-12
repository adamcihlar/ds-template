import os
from dotenv import load_dotenv
import yaml
from loguru import logger
from typing import List

from config import paths


def load_config(config_name: str):
    """
    Load configuration yaml file.
    Provide the config_name that identifies the particular configuration.
    """
    with open(paths.CONFIG_PATH) as file:
        config = yaml.safe_load_all(file)
        for conf in config:
            if conf["name"] == config_name:
                return conf
        logger.error(f'No configuration named "{config_name}".')
        pass


def load_env(var_names: List, path_to_env=paths.ENV) -> List:
    """
    Load the .env file and get the desired variables (typically defined in
    config.yaml).
    """
    load_dotenv(path_to_env)
    env_vars = []
    for var in var_names:
        env_vars.append(os.getenv(var))
    return env_vars
