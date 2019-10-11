import os, time, json
import board, neopixel
import auth, AsyncSpotifyWrapper, BeatLine

BEAT_COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (255, 100, 0)
]

class ApiLedInterfacer():
    def __init__(self, g_state_machine, ping_interval=15):
        self.g_state_machine = g_state_machine

        self.ping_interval = ping_interval
        self.ping_timer = 0
        self.beat_counter = 0
        self.progress = 0
        self.intervals = []
        self.playback_request = None
        self.analysis_request = None
        self.refresh_request = None
        self.beat_line = BeatLine.BeatLine(70, [50, 50, 50])

        # Load config file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/../../config.json') as f:
            config = json.load(f)

        # If a refresh token doesn't exist, request one
        if config['DATA']['refresh_token'] == '':
            response = auth.request_token(
                config['SETUP']['id'],
                config['SETUP']['secret'],
                config['DATA']['code'],
                config['SETUP']['redirect']
            )

            refresh_token = response['refresh_token']
            with open(dir_path + '/../../config.json', 'w') as f:
                config['DATA'] = {**config['DATA'], "refresh_token": refresh_token}
                json.dump(config, f, ensure_ascii=False, indent=4)

        # Use refresh token to get access token
        self.id = config['SETUP']['id']
        self.secret = config['SETUP']['secret']
        self.refresh_token = config['DATA']['refresh_token']
        response = auth.request_refresh(self.id, self.secret, self.refresh_token, True)

        print("response text:")
        print(response)
        access_token = response['access_token']
        self.ttl = response['expires_in']
        self.spotify = AsyncSpotifyWrapper.AsyncSpotifyWrapper(access_token)

        self.track = ""
        self.fetch_playback()


    def fetch_refresh(self):
        self.refresh_request = auth.request_refresh(
            self.id,
            self.secret,
            self.refresh_token
        )

    def set_refresh(self, response):
        access_token = json.loads(response.result().text)['access_token']
        self.spotify.update_token(access_token)
    
    def fetch_playback(self):
        self.playback_request = self.spotify.get_current_playback()

    def sync_playback(self, response):
        """Return 1 if playing, 0 otherwise"""
        print('Sync Playback called at ' + str(time.time()))

        currently_playing = json.loads(response.result().text)
        rtt = time.time() - response.result().init_time
        
        if currently_playing['is_playing'] == False:
            print("is_playing is False, changing state")
            self.g_state_machine.change_state('IdleState')
            return 0

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

        return 1

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

    def beat(self):
        self.beat_line.create_beat(2, 30, BEAT_COLORS[self.beat_counter % 3])

        self.beat_counter += 1
        print("beat " + str(self.beat_counter % 4) + " at " + str(time.time()))
        self.intervals.pop(0)

    def update(self, dt):
        self.ttl -= dt
        self.progress += dt
        self.ping_timer += dt
        self.beat_line.update(dt)

        if self.refresh_request and self.refresh_request.done():
            self.set_refresh(self.refresh_request)
            self.refresh_request = None

        if self.ping_timer > self.ping_interval:
            self.fetch_playback()
            self.ping_timer = 0

        if self.playback_request and self.playback_request.done():
            is_playing = self.sync_playback(self.playback_request)
            if not is_playing: return
            self.playback_request = None

        if self.ttl < 60:
            self.fetch_refresh()

        if self.analysis_request and self.analysis_request.done():
            self.trim_intervals(self.analysis_request)
            self.analysis_request = None

        if len(self.intervals) > 0 and self.progress > self.intervals[0]:
            self.beat()

        self.beat_line.render()


    def exit(self):
        print("Releasing neopixel")
        self.beat_line.exit()
