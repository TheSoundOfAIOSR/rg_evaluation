"""
This script turns the dbConfig.json file into environment variables.
This script will first check to see if these variables are already defined
(e.g. by Github Secrets (see https://docs.github.com/en/actions/reference/encrypted-secrets)).
"""
import os
import json
from collections import defaultdict
from utils import load_json
from constants import VAR_NAMES, CONFIG_FILE


class Config:
    def __init__(self) -> None:
        pass

    def is_defined_in_environ(var_names):
        """
        return true if all are defined in the environment. Otherwise false.
        """
        return all([name.upper() in os.environ for name in var_names])

    def config_from_environment(var_names):
        config = defaultdict()

        for var_name in var_names:
            config[var_name] = os.environ[var_name.upper()]

        print("Config loaded from environment variables.")

        return config

    def config_from_file(config_file):
        """ Load the config from the config file."""

        print("Environment variables not found. Attemping to load from dbConfig.json.")
        try:
            DBParameters = load_json(config_file)
        except FileNotFoundError:
            print(f"Please obtain {config_file} from 6-evaluation-osr slack channel.")
            raise FileNotFoundError
        config = DBParameters["sofai_evalDB"]
        print("Config successfully loaded from file.")

        return config

    def load_config(var_names=VAR_NAMES, config_file=CONFIG_FILE):
        """
        Attempts to load the config from environment variables. Otherwise tries to load from the config file.
        """

        if Config.is_defined_in_environ(var_names):
            return Config.config_from_environment(var_names)
        else:
            return Config.config_from_file(config_file)
