"""Members: cached from a Keycloak-shaped JSON list. Nothing in git creates one."""

import json
from pathlib import Path

from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, TypeAdapter, ValidationError

from pages.models import Member
from pages.sources.common import SyncResult, abort_if, format_validation_error


class MemberSource(BaseModel):
    """One entry in the external member list."""

    model_config = ConfigDict(extra="forbid")

    username: str
    name: str


_member_list = TypeAdapter(list[MemberSource])


def load_members(path: Path, errors: list[str]) -> list[MemberSource]:
    if not path.is_file():
        errors.append(f"{path}: file not found")
        return []

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        return _member_list.validate_python(raw)
    except json.JSONDecodeError as exc:
        errors.append(f"{path.name}: invalid JSON: {exc}")
    except ValidationError as exc:
        errors.append(f"{path.name}: {format_validation_error(exc)}")
    return []


def sync_members(records: list[MemberSource]) -> SyncResult:
    with transaction.atomic():
        for record in records:
            Member.objects.update_or_create(
                username=record.username, defaults={"name": record.name}
            )
        removed, _ = Member.objects.exclude(
            username__in=[record.username for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_members() -> SyncResult:
    errors: list[str] = []
    records = load_members(settings.MEMBERS_SOURCE, errors)
    abort_if(errors, "sync_members")

    return sync_members(records)
