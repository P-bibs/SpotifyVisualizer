from BaseState import BaseState

class IdleState(BaseState):
    def __init__(self, g_state_machine):
        print("Entering Idle State")
        self.timer = 0
        self.g_state_machine = g_state_machine

    def update(self, dt):
        self.timer += dt

        if self.timer % 10 < .02:
            print("Idle Timer... " + str(self.timer))

        if self.timer > 10:
            print("Checking if user has current playback...")
            self.g_state_machine.change_state('PlayState')

    def exit(self):
        print("Exiting Idle State")