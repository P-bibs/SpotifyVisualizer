"""Functions for requesting and refreshing authentication tokens for the Spotify API"""

import json, os
from requests_futures.sessions import FuturesSession

def request_token(id, secret, code, redirect):
    with FuturesSession() as session:
        print('requesting a token')

        request = session.post(
            "https://accounts.spotify.com/api/token",
            data={
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': redirect,
                'client_id': id,
                'client_secret': secret
            }
        )
        response = request.result()
        if response.status_code != 200:
            print("ERROR (when requesting initial access token)")
            print(response.status_code)
            print(response.reason)
            print(response.text)
        else:
            return json.loads(response.text)


def request_refresh(id, secret, refresh_token, blocking=False):
    print('requesting a refreshed token')
    with FuturesSession() as session:
        request = session.post(
            "https://accounts.spotify.com/api/token",
            data={
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
                'client_id': id,
                'client_secret': secret
            }
        )

        if blocking:
            return json.loads(request.result().text)
        else:
            return request

    # print(r.status_code)
    # print(r.reason)
    # print(r.text)
    # return json.loads(r.text)
