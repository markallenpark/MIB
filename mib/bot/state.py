from typing import Any


class State:

    status = {}

    def reset(self) -> None:
        self.status = {}
    
    def set(self, states: dict) -> None:
        self.status.update(states)
    
    def get(self, key: str, default: Any = None) -> Any:
        try:
            return self.status[key]
        except KeyError:
            return default
