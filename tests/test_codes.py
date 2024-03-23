import requests
from .conftest import USER_URL, DOMAIN_URL


def test_get_user_success():
    response = requests.get(USER_URL + "/2")

    assert response.status_code == 200


def test_create_user_success():
    name = 'abc'
    job = 'fdr'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(url=USER_URL, json=payload)
    assert response.status_code == 201


def test_delete_user_success():
    response = requests.delete(url=USER_URL + '/2')

    assert response.status_code == 204


def test_invalid_request():
    response = requests.get(USER_URL + "/23")

    assert response.status_code == 404


def test_bad_request():
    payload = {
    "email": "sydney@fife"
}
    response = requests.post(url=DOMAIN_URL + '/login', json=payload)

    assert response.status_code == 400