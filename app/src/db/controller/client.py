from src.db.dal import write, read
from src.db.row import Row, RowKey, RowValue
from src.db.folder_manager import Manager


class Client:
    def __init__(self):
        self.folder_manager = Manager()

    def current_filepath(self, key):
        return self.folder_manager.current_filepath(key)

    def read_data(self, key):
        row = read(RowKey(key), self.current_filepath(key))
        return row.get_json_value()

    def write_data(self, key, data):
        rowkey = RowKey.from_str(key)
        value = RowValue(data)
        row = Row(rowkey, value)
        try:
            resp = write(row, self.current_filepath(key))
        except Exception as e:
            # TODO(kgoodman) log this
            raise e
        self.folder_manager.add_write(key)
        return resp


if __name__ == '__main__':
    c = Client()
    c.write_data("c", {"a":1})
    print(c.read_data("b"))
