# 3. На разные статус-коды 200/201/204/404/400
import json
import pytest
import requests
from requests import Response


def test_404_code():
    url = f'https://reqres.in/api/unknown/hvbhd'

    result: Response = requests.get(url)

    assert result.status_code == 404


def test_200_code():
    url = f'https://reqres.in/api/users/2'

    result: Response = requests.get(url)

    assert result.status_code == 200


def test_201_code():
    url = 'https://reqres.in/api/users'

    payload = json.dumps({
        "name": "morpheus",
        "job": "leader"
    })

    result: Response = requests.post(url, data=payload)
    assert result.status_code == 201


def test_204_code():
    url = 'https://reqres.in/api/users/2'

    result: Response = requests.delete(url)

    assert result.status_code == 204


def test_400_code():
    url = 'https://reqres.in/api/login'

    payload = json.dumps({
        "email": "any@mail.hh",
    })

    result: Response = requests.post(url, data=payload)
    assert result.status_code == 400
