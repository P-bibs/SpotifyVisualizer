import time

from requests_futures.sessions import FuturesSession


class AsyncSpotifyWrapper:
    """Contains functions for querying audio analysis and current playback endpoints.

    Returns future objects."""

    def __init__(self, token):
        """Create instance with given auth token.

        Update token with update_token function."""
        self.token = token
        self.session = FuturesSession(max_workers=5)

    def update_token(self, token):
        """Update authentication token."""
        self.token = token

    def get_audio_analysis(self, track_id):
        """Return a future that resolves to an audio analysis object for given track."""
        url = "https://api.spotify.com/v1/audio-analysis/" + track_id
        headers = {'Authorization': "Bearer " + self.token}

        request = self.session.get(url, headers=headers)
        return request

    def get_current_playback(self):
        """Return a future that resolves to a current playback object for current user."""
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
