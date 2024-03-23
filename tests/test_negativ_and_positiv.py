import requests
from .conftest import DOMAIN_URL

def test_pozitive_register():
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
    response = requests.post(url=DOMAIN_URL +"/register", json=payload)
    assert response.status_code == 200

def test_negative_register():
    payload = {
    "email": "sydney@fife"
}
    response = requests.post(url=DOMAIN_URL +"/register", json=payload)
    assert response.status_code == 400
