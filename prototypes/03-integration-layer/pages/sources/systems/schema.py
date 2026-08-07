from pydantic import BaseModel, ConfigDict, Field


class SystemFrontmatter(BaseModel):
    """Frontmatter contract for ``content/systems/<slug>/system.md``."""

    model_config = ConfigDict(extra="forbid")

    title: str
    summary: str = ""
    teamlead: str
    admins: list[str] = Field(default_factory=list)


class UpdateItem(BaseModel):
    """One row in ``content/systems/<slug>/updates.json``."""

    model_config = ConfigDict(extra="forbid")

    date: str
    kind: str
    message: str
