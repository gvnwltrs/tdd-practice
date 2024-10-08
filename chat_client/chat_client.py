from .connection import Connection
from .connection import Connection
class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname
        self._connection = None

    def send_message(self, message: str) -> str:
        sent_message = f"{self.nickname}: {message}"
        self.connection.broadcast(sent_message)
        return sent_message
    
    @property
    def connection(self):
        if self._connection is None:
            self._connection = self._get_connection()
        return self._connection

    @connection.setter
    def connection(self, value):
        if self._connection is not None:
            self._connection.close()
        self._connection = value

    def _get_connection(self):
        return Connection(("localhost", 9090))
