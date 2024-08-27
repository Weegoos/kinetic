from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from dependencies import get_admin_access_token
import requests
import jwt
import os

auth_router = APIRouter()

server_base_url = os.getenv('SERVER_BASE_URL')
front_base_url = os.getenv('CLIENT_BASE_URL')

keycloak_server_url = os.getenv("KEYCLOAK_SERVER_URL")
realm_name = os.getenv("REALM_NAME")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET_KEY")

keycloak_auth_url = f"{keycloak_server_url}realms/{realm_name}/protocol/openid-connect/auth"
keycloak_token_url = f"{keycloak_server_url}realms/{realm_name}/protocol/openid-connect/token"
keycloak_logout_url = f"{keycloak_server_url}realms/{realm_name}/protocol/openid-connect/logout"
keycloak_users_url = f"{keycloak_server_url}admin/realms/{realm_name}/users"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=keycloak_token_url)

def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        return decoded_token
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=400, detail=f"Error decoding token: {str(e)}")

@auth_router.get("/login")
async def login():
    redirect_uri = f"{server_base_url}/auth/callback"
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": "openid"
    }
    try:
        auth_url = requests.Request('GET', keycloak_auth_url, params=params).prepare().url
        if auth_url:
            return RedirectResponse(url=auth_url)
        else:
            raise HTTPException(status_code=500, detail="Failed to generate authentication URL")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting authentication URL: {str(e)}")

@auth_router.get("/logout")
async def logout(request: Request):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="No refresh token found")

    try:
        response_kc = requests.post(
            keycloak_logout_url,
            data={
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
            }
        )
        if response_kc.status_code != 204:
            raise HTTPException(status_code=response.status_code, detail="Failed to end session")
        
        response = RedirectResponse(url=f"{server_base_url}/auth/login")
        response.delete_cookie(key="access_token", path='/')
        response.delete_cookie(key="refresh_token", path='/')
        return response
        

    except HTTPException as e:
        raise e

    except Exception as e:
        print(f"Error ending session: {e}")
        raise HTTPException(status_code=500, detail="Error ending session")

@auth_router.get("/callback")
async def callback(request: Request):
    code = request.query_params.get('code')
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")

    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': f"{server_base_url}/auth/callback",
        'client_id': client_id,
        'client_secret': client_secret,
    }
    try:
        response = requests.post(keycloak_token_url, data=token_data)

        token = response.json()
        access_token = token.get('access_token')
        refresh_token = token.get('refresh_token')

        if not access_token or not refresh_token:
            raise HTTPException(status_code=400, detail="Access token or refresh token not found in response")

        response = RedirectResponse(url=front_base_url)
        response.set_cookie(key="access_token", value=access_token, path='/')
        response.set_cookie(key="refresh_token", value=refresh_token, path='/')
        return response
    except requests.RequestException as e:
        print(f"Error exchanging code for token: {e}")
        raise HTTPException(status_code=500, detail="Error exchanging code for token")


@auth_router.get("/user")
async def get_user_info(request: Request):
    access_token = request.cookies.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401, detail="No access token found")

    try:
        userinfo = decode_token(access_token)
        return userinfo
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid credentials: {str(e)}")

# Route to get user info by login
@auth_router.get("/user/{username}")
def get_user_info_by_login(username: str, access_token: str = Depends(get_admin_access_token)):
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