import requests
import json

def request_token(code, secret):
    print('requesting a token')
    r = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://localhost:3000/authenticated',
            'client_id': '31f47db1c9b043b78f5ca5fbc53ac1d5',
            'client_secret' : secret
        }
    )
    print(r.status_code)
    print(r.reason)
    print(r.text)
    return json.loads(r.text)

def request_refresh(refresh_token, secret):
    print('requesting a token')
    r = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            'grant_type': 'refresh_token',
            'refresh_token' : refresh_token,
            'client_id': '31f47db1c9b043b78f5ca5fbc53ac1d5',
            'client_secret' : secret
        }
    )
    print(r.status_code)
    print(r.reason)
    print(r.text)
    return json.loads(r.text)