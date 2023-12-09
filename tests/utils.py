import json

import jsonschema
import os
import sys

# добавьте путь к директории, где находится utils.py
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def load_schema(filepath):
    with open(filepath) as file:
        schema = json.load(file)
        return schema
