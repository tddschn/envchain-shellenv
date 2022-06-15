#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-05-26
Purpose: envchain shellenv
"""

import argparse
from pathlib import Path
from . import __version__, __app_name__, __description_long__, __project_info__
from .config import (
    read_config,
    extract_envchain_pairs,
    use_dict,
    DEFAULT_CONFIG_PATH,
    create_example_config,
)
from .core import unset_env_vars


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        prog=__app_name__,
        description=__description_long__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=__project_info__,
    )

    parser.add_argument(
        '-c', '--config', default=DEFAULT_CONFIG_PATH, help='config file', type=Path
    )

    parser.add_argument(
        '-s',
        '--section',
        '--envchain-namespace',
        help='''Only export from this section (aka envchain namespace) in the config.
        The choices shown are for the config file at the default location.''',
        type=str,
        choices=read_config(DEFAULT_CONFIG_PATH).keys(),
    )

    parser.add_argument(
        '--create-example-config',
        action='store_true',
        help='create example config file',
    )

    parser.add_argument(
        '-u',
        '--use',
        help='What to use to extract secrets',
        type=str,
        default='envchain',
        choices=use_dict.keys(),
    )

    parser.add_argument('-U', '--unset', help='Unset env vars', action='store_true')

    parser.add_argument(
        '--version', '-V', action='version', version='%(prog)s {}'.format(__version__)
    )

    return parser.parse_args()


async def main(args) -> None:
    if args.create_example_config:
        create_example_config()
        print(f'Created example config file at {str(DEFAULT_CONFIG_PATH)}')
        return
    use = args.use
    config_path = args.config
    section = args.section
    export_envchain_multi = use_dict[use]
    config = read_config(config_path)
    if section:
        config = {section: config[section]}
    envchain_pairs = extract_envchain_pairs(config)
    if args.unset:
        unset_commands = unset_env_vars(envchain_pairs)
        print(unset_commands)
        return
    export_commands = await export_envchain_multi(envchain_pairs)
    print(export_commands)


def main_sync() -> None:
    args = get_args()
    import asyncio

    asyncio.run(main(args))


if __name__ == '__main__':
    main_sync()
