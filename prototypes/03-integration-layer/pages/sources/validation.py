from pydantic import ValidationError


def format_validation_error(exc: ValidationError) -> str:
    parts = []
    for error in exc.errors():
        location = ".".join(str(part) for part in error["loc"]) if error["loc"] else "value"
        parts.append(f"{location}: {error['msg']}")
    return "; ".join(parts)
