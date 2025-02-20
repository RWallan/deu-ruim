from dataclasses import dataclass

from pydantic_ai import Agent

from deu_ruim.llm.schemas import ValidatorResponse


@dataclass
class FixerDeps:
    validator_agent: Agent[None, ValidatorResponse]
