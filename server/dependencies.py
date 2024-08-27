import os
import requests
from fastapi import HTTPException

admin_client_id = os.getenv("ADMIN_CLIENT_ID")
admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")
keycloak_server_url = os.getenv("KEYCLOAK_SERVER_URL")

def get_admin_access_token():
    token_url = f"{keycloak_server_url}realms/master/protocol/openid-connect/token"
    data = {
        "client_id": admin_client_id,
        "username": admin_username,
        "password": admin_password,
        "grant_type": "password",
    }
    try:
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        return response.json()["access_token"]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error obtaining admin access token: {e}")