from .dal import Client


class API:
    def __init__(self):
        self.client = Client()

    def read_data(self, key):
        return self.client.read_data(key)

    def write_data(self, key, data):
        return self.client.write_data(key, data)
