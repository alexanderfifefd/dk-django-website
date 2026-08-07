import json
from dataclasses import dataclass
from pathlib import Path

import frontmatter
from pydantic import TypeAdapter, ValidationError

from pages.models import Member
from pages.sources.errors import IngestReport
from pages.sources.markdown import render_markdown
from pages.sources.systems.schema import SystemFrontmatter, UpdateItem
from pages.sources.validation import format_validation_error

UpdateList = TypeAdapter(list[UpdateItem])


@dataclass(frozen=True)
class SystemRecord:
    slug: str
    title: str
    summary: str
    teamlead_username: str
    admin_usernames: list[str]
    body_html: str
    updates: list[dict[str, str]]


def load_all_systems(
    systems_dir: Path,
    members: dict[str, Member],
    report: IngestReport,
) -> list[SystemRecord]:
    if not systems_dir.is_dir():
        return []

    records: list[SystemRecord] = []
    for system_dir in sorted(systems_dir.iterdir()):
        if not system_dir.is_dir():
            continue

        slug = system_dir.name
        system_path = system_dir / "system.md"
        updates_path = system_dir / "updates.json"

        if not system_path.is_file():
            report.add(f"systems/{slug}/", "missing system.md")
            continue

        record = _load_system_dir(
            slug=slug,
            system_path=system_path,
            updates_path=updates_path,
            members=members,
            report=report,
        )
        if record is not None:
            records.append(record)

    return records


def _load_system_dir(
    *,
    slug: str,
    system_path: Path,
    updates_path: Path,
    members: dict[str, Member],
    report: IngestReport,
) -> SystemRecord | None:
    label = f"systems/{slug}/system.md"
    parsed = frontmatter.load(system_path)

    try:
        frontmatter_data = SystemFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        report.add(label, format_validation_error(exc))
        return None

    if frontmatter_data.teamlead not in members:
        report.add(label, f"unknown teamlead {frontmatter_data.teamlead!r}")
        return None

    unknown_admins = sorted(
        username for username in frontmatter_data.admins if username not in members
    )
    if unknown_admins:
        report.add(label, f"unknown admins: {', '.join(unknown_admins)}")
        return None

    updates: list[dict[str, str]] = []
    if updates_path.is_file():
        updates = _load_updates(f"systems/{slug}/updates.json", updates_path, report)
        if updates is None:
            return None

    return SystemRecord(
        slug=slug,
        title=frontmatter_data.title,
        summary=frontmatter_data.summary,
        teamlead_username=frontmatter_data.teamlead,
        admin_usernames=frontmatter_data.admins,
        body_html=render_markdown(parsed.content),
        updates=updates,
    )


def _load_updates(
    label: str,
    path: Path,
    report: IngestReport,
) -> list[dict[str, str]] | None:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.add(label, f"invalid JSON: {exc}")
        return None

    try:
        items = UpdateList.validate_python(raw)
    except ValidationError as exc:
        report.add(label, format_validation_error(exc))
        return None

    return [item.model_dump() for item in items]
