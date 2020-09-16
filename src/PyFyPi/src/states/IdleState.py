from .BaseState import BaseState


class IdleState(BaseState):
    def __init__(self, g_state_machine, extra_state):
        print("Entering Idle State")
        self.timer = 0
        self.g_state_machine = g_state_machine
        self.beat_line = extra_state['beat_line'] if 'beat_line' in extra_state else None

    def update(self, dt):
        self.timer += dt

        if self.timer % 1 < .0001:
            print("Idle Timer... " + str(self.timer))

        if self.timer > 100:
            print("Checking if user has current playback...")
            self.g_state_machine.change_state('PlayState', beat_line=self.beat_line)

    def exit(self):
        print("Exiting Idle State")