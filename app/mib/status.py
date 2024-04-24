"""
Status Module
"""

from typing import Any

class Status:
    """
    Status class

    Manages application state
    """

    state: dict[str, Any] = {}

    def clear(self) -> None:
        """
        Clear all states
        """
        self.state = {}

    def update(self, states: dict[str, Any]) -> None:
        """
        Update current states
        """
        self.state.update(states)

    def get(self, state: str, default: Any = None) -> Any:
        """
        Get current state
        """
        try:
            return self.state[state]
        except KeyError:
            return default
