from fastapi import FastAPI, Depends
import requests
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.environ.get("GOOGLE_REDIRECT_URI")

@app.get("/login/google")
async def login_google():
    """
    Redirect the user to the Google login page.

    This endpoint returns a JSON object with a single key, "url", which is the URL
    that the user should be redirected to in order to log in with Google.
    """
    return {
        "url": f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
    }

@app.get("/auth/google")
async def auth_google(code: str):
    """
    Handle the callback from Google after the user has authorized your app.

    This endpoint expects a single query parameter, "code", which is the authorization code
    returned by Google.

    The endpoint will return a JSON object with information about the user.
    """
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    return user_info.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("google_login:app", host="0.0.0.0", port=8001, reload=True)