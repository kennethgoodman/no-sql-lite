import os
import json


def read(key, path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        current_value = None
        for line in f:
            if line.split(",")[0] == key:
                current_value = json.loads(",".join(line.split(",")[1:]))
        return current_value
