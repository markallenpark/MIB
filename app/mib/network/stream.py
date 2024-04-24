"""
Stream Module
---

Handles network connection
"""

from socket import socket, AF_INET, SOCK_STREAM
import ssl
from time import sleep

class Stream:
    """
    Stream class
    """

    connection: socket | None = None
    throttle: float | None = None

    def __init__(self, throttle: int | None = None) -> None:
        """
        Initialize the class
        """

        if throttle is not None:
            self.throttle = throttle / 1000


    def disconnect(self) -> None:
        """
        Disconnect from server
        """

        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def connect(self, host: str, port: int = 6667, use_ssl: bool = False) -> None:
        """
        Connect to server
        """
        self.disconnect()
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))

        if use_ssl:
            ##
            # Use SSL/TLS to encrypt connection
            #
            # This is buggy. I'm not sure why.
            #
            # Note:   check_hostname and verify mode disabled as most IRC servers
            #         use self-signed certificates.
            #

            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            self.connection = context.wrap_socket(sock)
        else:
            self.connection = sock

    def receive(self) -> str | None:
        """
        Get data from socket
        """

        if self.connection is None:
            raise ConnectionError

        self.connection.settimeout(1/5)

        try:
            return self.connection.recv(1500).decode('utf-8')
        except TimeoutError:
            return None

    def send(self, text: str) -> bool:
        """
        Send data to socket
        """

        if self.connection is None:
            return False

        self.connection.settimeout(5)
        data = bytes(f"{text}\r\n", "utf-8")

        try:
            self.connection.send(data)
        except (
            TimeoutError,
            ConnectionError,
            ConnectionAbortedError,
            ConnectionRefusedError,
            ConnectionResetError
        ):
            return False

        if self.throttle is not None:
            sleep(self.throttle)

        return True
