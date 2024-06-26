"""
App Module
"""

from mib.client import Client

class App(Client):
    """
    App class
    """

    def __init__(self) -> None:
        """
        Initialize the class
        """
        self.config.load('irc')

if __name__ == "__main__":
    App().run()
