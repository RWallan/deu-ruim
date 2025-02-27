import sys

import click
import rich
from cyclopts import App
from pydantic_ai import UnexpectedModelBehavior
from rich.progress import Progress, SpinnerColumn, TextColumn

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
    with Progress(
        SpinnerColumn(), TextColumn('{task.description}'), transient=True
    ) as progress:
        task_id = progress.add_task('Diagnosting command...', total=None)
        deps = FixerDeps(
            validator_agent=Validator, progress=progress, task_id=task_id
        )
        _, error = await execute_terminal_cmd(cmd)
        if error:
            progress.update(
                task_id,
                description='Generating correct comand...',
            )
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
        else:
            rich.print('[green] Nada para fazer!')
            sys.exit(0)

    # HACK: Stop progress explicity otherwise `click.confirm` will not show
    progress.stop()

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
