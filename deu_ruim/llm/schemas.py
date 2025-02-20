"""Schemas to LLM Agents responses."""

from typing import TypeAlias, Union

from pydantic import BaseModel


class FixerSuccess(BaseModel):
    """Response with the correct command."""

    fixed_command: str


class FixerFail(BaseModel):
    """Response when the user input and the error didn't include enough information."""  # noqa: E501

    error_message: str


class ValidatorSuccess(BaseModel):
    """Response when the command is valid."""

    response: bool


class ValidatorFail(BaseModel):
    """Response when the command is invalid."""

    response: bool


FixerResponse: TypeAlias = Union[FixerSuccess, FixerFail]
ValidatorResponse: TypeAlias = Union[ValidatorSuccess, ValidatorFail]
