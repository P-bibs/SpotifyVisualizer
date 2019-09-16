from BaseState import BaseState
import ApiLedInterfacer

class PlayState(BaseState):
    def __init__(self):
        self.interfacer = ApiLedInterfacer.ApiLedInterfacer()

    def update(self, dt):
        self.interfacer.update(dt)

    def exit(self):
        self.interfacer.exit()