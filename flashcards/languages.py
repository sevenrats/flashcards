from enum import Enum


class Language(Enum):
    GERMAN = "german"

    @classmethod
    def choices(cls) -> list[str]:
        """Return lowercase language names accepted by the CLI."""
        return [member.value for member in cls]
