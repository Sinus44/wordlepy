import json
import os


def read(file_path, default=None):
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return default

    with open(file_path, "r") as file:
        return json.loads(file.read())


def write(file_path, data):
    with open(file_path, "w") as file:
        file.write(json.dumps(data))
