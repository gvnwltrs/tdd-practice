import unittest
from unittest.mock import patch, MagicMock

from chat_client import Connection

class TestConnection(unittest.TestCase):
    @patch.object(Connection, "connect", return_value=None)
    def test_broadcast(self, mock_connect):
        c = Connection(("127.0.0.1", 9090))

        with patch.object(c, "get_messages", return_value=[]):
            c.broadcast("Hello World")

            assert c.get_messages()[-1] == "Hello World"

if __name__ == '__main__':
	unittest.main()