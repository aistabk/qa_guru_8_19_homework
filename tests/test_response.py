# 5. С ответом и без ответа
import requests
from requests import Response


def test_with_empty_response():
    url = "https://reqres.in/api/users/2"

    result: Response = requests.delete(url)

    assert result.text == ''


def test_with_response():
    url = "https://reqres.in/api/login"
    payload = {"email": "peter@klaven"}

    response = requests.post(url, json=payload)

    assert "Missing password" in response.text
