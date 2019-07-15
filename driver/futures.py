import time
from requests_futures.sessions import FuturesSession

class Futures:
    def __init__(self):
        self.session = FuturesSession()
        self.future_one = self.session.get('http://httpbin.org/get')
        self.intervals = []

    def fetch_progress(self):
        self.future_one = self.session.get('http://httpbin.org/get')
        self.future_one.add_done_callback(self.sync_progress)

    def sync_progress(self, response):
        self.progress = response.progress_ms/1000

        while self.progress > self.intervals[0]:
            self.intervals.pop(0)

    def update(self, dt):
        if not self.future_one.done():
            print("Future not done")
        else:
            print("Future completed")


driver = Futures()
current_time = time.time()
while True:
    dt = time.time() - current_time
    current_time = time.time()
    driver.update(dt)