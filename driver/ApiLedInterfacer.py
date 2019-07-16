import os
import threading
import time
import spotipy
import auth

class ApiLedInterfacer():
    def __init__(self, ping_interval = 15):
        self.ping_interval = ping_interval
        self.ping_timer = 0
        self.beat_counter = 0

        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/../data/authCode.txt') as f:
            code = f.readlines()
        with open(dir_path + '/../data/secret.txt') as f:
            secret = f.readlines()

        response = auth.request_token(code, secret)
        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']
        self.ttl = response['expires_in']
        self.sp = spotipy.Spotify(auth=self.access_token)

        self.track = ""
        self.sync_playback()




    def refresh_credentials(self):
        response = auth.request_token(code, secret)
        self.access_token = response['access_token']
        self.sp = spotipy.Spotify(auth=access_token)

    def sync_playback(self):
        time_before_request = time.time()
        now_playing = self.sp.currently_playing()
        time_after_request = time.time()

        #delay_time = time.time() - now_playing['timestamp']/1000
        delay_time = (time_after_request - time_before_request) / 2
        self.progress = (now_playing['progress_ms']/1000) + delay_time
        
        #Only fetch analysis if the track has changed
        if (now_playing['item']['id'] != self.track):
            self.track = now_playing['item']['id']
            self.fetch_intervals()
        
        print('\n=================')
        print('Playback Synced')
        print('delay time %s' % delay_time)
        print('Current progress: ' + str(self.progress))
        print('Current Track: ' + self.track)
        print('=================\n')

    def fetch_intervals(self):
        data = self.sp.audio_analysis(self.track)

        self.intervals = list(map((lambda x : x['start']), data['beats']))
        print(self.intervals)
        print(self.progress)
        #trim intervals to current location in time
        while (self.progress > self.intervals[0]):
            #print(len(self.intervals))
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
            self.sync_playback()
            self.ping_timer = 0

        if self.ttl < 60:
            refresh_credentials()

        if len(self.intervals) > 0 and self.progress > self.intervals[0]:
            self.beat_counter +=1
            print("beat " + str(self.beat_counter%4) + " at " + str(time.time()))
            self.intervals.pop(0)


    def exit(self):
        pass
        #self.refresh_timer.stop()