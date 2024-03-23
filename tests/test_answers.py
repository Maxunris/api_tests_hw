import requests
from .conftest import DOMAIN_URL, USER_URL


def test_without_answer():
    response = requests.get(url= USER_URL + '/23')

    assert response.json() == {}
    assert response.status_code == 404


def test_with_answer():
    response = requests.get(url=DOMAIN_URL + '/unknown/2')

    assert response.json()["data"]["id"] == 2
    assert response.status_code == 200