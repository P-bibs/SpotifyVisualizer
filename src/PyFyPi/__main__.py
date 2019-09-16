import os
import threading
import time
import StateMachine

state_machine = StateMachine.StateMachine()
current_time = time.time()
while True:
    try:
        dt = time.time() - current_time
        current_time = time.time()
        state_machine.update(dt)
        
    except KeyboardInterrupt:
        state_machine.exit()
        break