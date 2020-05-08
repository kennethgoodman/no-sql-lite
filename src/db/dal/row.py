import time,json


class RowKey:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other_key):
        return self.key == other_key.key

    def to_file_format(self):
        return str(self.key)


class Row:
    def __init__(self, key, value):
        self.ts = None
        self.key = RowKey(key)
        self.value = value

    @staticmethod
    def from_str(row_str):
        ts, key, value = row_str.split(",")
        value = json.loads(value)
        row = Row(key, value)
        row.ts = ts
        return row

    def to_file_format(self):
        if self.ts is None:
            self.ts = time.time()
        return "{},{},{}".format(self.ts, self.key.to_file_format(), json.dumps(self.value))

    def is_equal_to_key(self, other_row_key):
        return self.key == other_row_key


class NullRow(Row):
    def __init__(self):
        super(NullRow, self).__init__(None, None)

    def __eq__(self, other):
        return isinstance(other, NullRow)
