import json
import allure
from core.api_client import get
from core.endpoints import LOGOUT

@allure.title("Logout Test")
def test_logout(gateway_headers):
    with open("config/config.json") as c:
        config = json.load(c)

    response = get(
        config["gateway_base_url"] + LOGOUT,
        gateway_headers
    )

    assert response.status_code == 200
