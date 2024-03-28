from os import makedirs, open, close, remove
from os.path import expanduser, join
from json import load, dump
from typing import Any



class Config:
    """ Handle configuration files """

    config_file: str = ''
    data: dict[str, Any] = {}
    version: str = ''

    def __init__(self, version: str, config_name: str = 'config', config_path: str = None) -> None:
        """ Initiate class """

        self.version = version

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

        if self.data['version'] != self.version:
            print('Incompatible config version')
            return False

        return True

    def get(self, key: str) -> Any:
        """ Get config value """
        return self.data[key]

    def set(self, data: dict, persist: bool = False) -> None:
        """ Set config value """

        self.data.update(data)

        if persist:
            # Write config
            try:
                remove(self.config_file)
            except OSError:
                # Do nothing
                pass
            cf = open(self.config_file, 'w')

            dump(self.data, cf)
            close(cf)
