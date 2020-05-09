import json


class RowValue:
    def __init__(self, value, raw_value=None):
        self.value = value
        self.raw_value = raw_value

    @staticmethod
    def from_str(value_str):
        return RowValue(None, value_str)

    def to_file_format(self):
        return json.dumps(self.value)

    def to_json(self):
        return self.get_value()

    def get_value(self):
        if self.value is None:
            self.value = json.loads(self.raw_value)
        return self.value
