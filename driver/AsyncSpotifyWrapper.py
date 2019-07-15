from requests_futures.sessions import FuturesSession

class AsyncSpotifyWrapper:
    def __init__(self, token):
        self.token = token
        self.session = FuturesSession()

    def update_token(self, token):
        self.token = token

    def get_audio_analysis(self, track_id, callback):
        url = "https://api.spotify.com/v1/audio-analysis/" + track_id
        headers = {'Authorization' : "Bearer " + self.token}

        request = self.session.get(url, headers=headers)
        request.add_done_callback(callback)

    def get_current_playback(self, callback):
        url = "https://api.spotify.com/v1/me/player/currently-playing"

        request = self.session.get(url)
        request.add_done_callback(callback)
