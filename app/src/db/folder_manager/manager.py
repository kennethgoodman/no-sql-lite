import os
import time

from config import config


class Manager:
    def __init__(self):
        self.config = config

    def get_segment_dir(self, segment):
        return os.path.join(self.config.db.dir_location, segment)

    def db_dir_exists(self):
        return os.path.exists(self.config.db.dir_location)

    def get_segment_dirs(self):
        for segmentdir in os.listdir(self.config.db.dir_location):
            yield segmentdir

    def get_files(self, segment):
        for fn in os.path.join(self.config.db.dir_location, segment):
            yield fn

    def get_most_recent_file(self, segment):
        most_recent, most_recent_ts = None, -1
        for fn in self.get_files(segment):
            if float(fn) > most_recent_ts:
                most_recent, most_recent_ts = fn, float(fn)
        return most_recent, most_recent_ts

    def get_line_count(self, segment, fn):
        """
        should switch to: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
        :param segment:
        :param fn:
        :return:
        """
        path = os.path.join(self.get_segment_dir(segment), fn)
        c = 0
        with open(path, 'r') as f:
            for _ in f:
                c += 1
        return c

    @staticmethod
    def get_current_fn():
        return "{}".format(time.time())
