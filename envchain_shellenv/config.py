#!/usr/bin/env python3

from .types import ConfigDict, EnvVar, EnvchainNamespace, EnvchainEnv, EnvchainTuple
from . import __app_name__

# import configparser
from pathlib import Path
import importlib.util

DEFAULT_CONFIG_DIR = Path.home() / '.config' / __app_name__
DEFAULT_CONFIG_PATH = DEFAULT_CONFIG_DIR / 'keychain.yaml'
EXAMPLE_CONFIG_PATH = Path(__file__).parent / 'examples' / 'keychain.yaml'


def create_example_config():
    """write EXAMPLE_CONFIG_PATH, overwrites config file if exists"""
    import shutil

    DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy(EXAMPLE_CONFIG_PATH, DEFAULT_CONFIG_PATH)


def read_config(config_file: Path) -> ConfigDict:
    from yaml import safe_load

    config = safe_load(config_file.read_text())
    return config


def extract_envchain_pairs(
    config: ConfigDict,
) -> list[EnvchainTuple]:
    """return a list of tuples containing env_var, envchain_namespace, envchain_env"""
    envchain_pairs = []
    for envchain_ns, envchain_ns_value in config.items():
        if envchain_ns_value is None:
            continue
        for env_var, envchain_env in envchain_ns_value.items():
            if envchain_env is None:
                envchain_env = env_var
            envchain_pairs.append((env_var, envchain_ns, envchain_env))
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
