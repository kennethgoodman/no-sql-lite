import os
from collections import defaultdict

from src.db.dal import write, read
from src.db.row import Row, RowKey, RowValue
from src.db.folder_manager import Manager


class Client:
    def __init__(self):
        self.folder_manager = Manager()
        self.current_amount = defaultdict(int)
        self.current_file = {}
        self.initialize_current()

    def initialize_current(self):
        if not self.folder_manager.db_dir_exists():
            return
        for segmentdir in self.folder_manager.get_segment_dirs():
            self.current_file[segmentdir] = None
            most_recent, _ = self.folder_manager.get_most_recent_file(segmentdir)
            self.current_file[segmentdir] = most_recent
            self.current_amount[segmentdir] = self.folder_manager.get_line_count(segmentdir, most_recent)

    @staticmethod
    def key_to_segment(key):
        return key[0]

    def current_filepath(self, key):
        segment = self.key_to_segment(key)
        dirpath = self.folder_manager.get_segment_dir(segment)
        if segment not in self.current_file:
            self.current_file[segment] = self.folder_manager.get_current_fn()
        fn = self.current_file[segment]
        return os.path.join(dirpath, fn)

    def read_data(self, key):
        row = read(RowKey(key), self.current_filepath(key))
        return row.get_json_value()

    def combine_files(self, segment):
        pass

    def should_combine_files(self, segment):
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
        if self.should_combine_files(segment):
            self.combine_files(segment)
            self.current_amount[segment] = 0
        return resp


if __name__ == '__main__':
    c = Client()
    c.write_data("b", [123])
    print(c.read_data("b"))
