import unittest 
from unittest.mock import patch, MagicMock

from chat_client import Connection, ChatClient 

class TestChatClient(unittest.TestCase):
    
    @patch.object(ChatClient, "_get_connection")
    def test_client_connection(self, _get_connection):
        connection_spy = MagicMock()
        _get_connection.return_value = connection_spy

        client = ChatClient("User 1")
        client.send_message("Hello World")
        
        # assert that the spy was called with the expected data to broadcast
        connection_spy.broadcast.assert_called_with("User 1: Hello World")

    if __name__ == '__main__':
        unittest.main()