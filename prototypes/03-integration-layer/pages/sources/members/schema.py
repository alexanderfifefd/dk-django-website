from pydantic import BaseModel, ConfigDict, Field


class MemberSource(BaseModel):
    """A row from the Keycloak-shaped members fixture."""

    model_config = ConfigDict(extra="forbid")

    username: str
    name: str
