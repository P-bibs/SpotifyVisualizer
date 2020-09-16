from BaseState import BaseState

class StateMachine():
    def __init__(self, states, global_state):
        print('Creating State machine with states:')
        print(states)
        self.current_state = BaseState()
        self.global_state = global_state
        
        self.states = states

    def change_state(self, new_state, new_global_state={}):
        print("Exiting current state...")
        self.current_state.exit()

        print("Updating global state")
        self.global_state = {**self.global_state, **new_global_state}

        print("Entering " + new_state)
        self.current_state = self.states[new_state](self, self.global_state)

    def update(self, dt):
        self.current_state.update(dt)

    def exit(self):
        self.current_state.exit()