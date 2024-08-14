import unittest
import unittest.mock

from chat_client import ChatClient

from ._dummy_connection import _DummyConnection

class TestChatClient(unittest.TestCase):

    def test_send_message(self):
        client = ChatClient("User 1")
        #client.connection  = _DummyConnection()
        client.connection  = unittest.mock.Mock()

        sent_message = client.send_message("Hello World")

        assert sent_message == "User 1: Hello World"

if __name__ == '__main__':
	unittest.main()