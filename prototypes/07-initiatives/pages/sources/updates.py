"""Updates: record-like JSON beside each system at ``updates.json``."""

import json
from pathlib import Path

from pydantic import BaseModel, ConfigDict, TypeAdapter, ValidationError

from pages.sources.common import format_validation_error


class UpdateItem(BaseModel):
    model_config = ConfigDict(extra="forbid")

    date: str
    kind: str
    message: str


_update_list = TypeAdapter(list[UpdateItem])


def load_updates(
    path: Path, slug: str, errors: list[str], *, collection: str = "systems"
) -> list[dict[str, str]] | None:
    if not path.is_file():
        return []

    label = f"{collection}/{slug}/updates.json"
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        items = _update_list.validate_python(raw)
    except json.JSONDecodeError as exc:
        errors.append(f"{label}: invalid JSON: {exc}")
        return None
    except ValidationError as exc:
        errors.append(f"{label}: {format_validation_error(exc)}")
        return None

    return [item.model_dump() for item in items]
