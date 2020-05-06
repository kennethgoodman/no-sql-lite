import os
import json
from pathlib import Path
import ntpath


def write(key, data, path):
    dirpath, _ = os.path.split(path)
    Path(dirpath).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'w') as f:
            pass
    with open(path, 'a') as f:
        f.write("{},{}\n".format(key, json.dumps(data)))
