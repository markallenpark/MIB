from mib.bot.config import Config
from mib.bot.state import State
from mib.bot import handler
from mib.irc import command
from mib.irc.parser import parse
from mib.network.stream import Stream
from mib.util.time import monotonic_ms


class Client:

    config = None
    status = State()
    stream = Stream()
    version = '0.0.1'

    def send(self, data: str) -> None:
        self.status.set({"connected": self.stream.send(data)})
    
    def connect(self) -> None:
        """ Ensure that socket is not set before attempting to connect """
        self.stream.disconnect()

        """ Server Settings """
        host = self.config.get('server.host')
        port = self.config.get('server.port')
        use_ssl = self.config.get('server.use_ssl')

        """ Bot Settings """
        nickname = self.config.get('bot.nickname')
        username = self.config.get('bot.username')
        realname = self.config.get('bot.realname')

        self.stream.connect(host, port, use_ssl)

        self.send(command.set_nickname(nickname))
        self.send(command.set_username(username, realname))

    def start(self):
        self.config = None  # Reset config

        self.config = Config(self.version, 'client')
        
        if not self.config.load():
            """ TODO: Run setup script """
            print("Configuration does not exist")
            quit()


        self.connect()
        self.process()

        self.status.reset()

    def keep_alive(self) -> None:
        """ Keep connection alive """

        if self.status.get('registered', False):
            current_time = monotonic_ms()
            last_ping = self.status.get('last_ping')

            if last_ping is None or current_time - last_ping > 300000:
                last_ping = current_time
                self.send(command.send_ping(str(current_time)))

    def respond(self, responses: dict) -> None:
        try:
            commands = responses['commands']
        except KeyError:
            commands = []
        
        try:
            states = responses['states']
        except KeyError:
            states = {}
        
        self.status.set(states)

        for response in commands:
            self.send(response)
    
    def handle(self, event: dict) -> None:
        handler.handle(event)

    def process(self) -> None:
        """ Main script loop """

        buffer = ""  # Reset buffer

        while self.status.get('connected', False):
            self.keep_alive()

            new_buff = self.stream.receive()

            match new_buff:
                case None:
                    continue
                case '':
                    continue
                case buffer:
                    continue
            
            buffer += new_buff

            lines = buffer.split('\n')

            if buffer[-1] != '\n':
                buffer = lines[-1]
            else:
                buffer = ''
            
            del lines[-1]

            for line in lines:
                line = line.strip()

                event = parse(line)

                self.handle(event)
