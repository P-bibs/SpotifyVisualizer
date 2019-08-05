import time
from requests_futures.sessions import FuturesSession

class AsyncSpotifyWrapper:
    def __init__(self, token):
        self.token = token
        self.session = FuturesSession()

    def update_token(self, token):
        self.token = token

    def get_audio_analysis(self, track_id):
        url = "https://api.spotify.com/v1/audio-analysis/" + track_id
        headers = {'Authorization': "Bearer " + self.token}

        request = self.session.get(url, headers=headers)
        return request

    def get_current_playback(self):
        now = time.time()
        def response_hook(response,**kwargs):
            print('first hook called at ' + str(time.time()))
            response.init_time = now
            response.sanity_check = "yep"
            print("init time: " + str(response.init_time))

        url = "https://api.spotify.com/v1/me/player/currently-playing"
        headers = {'Authorization': "Bearer " + self.token}

        print('request made at ' + str(time.time()))
        request = self.session.get(url, headers=headers, hooks={'response': response_hook})
        
        return request
