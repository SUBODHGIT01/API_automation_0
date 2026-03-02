import json
import allure
import random
from core.api_client import post
from core.endpoints import CREATE_TEMPLATE, DELETE_TEMPLATE

from core.api_client import delete

@allure.title("Create and Delete Template - Positive Flow")
def test_create_and_delete_template(gateway_headers):
    with open("config/config.json") as c:
        config = json.load(c)

    with open("payloads/create_template_payload.json") as p: 
        create_payload = json.load(p)

    random_number = random.randint(1000, 9999)

# Update template name dynamically
    create_payload["template_name"] = f"Custom test template {random_number}"
    print("Using template name:", create_payload["template_name"])

    # CREATE TEMPLATE
    create_resp = post(
        config["gateway_base_url"] + CREATE_TEMPLATE,
        gateway_headers,
        create_payload
    )

    assert create_resp.status_code == 201
    template_id = create_resp.json()["data"]["user_template_id"]

    # DELETE TEMPLATE
    delete_payload = {
        "user_template_id": template_id,
        "is_deleted": True
    }

    delete_resp = delete(
        config["gateway_base_url"] + DELETE_TEMPLATE,
        gateway_headers,
        delete_payload
    )

    assert delete_resp.status_code == 200
