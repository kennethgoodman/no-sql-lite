import json


class RowValue:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_str(value_str):
        return RowValue(json.loads(value_str))

    def to_file_format(self):
        return json.dumps(self.value)
