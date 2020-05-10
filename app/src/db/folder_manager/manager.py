import os

from config import config
from src.db.segment_manager import Manager as SegmentManager


class Manager:
    def __init__(self):
        self.config = config
        self.segment_managers = {}
        self.initialize_segment_managers()

    def initialize_segment_managers(self):
        if not self.db_dir_exists():
            return
        for segmentdir in self.get_segment_dirs():
            self.add_segment_manager(segmentdir)

    def add_segment_manager(self, segment):
        segmentdirpath = self.get_segment_dir(segment)
        self.segment_managers[segment] = SegmentManager(segmentdirpath)

    def get_segment_dir(self, segment):
        return os.path.join(self.config.db.dir_location, segment)

    def db_dir_exists(self):
        return os.path.exists(self.config.db.dir_location)

    def get_segment_dirs(self):
        for segmentdir in os.listdir(self.config.db.dir_location):
            yield segmentdir

    def get_line_count(self, segment):
        return self.segment_managers[segment].get_line_count()

    def current_filepath(self, key):
        segment = self.key_to_segment(key)
        if segment not in self.segment_managers:
            self.add_segment_manager(segment)
        return self.segment_managers[segment].current_filename

    def add_write(self, key):
        segment = self.key_to_segment(key)
        if segment not in self.segment_managers:
            self.add_segment_manager(segment)
        self.segment_managers[segment].add_write()

    @staticmethod
    def key_to_segment(key):
        return key[0]
