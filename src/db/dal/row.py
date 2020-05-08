import time,json


class Row:
    def __init__(self, key, value):
        self.ts = None
        self.key = key
        self.value = value

    @staticmethod
    def parsestr(rowstr):
        ts, key, value = rowstr.split(",")
        value = json.loads(value)
        row = Row(key, value)
        row.ts = ts
        return row

    def to_file_format(self):
        if self.ts is None:
            self.ts = time.time()
        return "{},{},{}".format(self.ts, self.key, json.dumps(self.value))
