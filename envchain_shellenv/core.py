#!/usr/bin/env python3


def export_envchain_keyring(
    env_var: str,
    envchain_namespace: str,
    envchain_env: str,
) -> str:
    """set env_var to the password of envchain_env of account envchain-{envchain_namespace} in the keychain
    return a string to be eval'd by the shell"""
    import keyring

    password = keyring.get_password(f"envchain-{envchain_namespace}", envchain_env)
    return f"export {env_var}='{password}'"


async def export_envchain_envchain(
    env_var: str, envchain_namespace: str, envchain_env: str
) -> str:
    """get the env vars with envchain executable"""
    import asyncio
    from asyncio.subprocess import Process

    # run this command in async subprocess:
    # envchain envchain_namespace printenv envchain_env
    proc: Process = await asyncio.create_subprocess_exec(
        "envchain",
        envchain_namespace,
        "printenv",
        envchain_env,
        stdout=asyncio.subprocess.PIPE,
    )
    # wait for the process to finish:
    stdout, _ = await proc.communicate()
    # return the env var:
    return f"export {env_var}='{stdout.decode().strip()}'"
    # return f"export {env_var}='{password}'"


async def export_envchain_keyring_multi(
    envchain_pairs: list[tuple[str, str, str]]
) -> str:
    import asyncio
    from concurrent.futures import ThreadPoolExecutor
    from functools import partial

    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(pool, partial(export_envchain_keyring, *pair))
            for pair in envchain_pairs
        ]
        export_commands = await asyncio.gather(*tasks)
    return '\n'.join(export_commands)


async def export_envchain_envchain_multi(
    envchain_pairs: list[tuple[str, str, str]]
) -> str:
    import asyncio

    tasks = [
        asyncio.create_task(export_envchain_envchain(*pair)) for pair in envchain_pairs
    ]
    export_commands = await asyncio.gather(*tasks)
    return '\n'.join(export_commands)
