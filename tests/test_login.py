import json
import pytest
import allure
from core.api_client import post
from core.endpoints import LOGIN

@allure.title("Positive Login Test")
@pytest.mark.sanity
# @pytest.mark.regression
def test_login_success():
    with open("config/config.json") as c:
        config = json.load(c)

    with open("payloads/login_payload.json") as p:
        payload = json.load(p)

    headers = {
        "Content-Type": "application/json",
        "Authorization": config["authorization"]
    }

    response = post(config["login_base_url"] + LOGIN, headers, payload)

    assert response.status_code == 200
    assert "accessToken" in response.json()["data"]

@allure.title("Negative Login Test - Invalid Password")
@pytest.mark.sanity
def test_login_invalid_password():
    with open("config/config.json") as c:
        config = json.load(c)

    payload = {
        "username": "subodh_m",
        "password": "wrongpass",
        "forceLogin": True
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": config["authorization"]
    }

    response = post(config["login_base_url"] + LOGIN, headers, payload)
    assert response.status_code != 200
