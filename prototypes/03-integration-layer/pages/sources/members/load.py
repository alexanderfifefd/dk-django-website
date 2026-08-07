import json
from pathlib import Path

from pydantic import TypeAdapter, ValidationError

from pages.sources.errors import IngestReport
from pages.sources.members.schema import MemberSource
from pages.sources.validation import format_validation_error

MemberList = TypeAdapter(list[MemberSource])


def load_members(path: Path, report: IngestReport) -> list[MemberSource]:
    if not path.is_file():
        report.add(str(path), "file not found")
        return []

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.add(path.name, f"invalid JSON: {exc}")
        return []

    try:
        return MemberList.validate_python(raw)
    except ValidationError as exc:
        report.add(path.name, format_validation_error(exc))
        return []
