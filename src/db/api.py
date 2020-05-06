from .dal import Client


class API:
    def __init__(self):
        self.client = Client()

    def read_data(self, key):
        data = self.client.read_data(key)
        if data is not None:
            return data
        return {}

    def write_data(self, key, data):
        return self.client.write_data(key, data)
