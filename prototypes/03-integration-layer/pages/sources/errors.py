from dataclasses import dataclass, field


@dataclass
class IngestReport:
    errors: list[str] = field(default_factory=list)

    def add(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def extend(self, location: str, messages: list[str]) -> None:
        for message in messages:
            self.add(location, message)


@dataclass(frozen=True)
class SyncResult:
    upserted: int
    removed: int
