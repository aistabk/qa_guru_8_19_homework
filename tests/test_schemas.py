# 4. На разные схемы (4-5 схем

import os

import jsonschema
import requests
from requests import Response

from tests.utils import load_schema


def test_single_schema():
    url = "https://reqres.in/api/unknown/2"
    schema = load_schema(os.path.abspath("schemas/single_schema.json"))

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_list_schema():
    url = "https://reqres.in/api/unknown"
    schema = load_schema(os.path.abspath("schemas/list_schema.json"))

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
