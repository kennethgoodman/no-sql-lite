class RowKey:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other_key):
        return self.key == other_key.key

    @staticmethod
    def from_str(key):
        return RowKey(key)

    def to_file_format(self):
        return str(self.key)
