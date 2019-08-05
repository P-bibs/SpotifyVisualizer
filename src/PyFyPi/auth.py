import json
import os
from requests_futures.sessions import FuturesSession

def request_token(code, secret):
    with FuturesSession() as session:
        print('requesting a token')
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open(dir_path + '/../../data/redirect.txt') as f:
            redirect_uri = f.readlines()[0].strip('\n')

        request = session.post(
            "https://accounts.spotify.com/api/token",
            data={
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': redirect_uri,
                'client_id': '31f47db1c9b043b78f5ca5fbc53ac1d5',
                'client_secret': secret
            }
        )
        response = request.result()
        print(response.status_code)
        print(response.reason)
        print(response.text)
        return json.loads(response.text)


def request_refresh(refresh_token, secret, callback):
    print('requesting a token')
    session = FuturesSession()

    def response_hook(response):
        response.new_token = json.loads(response.text)['access_token']

    request = session.post(
        "https://accounts.spotify.com/api/token",
        data={
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': '31f47db1c9b043b78f5ca5fbc53ac1d5',
            'client_secret': secret
        },
        hooks={'response': response_hook},
    )

    request.add_done_callback(callback)

    # print(r.status_code)
    # print(r.reason)
    # print(r.text)
    # return json.loads(r.text)
