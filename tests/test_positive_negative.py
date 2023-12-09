import pytest
import requests
from requests import Response


@pytest.mark.parametrize('id_', [1, 27, 30000, 'd', '-5'])
def test_404_code(id_):
    url = f'https://reqres.in/api/unknown/{id_}'

    result: Response = requests.get(url)

    assert result.status_code == 404
