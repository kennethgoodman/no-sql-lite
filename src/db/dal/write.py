import os
from pathlib import Path


def write(row, path):
    dirpath, _ = os.path.split(path)
    Path(dirpath).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'w') as f:
            pass
    with open(path, 'a') as f:
        f.write("{}\n".format(row.to_file_format()))
