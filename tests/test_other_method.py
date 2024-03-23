import resource

import requests
from .conftest import USER_URL


def test_get_users():
    response = requests.get(url=USER_URL, params={"page":2})

    assert response.json()["page"] == 2
    assert response.status_code == 200

def test_create_user():
    name = 'abc'
    job = 'fdr'
    payload = {
        "name": name,
        "job": job
    }
    response = requests.post(url=USER_URL, json=payload)
    assert response.status_code == 201
    assert response.json()['name'] == name

def test_update_users():
    payload = {
        "name": "morpheus",
        "job": "zion resident",
        "updatedAt": "2024-03-23T19:36:51.375Z"
    }
    response = requests.put(url=USER_URL + "/2", json=payload)
    assert  response.status_code == 200
    assert response.json()["job"] == "zion resident"

def test_delete_users():
    response = requests.delete(url=USER_URL + "/2")
    assert response.status_code == 204
