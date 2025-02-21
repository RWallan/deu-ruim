"""Utilities for the app."""

import asyncio


async def execute_terminal_cmd(cmd: str) -> tuple[str, str]:
    """Run a terminal command.

    Args:
        cmd: Terminal command

    Returns:
        stdout and stderr
    """
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    stdout, stderr = await proc.communicate()
    return stdout.decode('utf-8'), stderr.decode('utf-8')
