import unittest
from unittest.mock import patch, MagicMock

from chat_client import Connection, ChatClient
from ._fake_server import FakeServer

class TestConnection(unittest.TestCase):
    @patch.object(Connection, "connect", return_value=None)
    @patch.object(Connection, "broadcast", return_value=None)
    @patch.object(Connection, "get_messages", return_value=["Hello World"])
    def test_broadcast(self, mock_get_messages, mock_broadcast, mock_connect):
        c = Connection(("127.0.0.1", 9090))

        c.broadcast("Hello World")

        assert c.get_messages()[-1] == "Hello World" 

    @patch("multiprocessing.managers.listener_client", new={"pickle": (None, FakeServer())})
    def test_exchange_with_server():
        c1 = Connection(("localhost", 9090))  
        c2 = Connection(("localhost", 9090))  

        c1.broadcast("connected message")

        assert c2.get_messages()[-1] == "connected message"


    if __name__ == '__main__':
        unittest.main()