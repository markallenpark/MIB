"""
IRC Bot Client Module
"""

from mib.config import Config
from mib.status import Status
from mib.irc import api
from mib.irc import parser
from mib.network.stream import Stream
from mib.util import chrono
import re

class Client:
    """
    IRC Bot Client Class
    """

    config: Config = Config()
    stream: Stream = Stream()
    state: Status = Status()
    buffer: str = ''

    def run(self) -> None:
        """
        Run the bot
        """

        self.state.clear()  # Reset all states
        self.buffer = ''    # Reset buffer
        self.connect()      # Connect to IRC
        self.loop()

        if self.state.get('restart', False):
            self.run()

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

    def send(self, message: str) -> None:
        """
        Send data to IRC
        """

        connected = self.stream.send(message)
        self.state.update({'connected': connected})

        if self.state.get('connected', False):
            print(f">> {message}")

    def keep_alive(self) -> None:
        """
        Maintain connection to IRC
        """

        last_ping = self.state.get('last_ping')
        current_time = chrono.monotonic_ms()

        if last_ping is None or current_time - last_ping > 120000:
            self.send(api.send_ping(str(current_time)))
            self.state.update({'last_ping': current_time})

    def get_lines(self) -> list:
        """
        Split buffer into API lines
        """
        new_buff = self.stream.receive()

        match new_buff:
            case None:
                return []
            case '':
                return []
            case self.buffer:
                return []
            case _:
                self.buffer += new_buff

        lines = self.buffer.split('\n') # Split on line feeds

        if self.buffer[-1] != '\n':
            self.buffer = lines[-1]

        del lines[-1]

        out = []

        for line in lines:
            line = re.sub(r'\s+', ' ', line) # remove extra whitespaces
            out.append(line.strip())

        return out

    def handle(self, event: dict) -> None:
        """
        Handle events
        """
        match event['type']:
            case '001':
                # Update the connection as being registered
                self.state.update({'registered': True})
                for channel in self.config.get('irc', 'channels', []):
                    # Join any configured channels
                    self.send(api.channel_join(channel))
            case 'ping':
                # Respond to pings
                self.state.update({'last_ping': chrono.monotonic_ms})
                self.send(api.send_pong(event['message']))

    def loop(self) -> None:
        """
        Collect data from server and loop through event parsers and handlers
        """
        while self.state.get('connected', False):
            if self.state.get('registered', False):
                self.keep_alive()

            lines = self.get_lines()

            for line in lines:
                self.handle(parser.parse(line))
