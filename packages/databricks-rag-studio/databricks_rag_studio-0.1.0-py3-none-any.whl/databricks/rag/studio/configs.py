import os
import mlflow
import yaml
from typing import Optional


class RagConfig:
    def __init__(self, config_path: Optional[str] = None):
        _mlflow_rag_config_path = getattr(
            mlflow.langchain._rag_utils, "__databricks_rag_config_path__", None
        )
        self.config_path = _mlflow_rag_config_path or config_path

        if not self.config_path:
            raise FileNotFoundError("Config file is None. Please provide a valid path.")

        if not os.path.isfile(self.config_path):
            raise FileNotFoundError(f"Config file '{self.config_path}' not found.")

    def _read_config(self):
        """Reads the YAML configuration file and returns its contents.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            yaml.YAMLError: If there is an error parsing the YAML content.

        Returns:
            dict or None: The content of the YAML file as a dictionary, or None if the config path is not set.
        """
        with open(self.config_path, "r") as file:
            try:
                return yaml.safe_load(file)
            except yaml.YAMLError as e:
                raise yaml.YAMLError(f"Error parsing YAML file: {e}")

    def get(self, key):
        """Gets the value of a top-level parameter in the configuration."""
        config_data = self._read_config()

        if config_data and key in config_data:
            return config_data[key]
        else:
            raise KeyError(f"Key '{key}' not found in configuration: {config_data}.")
