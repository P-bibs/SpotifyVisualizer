import json

from ..globals import CONFIG_PATH


def read_config():
    with open(CONFIG_PATH) as f:
        config = json.load(f)

    return config

def write_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
