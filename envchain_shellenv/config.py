#!/usr/bin/env python3

from . import __app_name__
import configparser
from pathlib import Path
import importlib

DEFAULT_CONFIG_DIR = Path.home() / '.config' / __app_name__
DEFAULT_CONFIG_PATH = DEFAULT_CONFIG_DIR / 'keychain.ini'
EXAMPLE_CONFIG_PATH = Path(__file__).parent / 'examples' / 'keychain.ini'


def create_example_config():
    """write EXAMPLE_CONFIG_PATH, overwrites config file if exists"""
    import shutil

    DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy(EXAMPLE_CONFIG_PATH, DEFAULT_CONFIG_PATH)


def read_config(config_file) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.optionxform = str  # type: ignore
    config.read(config_file)
    return config


def extract_envchain_pairs(
    config: configparser.ConfigParser,
) -> list[tuple[str, str, str]]:
    """return a list of tuples containing env_var, envchain_namespace, envchain_env"""
    # config is like this:
    # [envchain]
    # TEST = test TEST

    # # equivalent to MULTILINE = test MULTILINE
    # MULTILINE = test
    envchain_pairs = []
    for env_var in config['envchain']:
        val = config['envchain'][env_var]
        if ' ' in val:
            envchain_pairs.append((env_var, val.split(' ')[0], val.split(' ')[1]))
        else:
            envchain_pairs.append((env_var, val, env_var))
    return envchain_pairs


from .core import (
    export_envchain_keyring_multi,
    export_envchain_envchain_multi,
)

use_dict = {
    'envchain': export_envchain_envchain_multi,
}


keyring_spec = importlib.util.find_spec("keyring")  # type: ignore
if keyring_spec:
    use_dict['keyring'] = export_envchain_keyring_multi
