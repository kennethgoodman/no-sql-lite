import os

from .row import Row


def read(key, path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        current_best_row = None
        for line in f:
            row = Row.parsestr(line)
            if row.key == key:
                current_best_row = row
        return current_best_row
