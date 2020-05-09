import os

from src.db.row import Row, NullRow


def read(row_key, path):
    if not os.path.exists(path):
        return NullRow()
    with open(path, 'r') as f:
        current_best_row = NullRow()
        for line in f:
            row = Row.from_str(line)
            if row.is_equal_to_key(row_key):
                current_best_row = row
        return current_best_row
