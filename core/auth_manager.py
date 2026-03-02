import json
from core.api_client import post
from core.endpoints import LOGIN

class AuthManager:
    _access_token = None

    @staticmethod
    def login(base_url, auth_header):
        with open("payloads/login_payload.json") as f:
            payload = json.load(f)

        headers = {
            "Content-Type": "application/json",
            "Authorization": auth_header
        }

        response = post(base_url + LOGIN, headers, payload)
        assert response.status_code == 200

        AuthManager._access_token = response.json()["data"]["accessToken"]
        return AuthManager._access_token

    @staticmethod
    def get_access_token():
        return AuthManager._access_token
    

    
