# 1. на каждый из методов GET/POST/PUT/DELETE ручек reqres.in
import json
import os
from datetime import datetime

import jsonschema
import requests
from requests import Response

from tests.utils import load_schema


def test_get_method():
    url = "https://reqres.in/api/users?delay=3"
    schema = load_schema(os.path.abspath("schemas/delayed_response_schema.json"))

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_post_method():
    url = "https://reqres.in/api/register"

    payload = {"email": "sydney@fife"}

    response = requests.post(url, json=payload)

    assert "Missing password" in response.text


def test_put_method():
    url = "https://reqres.in/api/users/2"
    payload = json.dumps({
        "name": "morpheus",
        "job": "zion resident"
    })

    response = requests.put(url, data=payload)

    request_time_utc = datetime.utcnow().replace(microsecond=0).isoformat()
    assert response.json()["updatedAt"][:-5] == request_time_utc


def test_delete_method():

    url = "https://reqres.in/api/users/2"

    result: Response = requests.delete(url)

    assert result.status_code == 204




