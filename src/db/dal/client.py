import os
from time import time

from config import config
from src.db.dal.write import write
from src.db.dal.read import read


class Client:
    def __init__(self):
        self.config = config
        self.current_amount = 0
        self.current_file = None
        self.set_current_file()

    @property
    def current_filepath(self):
        return os.path.join(self.config.db.dir_location, self.current_file)

    def set_current_file(self):
        self.current_file = "{}.csv".format(time())

    def read_data(self, key):
        return read(key, self.current_filepath)

    def combine_files(self):
        pass

    def should_combine_files(self):
        return False

    def write_data(self, key, data):
        try:
            resp = write(key, data, self.current_filepath)
        except Exception as e:
            # TODO(kgoodman) log this
            raise e
        self.current_amount += 1
        if self.should_combine_files():
            self.combine_files()
            self.current_amount = 0
            self.set_current_file()
        return resp


if __name__ == '__main__':
    c = Client()
