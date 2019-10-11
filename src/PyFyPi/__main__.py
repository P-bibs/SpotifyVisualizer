import os, threading, time, signal
import StateMachine, IdleState, PlayState

states = {
    'IdleState': IdleState.IdleState,
    'PlayState': PlayState.PlayState
}

state_machine = StateMachine.StateMachine(states)
state_machine.change_state('PlayState')

class SignalCatcher:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        print("Got signal " + str(signum))
        self.kill_now = True

current_time = time.time()
signal_catcher = SignalCatcher()

while not signal_catcher.kill_now:
        dt = time.time() - current_time
        current_time = time.time()
        state_machine.update(dt)

state_machine.exit()
print("Exited Gracefully")