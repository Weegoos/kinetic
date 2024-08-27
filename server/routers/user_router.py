from fastapi import APIRouter, HTTPException, Request, Response, Depends
import os
import requests
from dependencies import get_admin_access_token

user_router = APIRouter()

keycloak_server_url = os.getenv("KEYCLOAK_SERVER_URL")
realm_name = os.getenv("REALM_NAME")

@user_router.get("/user/{username}")
async def get_user_info_by_login(username: str, access_token: str = Depends(get_admin_access_token)):
    """Getting user information by Keycloak Login"""
    url = f"{keycloak_server_url}/admin/realms/{realm_name}/users"
    params = {
        "username": username,
        "exact": "true",
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        users = response.json()
        if not users:
            raise HTTPException(status_code=404, detail="User not found")
        return users[0]
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user info: {e}")
    
@user_router.get("/users")
async def get_all_users(access_token: str = Depends(get_admin_access_token)):
    """Getting all user's informations on Keycloak"""
    url = f"{keycloak_server_url}/admin/realms/{realm_name}/users"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        users = response.json()
        if not users:
            raise HTTPException(status_code=404, detail="There is no users")
        return users
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user info: {e}")