import time
from .row_key import RowKey
from .row_value import RowValue


class Row:
    def __init__(self, key, value):
        self.ts = None
        self.key = RowKey(key)
        self.value = RowValue(value)

    @staticmethod
    def from_str(row_str):
        ts, key, value = row_str.split(",")
        key = RowKey.from_str(key)
        value = RowValue.from_str(value)
        row = Row(key, value)
        row.ts = ts
        return row

    def to_file_format(self):
        if self.ts is None:
            self.ts = time.time()
        return "{},{},{}".format(self.ts, self.key.to_file_format(), self.value.to_file_format())

    def is_equal_to_key(self, other_row_key):
        return self.key == other_row_key


class NullRow(Row):
    def __init__(self):
        super(NullRow, self).__init__(None, None)

    def __eq__(self, other):
        return isinstance(other, NullRow)
