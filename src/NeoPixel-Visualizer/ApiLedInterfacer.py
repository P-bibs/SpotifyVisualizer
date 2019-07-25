import os
import time
import json
import auth
import AsyncSpotifyWrapper

class ApiLedInterfacer():
    def __init__(self, ping_interval=5):
        self.ping_interval = ping_interval
        self.ping_timer = 0
        self.beat_counter = 0
        self.progress = 0
        self.intervals = []
        self.playback_request = None
        self.analysis_request = None

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/../../data/authCode.txt') as f:
            code = f.readlines()
        with open(dir_path + '/../../data/secret.txt') as f:
            self.secret = f.readlines()

        response = auth.request_token(code, self.secret)
        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']
        self.ttl = response['expires_in']
        self.spotify = AsyncSpotifyWrapper.AsyncSpotifyWrapper(self.access_token)

        self.track = ""
        self.fetch_playback()


    def refresh_credentials(self):
        auth.request_refresh(
            self.refresh_token,
            self.secret,
            (lambda response: self.spotify.update_token(response.new_token))
        )

    def fetch_playback(self):
        self.playback_request = self.spotify.get_current_playback()

    def sync_playback(self, response):
        print('Sync Playback called at ' + str(time.time()))

        currently_playing = json.loads(response.result().text)
        rtt = time.time() - response.result().init_time

        self.progress = (currently_playing['progress_ms']/1000)  + rtt / 2

        # Only fetch analysis if the track has changed
        if currently_playing['item']['id'] != self.track:
            self.track = currently_playing['item']['id']
            self.fetch_intervals()

        print('\n=================')
        print('Playback Synced')
        print('RTT is %s' % rtt)
        print('Current progress: ' + str(self.progress))
        print('Current Track: ' + self.track)
        print('=================\n')

    def fetch_intervals(self):
        self.analysis_request = self.spotify.get_audio_analysis(self.track)

    def trim_intervals(self, response):
        analysis = json.loads(response.result().text)
        self.intervals = list(map((lambda x: x['start']), analysis['beats']))

        # trim intervals to current location in time
        while self.progress > self.intervals[0]:
            # print(len(self.intervals))
            self.intervals.pop(0)

        print('\n=================')
        print('Intervals Fetched')
        print('Intervals Left: ' + str(len(self.intervals)))
        print('=================\n')

    def update(self, dt):
        self.ttl -= dt
        self.progress += dt
        self.ping_timer += dt

        if self.ping_timer > self.ping_interval:
            self.fetch_playback()
            self.ping_timer = 0

        if self.playback_request and self.playback_request.done():
            self.sync_playback(self.playback_request)
            self.playback_request = None

        if self.ttl < 60:
            self.refresh_credentials()

        if self.analysis_request and self.analysis_request.done():
            self.trim_intervals(self.analysis_request)
            self.analysis_request = None

        if len(self.intervals) > 0 and self.progress > self.intervals[0]:
            self.beat_counter += 1
            print("beat " + str(self.beat_counter % 4) + " at " + str(time.time()))
            self.intervals.pop(0)


    def exit(self):
        pass
