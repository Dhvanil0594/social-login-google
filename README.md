Here is the updated README.md file with the additional instructions:

# Social Login with Google
=====================================

This project provides a simple implementation of social login with Google using FastAPI.

## Requirements

* Python 3.7+
* FastAPI
* requests
* dotenv

## Installation

1. Clone the repository: `git clone https://github.com/your-username/your-repo-name.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Google Developer Console credentials:
	* `GOOGLE_CLIENT_ID`
	* `GOOGLE_CLIENT_SECRET`
	* `GOOGLE_REDIRECT_URI`

## Setup

1. Create a project in Google Cloud Console:
	* Go to the Google Cloud Console (https://console.cloud.google.com/) and create a new project if you haven’t already.
	* Enable the “Google+ API” in the “APIs & Services > Dashboard” section.

2. Create OAuth 2.0 Credentials:
	* In the Google Cloud Console, go to “APIs & Services > Credentials.”
	* Click on “Create Credentials” and select “OAuth client ID.”
	* If you have not created a consent screen then do it first then create credentials.
	* Choose “Web application” as the application type.
	* Add your FastAPI application’s URL (e.g., http://localhost:8000) to the “Authorized redirect URIs.”
	* Then publish the application.

## Usage

1. Run the application: `python google_login.py`
2. Open a web browser and navigate to `http://localhost:8001/login/google`
3. Click on the link to redirect to the Google login page
4. After authorization, Google will redirect back to `http://localhost:8001/auth/google` with an authorization code
5. The application will exchange the authorization code for an access token and retrieve user information from Google

## Endpoints

* `/login/google`: Redirects the user to the Google login page
* `/auth/google`: Handles the callback from Google after authorization and returns user information

## Environment Variables

* `GOOGLE_CLIENT_ID`: Your Google Client ID
* `GOOGLE_CLIENT_SECRET`: Your Google Client Secret
* `GOOGLE_REDIRECT_URI`: Your authorized redirect URI

Note: This is a basic implementation and you should consider adding additional security measures and error handling to your production application.