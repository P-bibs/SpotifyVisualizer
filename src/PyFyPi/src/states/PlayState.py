from ...lib import auth, config_utils
from ..ApiLedInterfacer import ApiLedInterfacer
from .BaseState import BaseState


class PlayState(BaseState):
    def __init__(self, g_state_machine, global_state):
        self.g_state_machine = g_state_machine

        # Fetch refresh token if needed
        config = config_utils.read_config()
        config = self.check_and_update_refresh_token(config)

        self.interfacer = ApiLedInterfacer(g_state_machine, global_state["pixels"], config)

    def check_and_update_refresh_token(self, config):
        # If a refresh token doesn't exist, request one
        if config['DATA']['refresh_token'] == '':
            response = auth.request_token(
                config['SETUP']['id'],
                config['SETUP']['secret'],
                config['DATA']['code'],
                config['SETUP']['redirect']
            )

            refresh_token = response['refresh_token']
            config['DATA'] = {**config['DATA'], "refresh_token": refresh_token}
            config_utils.write_config(config)

        return config

    def update(self, dt):
        self.interfacer.update(dt)

    def exit(self):
        self.interfacer.exit()
        print("Play state exit completed")
