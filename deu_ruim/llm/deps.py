from dataclasses import dataclass

from pydantic_ai import Agent
from rich.progress import Progress, TaskID

from deu_ruim.llm.schemas import ValidatorResponse


@dataclass
class FixerDeps:
    validator_agent: Agent[None, ValidatorResponse]
    progress: Progress
    task_id: TaskID
