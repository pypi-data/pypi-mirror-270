import json
import os

ASSET_HOME = os.getenv('SM_ASSET_HOME', default='./_steps/assets')


def get_userdata_path():
    return os.path.join(ASSET_HOME, '_userdata.json')


def get_data():
    with open(get_userdata_path()) as f:
        return json.load(f)


def write_data(data):
    with open(get_userdata_path(), 'w') as f:
        return json.dump(data, f)
