from BaseState import BaseState

class StateMachine():
    def __init__(self, states):
        print('Creating State machine with states:')
        print(states)
        self.current_state = BaseState()
        
        self.states = states

    def change_state(self, new_state, **kwargs):
        print("Exiting current state...")
        self.current_state.exit()
        print("Entering " + new_state)
        self.current_state = self.states[new_state](self, kwargs)

    def update(self, dt):
        self.current_state.update(dt)

    def exit(self):
        self.current_state.exit()