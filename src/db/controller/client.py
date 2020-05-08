import os
from time import time

from config import config
from src.db.dal import write, read
from src.db.row import Row, RowKey, RowValue


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
        row = read(RowKey(key), self.current_filepath)
        return row.value.to_json()

    def combine_files(self):
        pass

    def should_combine_files(self):
        return False

    def write_data(self, key, data):
        key = RowKey.from_str(key)
        value = RowValue(data)
        row = Row(key, value)
        try:
            resp = write(row, self.current_filepath)
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
    c.write_data("b", [123])
    print(c.read_data("b"))
