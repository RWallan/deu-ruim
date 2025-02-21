import sys

import click
import rich
from cyclopts import App
from pydantic_ai import UnexpectedModelBehavior

from deu_ruim.llm.agents import Fixer, Validator
from deu_ruim.llm.deps import FixerDeps
from deu_ruim.llm.schemas import FixerSuccess
from deu_ruim.utils import execute_terminal_cmd

app = App()


@app.default
async def deu_ruim(cmd: str, *, verbose: bool = False):
    """Fix a terminal command and run it.

    Args:
        cmd: Terminal command
        verbose: Show more messages about the run
    """
    deps = FixerDeps(validator_agent=Validator)
    _, error = await execute_terminal_cmd(cmd)
    if error:
        try:
            result = await Fixer.run(
                f'Please, fix the command {cmd}. It provided the error: {error}',  # noqa: E501
                deps=deps,
            )
        except UnexpectedModelBehavior as e:
            if verbose:
                rich.print(e)
            rich.print('[red]Deu ruim! 💀')
            sys.exit(1)

        if isinstance(result.data, FixerSuccess):
            if click.confirm(f'Run {result.data.fixed_command}', default=True):
                stdout, stderr = await execute_terminal_cmd(
                    result.data.fixed_command
                )
                if stderr:
                    if verbose:
                        rich.print(stderr)
                    rich.print('[red]Deu ruim! 💀')
                else:
                    rich.print(stdout)

        else:
            if verbose:
                rich.print(result.data)
            rich.print('[red]Deu ruim! 💀')


if __name__ == '__main__':
    app()
