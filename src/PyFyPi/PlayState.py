from BaseState import BaseState
import ApiLedInterfacer

class PlayState(BaseState):
    def __init__(self, g_state_machine):
        self.g_state_machine = g_state_machine
        self.interfacer = ApiLedInterfacer.ApiLedInterfacer(g_state_machine)

    def update(self, dt):
        self.interfacer.update(dt)

    def exit(self):
        self.interfacer.exit()