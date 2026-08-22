"""Shared shortcode errors and parsing helpers."""

from __future__ import annotations

import yaml
from pydantic import ValidationError


class ShortcodeError(ValueError):
    """Invalid shortcode in an article body."""


def parse_yaml_mapping(body: str, *, name: str) -> dict:
    try:
        data = yaml.safe_load(body.strip())
    except yaml.YAMLError as exc:
        raise ShortcodeError(f"{name}: invalid YAML ({exc})") from exc

    if not isinstance(data, dict):
        raise ShortcodeError(f"{name}: expected key/value fields")
    return data


def validation_message(exc: ValidationError) -> str:
    return "; ".join(
        f"{'.'.join(str(part) for part in error['loc']) or 'value'}: {error['msg']}"
        for error in exc.errors()
    )
