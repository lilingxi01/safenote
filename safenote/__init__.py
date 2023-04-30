import os
from getpass import getpass
from typing import List, Union


def request(key: Union[str, None] = None,
            keys: Union[List[str], None] = None,
            inject_env: bool = True):
    env = dict()
    if key is not None:
        if type(key) == str:
            env[key] = _request_single(key, inject_env)
        else:
            raise TypeError('key must be a string or None')
    elif keys is not None:
        if type(keys) == list:
            for key in keys:
                env[key] = _request_single(key, inject_env)
        else:
            raise TypeError('keys must be a list or None')
    return env


def _request_single(key: str,
                    inject_env: bool = True):
    if key not in globals():
        value = getpass(f'Enter the {key}:')
        globals()[key] = value
        if inject_env:
            os.environ[key] = value
        print(f'{key} is now ready')
    else:
        value = globals()[key]
        print(f'{key} has already been defined')
    return value
