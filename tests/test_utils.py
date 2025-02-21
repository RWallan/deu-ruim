import pytest

from deu_ruim.utils import execute_terminal_cmd


@pytest.mark.asyncio
async def test_execute_wrong_cmd_must_return_stderr():
    expected_error = '/bin/sh: 1: sl: not found\n'

    stdout, stderr = await execute_terminal_cmd('sl')

    assert not stdout
    assert stderr == expected_error
