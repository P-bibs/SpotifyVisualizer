import os
import threading
import time
import auth
import ApiLedInterfacer

interfacer = ApiLedInterfacer.ApiLedInterfacer()
current_time = time.time()
while True:
    try:
        dt = time.time() - current_time
        current_time = time.time()
        interfacer.update(dt)
        
    except KeyboardInterrupt:
        interfacer.exit()
        break