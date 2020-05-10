import time
import os


class Manager:
    def __init__(self, path):
        self.path = path
        self.current_filename, self.current_filename_ts = self.get_most_recent_file()
        self.count = self.get_line_count()

    def get_all_files(self):
        for fn in os.listdir(self.path):
            yield fn

    def get_most_recent_file(self):
        most_recent, most_recent_ts = None, -1
        for fn in self.get_all_files():
            if float(fn) > most_recent_ts:
                most_recent, most_recent_ts = fn, float(fn)
        return most_recent, most_recent_ts

    def combine_files(self):
        pass

    def should_combine_files(self):
        return False

    def add_write(self):
        self.count += 1
        if self.should_combine_files():
            self.combine_files()

    @staticmethod
    def get_current_fn():
        return "{}".format(time.time())

    def get_line_count(self, fn=None):
        """
        should switch to: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
        :param segment:
        :param fn:
        :return:
        """
        if fn is None:
            fn = self.current_filename
        path = os.path.join(self.path, fn)
        c = 0
        with open(path, 'r') as f:
            for _ in f:
                c += 1
        return c
