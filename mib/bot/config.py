from os import makedirs, open, close, remove
from os.path import expanduser, join
from json import load, dump
from typing import Any



class Config:

    config_file = None
    data = {}
    version = None

    def __init__(self, version: str, config_name: str = 'config', config_path: str = None) -> None:
        """ Initiate paths """

        if config_path is None:
            config_path = expanduser('.local/etc/mib')
        
        makedirs(config_path, exist_ok=True)

        self.config_file = join(config_path, f"{config_name}.json")

    def load(self) -> bool:
        """ Load config from file """

        try:
            cf = open(self.config_file, 'r')
        except OSError:
            return False
        
        self.data = load(cf)
        close(cf)

        return True

    def get(self, key: str, default: Any = None) -> Any:
        """ Get config value """

        try:
            return self.data[key]
        except KeyError:
            return default
    
    def set(self, data: dict, persist: bool = False) -> None:
        """ Set config value """

        self.data.update(data)

        if persist:
            """ Write config """
            try:
                remove(self.config_file)
            except OSError:
                """ Nothing to do """
                pass
            cf = open(self.config_file, 'w')

            dump(self.data, cf)
            close(cf)
