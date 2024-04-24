"""
IRC Bot Client Module
"""

from mib.config import Config
from mib.status import Status
from mib.irc import api
from mib.network.stream import Stream

class Client:
    """
    IRC Bot Client Class
    """

    config: Config = Config()
    stream: Stream = Stream()
    state: Status = Status()

    def __init__(self) -> None:
        """
        Initialize the class
        """
        self.config.load('irc')

    def run(self) -> None:
        """
        Run the bot
        """

        self.state.clear() # Reset all states
        self.connect()

    def connect(self) -> None:
        """
        Connect to IRC
        """

        server = self.config.get('irc', 'server')
        port = self.config.get('irc', 'port', 6667)
        use_ssl = self.config.get('irc', 'ssl', False)
        nickname = self.config.get('irc', 'nickname')
        username = self.config.get('irc', 'username')
        realname = self.config.get('irc', 'realname')

        self.stream.connect(server, port, use_ssl)
        self.send(api.set_nickname(nickname))
        self.send(api.set_username(username, realname))

    def send(self, api: str) -> None:
        """
        Send data to IRC
        """

        connected = self.stream.send(api)
        self.state.update({'connected': connected})

        if self.state.get('connected', False):
            print(f">> {api}")
