import requests
import jwt

BASE_URL = "http://localhost:8000/api"

def get_tokens(username, password):
    url = f"{BASE_URL}/token/"

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)
    json_response = response.json()

    access_token = json_response.get("access")
    refresh_token = json_response.get("refresh")

    return access_token, refresh_token


def decode_token(access_token):
    decoded_token = jwt.decode(access_token, algorithms=["HS256"], options={"verify_signature": False})
    user_id = decoded_token.get("user_id")
    print("User ID:", user_id)
    return user_id

def create_task(access_token, user_id):
    url = f"{BASE_URL}/v1/create/"
    data = {
        "title": "My Task",
        "description": "This is my task",
        "completed": False,
        "user": user_id
    }
    response = requests.post(url, data=data, headers={"Authorization": f"Bearer {access_token}"})
    print(response.json())

if __name__ == "__main__":
    access_token, refresh_token = get_tokens("admin", "admin")
    user_id = decode_token(access_token)
    create_task(access_token, user_id)