import socket
import ssl
from time import sleep


class Stream:

    connection = None
    throttle = None

    def __init__(self, throttle: int = 200) -> None:
        self.throttle = throttle / 1000

    def connect(self, host: str, port: int = 6667, use_ssl: bool = False) -> None:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        if use_ssl:
            """
            Create ssl context without verification of certificates, given that most IRC servers use self-signed
            certificates and therefore can't go through normal verification.
            """
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            self.connection = context.wrap_socket(sock)
        else:
            self.connection = sock

    def disconnect(self) -> None:
        """
        Reset the socket so that we can establish a new connection on reconnect without errors
        :return:
        """

        try:
            self.connection.close()
        except AttributeError:
            """ There's no connection to close, skip this """
            pass

        self.connection = None

    def receive(self) -> str:
        self.connection.settimeout(1/5)  # This is here to prevent blocking of the main loop

        try:
            return self.connection.recv(1024).decode('utf-8')
        except TimeoutError:
            return ''

    def send(self, message: str) -> bool:
        data = bytes(f"{message}\r\n", "utf-8")
        self.connection.settimeout(5)

        try:
            self.connection.settimeout(data)
        except (
            TimeoutError,
            ConnectionError,
            ConnectionAbortedError,
            ConnectionRefusedError,
            ConnectionResetError
        ):
            """ Connection Failed """
            return False

        if self.throttle > 0 and self.throttle is not None:
            sleep(self.throttle)

        return True
