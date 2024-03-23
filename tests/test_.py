import requests
import pytest

def test_get_users():
    url = "https://reqres.in/api/users"
    response = requests.get(url=url, params={"page":2})
    print(response.json())
    assert response.json()["page"] == 2
    assert response.status_code == 200
