from IdleState import IdleState
from PlayState import PlayState

class StateMachine():
    def __init__(self):
        self.current_state = PlayState()
        
        self.states = {
            'IdleState': IdleState,
            'PlayState': PlayState
        }

    def change_state(self, new_state):
        print("Exiting current state...")
        self.current_state.exit()
        print("Entering " + new_state)
        self.current_state = self.states[new_state]()

    def update(self, dt):
        self.current_state.update(dt)

    def exit(self):
        self.current_state.exit()