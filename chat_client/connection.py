from multiprocessing.managers import SyncManager

class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages")
        super().__init__(address=address)
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)