from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, field_validator


class ArticleFrontmatter(BaseModel):
    """Frontmatter contract for ``content/blog/*.md``."""

    model_config = ConfigDict(extra="forbid")

    title: str
    date: date
    author: str
    system: str | None = None
    summary: str = ""
    draft: bool = False

    @field_validator("date", mode="before")
    @classmethod
    def coerce_yaml_date(cls, value: object) -> object:
        if isinstance(value, datetime):
            return value.date()
        return value
