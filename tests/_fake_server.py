
class FakeServer:
    def __init__(self):
        self.last_command = None
        self.last_args = None
        self.messages = []

    def __call__(self, *args, **kwargs):
        # Make the SyncManager think that a new connection was created. 
        return self
    
    def send(self, data):
        # Track any command sent to the server.
        callid, command, args, kwargs = data
        self.last_command = command
        self.last_args = args


    def recv(self, *args, **kwargs):
        # For now we don't support any command, so just error. 
        return "ERROR", ValueError(f"{self.last_comand} - {self.last_args}")
    
    def close(self):
        pass

    