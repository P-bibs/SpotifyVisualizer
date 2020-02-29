from BaseState import BaseState
import ApiLedInterfacer

class PlayState(BaseState):
    def __init__(self, g_state_machine, extra_state):
        self.g_state_machine = g_state_machine
        if "beat_line" in extra_state:
            self.interfacer = ApiLedInterfacer.ApiLedInterfacer(g_state_machine, extra_state['beat_line'])
        else:
            self.interfacer = ApiLedInterfacer.ApiLedInterfacer(g_state_machine, None)

    def update(self, dt):
        self.interfacer.update(dt)

    def exit(self):
        self.interfacer.exit()