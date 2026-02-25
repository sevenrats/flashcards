"""Deck catalogue – one sub-module per language.

Use ``get_decks(language)`` to retrieve the card map for a given
:class:`~flashcards.languages.Language`.
"""

from flashcards.languages import Language
from flashcards.decks import german

# Registry: maps Language enum members to their deck dictionaries.
_REGISTRY: dict[Language, dict[str, list[tuple[str, str]]]] = {
    Language.GERMAN: german.DECKS,
}


def get_decks(language: Language) -> dict[str, list[tuple[str, str]]]:
    """Return the deck mapping for *language*, or raise ``KeyError``."""
    try:
        return _REGISTRY[language]
    except KeyError:
        supported = ", ".join(l.value for l in _REGISTRY)
        raise KeyError(
            f"No decks registered for {language.value!r}. "
            f"Supported languages: {supported}"
        ) from None
