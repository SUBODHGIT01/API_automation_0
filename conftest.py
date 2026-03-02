import json
import pytest
from core.auth_manager import AuthManager

@pytest.fixture(scope="function")
def access_token():
    with open("config/config.json") as f:
        config = json.load(f)

    token = AuthManager.login(
        config["login_base_url"],
        config["authorization"]
    )
    return token

@pytest.fixture(scope="function")
def gateway_headers(access_token):
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
