from datetime import datetime, timezone

import pytest
from freezegun import freeze_time
from pydantic_ai import capture_run_messages, models
from pydantic_ai.messages import (
    ModelRequest,
    ModelResponse,
    SystemPromptPart,
    ToolCallPart,
    ToolReturnPart,
    UserPromptPart,
)
from pydantic_ai.models.test import TestModel

from deu_ruim.llm.agents import Fixer, Validator, fixer_system_prompt
from deu_ruim.llm.deps import FixerDeps

models.ALLOW_MODEL_REQUESTS = False


@pytest.mark.asyncio
async def test_validator_agent():
    system_prompt = """\
You'll receive a terminal command generated by a LLM agent.
Be concise and return True if the command is valid else False.
"""

    with freeze_time('2025-01-01'):
        with capture_run_messages() as messages:
            with Validator.override(
                model=TestModel(custom_result_args='{"response": "True"}')
            ):
                prompt = 'ls'

                await Validator.run(prompt)

        assert messages == [
            ModelRequest(
                parts=[
                    SystemPromptPart(content=system_prompt),
                    UserPromptPart(
                        content=prompt, timestamp=datetime.now(tz=timezone.utc)
                    ),
                ]
            ),
            ModelResponse(
                parts=[
                    ToolCallPart(
                        tool_name='final_result_ValidatorSuccess',
                        args='{"response": "True"}',
                        tool_call_id=None,
                    ),
                ],
                model_name='test',
                timestamp=datetime.now(tz=timezone.utc),
            ),
            ModelRequest(
                parts=[
                    ToolReturnPart(
                        tool_name='final_result_ValidatorSuccess',
                        content='Final result processed.',
                        tool_call_id=None,
                        timestamp=datetime.now(tz=timezone.utc),
                    )
                ]
            ),
        ]


@pytest.mark.asyncio
async def test_fixer_agent():
    system_prompt = await fixer_system_prompt()
    with Validator.override(
        model=TestModel(custom_result_args='{"response": "True"}')
    ):
        deps = FixerDeps(validator_agent=Validator)
        with freeze_time('2025-01-01'):
            with capture_run_messages() as messages:
                with Fixer.override(
                    model=TestModel(
                        custom_result_args='{"fixed_command": "ls"}'
                    )
                ):
                    prompt = (
                        'Please, fix the command sl. '
                        "It provided the error: Command 'sl' not found, "
                        'but can be installed with: sudo apt install sl'
                    )

                    await Fixer.run(prompt, deps=deps)

            assert messages == [
                ModelRequest(
                    parts=[
                        SystemPromptPart(content=system_prompt),
                        UserPromptPart(
                            content=prompt,
                            timestamp=datetime.now(tz=timezone.utc),
                        ),
                    ]
                ),
                ModelResponse(
                    parts=[
                        ToolCallPart(
                            tool_name='final_result_FixerSuccess',
                            args='{"fixed_command": "ls"}',
                            tool_call_id=None,
                        ),
                    ],
                    model_name='test',
                    timestamp=datetime.now(tz=timezone.utc),
                ),
                ModelRequest(
                    parts=[
                        ToolReturnPart(
                            tool_name='final_result_FixerSuccess',
                            content='Final result processed.',
                            tool_call_id=None,
                            timestamp=datetime.now(tz=timezone.utc),
                        )
                    ]
                ),
            ]
