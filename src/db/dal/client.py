from config import config
from src.db.dal.write import write
from src.db.dal.read import read


class Client:
    def __init__(self):
        self.config = config

    def read_data(self, key):
        return read(key, self.config.db.file_location)

    def write_data(self, key, data):
        return write(key, data, self.config.db.file_location)


if __name__ == '__main__':
    c = Client()
