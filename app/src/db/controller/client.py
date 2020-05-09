import os
from time import time
from collections import defaultdict

from config import config
from src.db.dal import write, read
from src.db.row import Row, RowKey, RowValue


class Client:
    def __init__(self):
        self.config = config
        self.current_amount = defaultdict(int)
        self.initialize_current_amount()
        self.current_file = {}
        self.initialize_current_file_map()

    def initialize_current_amount(self):
        pass

    def initialize_current_file_map(self):
        pass

    @staticmethod
    def get_current_file():
        return "{}.csv".format(time())

    @staticmethod
    def key_to_segment(key):
        return key[0]

    def current_filepath(self, key):
        segment = self.key_to_segment(key)
        dirpath = os.path.join(self.config.db.dir_location, segment)
        if segment not in self.current_file:
            self.current_file[segment] = self.get_current_file()
        fn = self.current_file[segment]
        return os.path.join(dirpath, fn)

    def read_data(self, key):
        row = read(RowKey(key), self.current_filepath(key))
        return row.value.to_json()

    def combine_files(self):
        pass

    def should_combine_files(self):
        return False

    def write_data(self, key, data):
        rowkey = RowKey.from_str(key)
        value = RowValue(data)
        row = Row(rowkey, value)
        try:
            resp = write(row, self.current_filepath(key))
        except Exception as e:
            # TODO(kgoodman) log this
            raise e
        segment = self.key_to_segment(key)
        self.current_amount[segment] += 1
        if self.should_combine_files():
            self.combine_files()
            self.current_amount[segment] = 0
        return resp


if __name__ == '__main__':
    c = Client()
    c.write_data("b", [123])
    print(c.read_data("b"))
