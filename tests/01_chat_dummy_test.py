import unittest
import unittest.mock

from chat_client import ChatClient

from ._dummy_connection import _DummyConnection

class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")

        assert client.nickname == "User 1"

if __name__ == '__main__':
	unittest.main()