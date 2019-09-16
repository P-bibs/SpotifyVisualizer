from BaseState import BaseState

class IdleState(BaseState):
    def __init__(self):
        print("Entering Idle State")

    def update(self, dt):
        pass

    def exit(self):
        print("Exiting Idle State")