import os

from src.db.row import Row, NullRow


def read(row_key, path):
    """
    Should we switch to: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
    If we ensure line sizes are all the same size, can we avoid reading the value?
    """
    if not os.path.exists(path):
        return NullRow()
    with open(path, 'r') as f:
        current_best_row = NullRow()
        for line in f:
            row = Row.from_str(line)
            if row.is_equal_to_key(row_key):
                current_best_row = row
        return current_best_row
