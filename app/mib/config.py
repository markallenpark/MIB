"""
Config Module
"""

import json
from os import path, makedirs, remove
from typing import Any

class Config:
    """
    Handle application configurations
    """

    config: dict[str, dict] = {}
    path: str = '/etc/mib'

    def __init__(self) -> None:
        """
        Initialize config path
        """
        makedirs(self.path, exist_ok=True)

    def load(self, name: str) -> None:
        """
        Read configuration file

        name: str   - Configuration name
        """
        file = path.join(self.path, f"{name}.json")

        if not path.exists(file):
            raise FileNotFoundError(f"Unable to load configuration file: {file}")

        with open(file, mode="r", encoding="utf-8") as cf:
            self.config.update({name: json.load(cf)})

    def get(self, group: str, key: str, default: Any = None) -> Any:
        """
        Retrieve configuration value

        group   : str       - Config group
        key     : str       - Config key
        default : Any       - Default result ( defaults to None )
        """

        try:
            return self.config[group][key]
        except KeyError:
            return default

    def set(self, group: str, config: dict[str, Any], persist: bool = False) -> None:
        """
        Add configuration value

        group   : str       - Group to update config of
        config  : dict      - Configuration values to set
        persist : bool      - Save configuration to config file ( defaults to False )
        """
        self.config.update({group: config})

        if persist:
            file = path.join(self.path, f"{group}.json")

            if path.exists(file):
                remove(file)

            with open(file, mode="w", encoding="utf-8") as cf:
                json.dump(self.config[group], cf)
