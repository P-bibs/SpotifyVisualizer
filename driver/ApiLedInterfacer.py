import os
import time
import auth
import AsyncSpotifyWrapper

class ApiLedInterfacer():
    def __init__(self, ping_interval=15):
        self.ping_interval = ping_interval
        self.ping_timer = 0
        self.beat_counter = 0
        self.progress = 0
        self.intervals = []

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/../data/authCode.txt') as f:
            code = f.readlines()
        with open(dir_path + '/../data/secret.txt') as f:
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
        self.spotify.get_current_playback(self.sync_playback)

    def sync_playback(self, currently_playing):
        # delay_time = (time_after_request - time_before_request) / 2
        self.progress = (currently_playing['progress_ms']/1000)  # + delay_time

        # Only fetch analysis if the track has changed
        if currently_playing['item']['id'] != self.track:
            self.track = currently_playing['item']['id']
            self.fetch_intervals()

        print('\n=================')
        print('Playback Synced')
        # print('delay time %s' % delay_time)
        print('Current progress: ' + str(self.progress))
        print('Current Track: ' + self.track)
        print('=================\n')

    def fetch_intervals(self):
        self.spotify.get_audio_analysis(self.track, self.trim_intervals)

    def trim_intervals(self, response):
        self.intervals = list(map((lambda x: x['start']), response['beats']))
        print(self.intervals)
        print(self.progress)

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
            print('fetch initiated')
            self.fetch_playback()
            self.ping_timer = 0

        if self.ttl < 60:
            self.refresh_credentials()

        if len(self.intervals) > 0 and self.progress > self.intervals[0]:
            self.beat_counter += 1
            print("beat " + str(self.beat_counter % 4) + " at " + str(time.time()))
            self.intervals.pop(0)


    def exit(self):
        pass
        # self.refresh_timer.stop()
