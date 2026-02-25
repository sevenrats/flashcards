#!/usr/bin/env python3
"""Core helpers for building Anki decks."""

import genanki
from pathlib import Path

# Unique model ID (must stay constant once created)
MODEL_ID = 1607392319

basic_model = genanki.Model(
    MODEL_ID,
    "Basic Flashcard Model",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Front}}",
            "afmt": "{{FrontSide}}<hr id='answer'>{{Back}}",
        },
    ],
)


def create_deck(
    deck_name: str,
    cards: list[tuple[str, str]],
    output_dir: Path,
) -> Path:
    """Build an .apkg file for *deck_name* and write it to *output_dir*."""
    deck_id = abs(hash(deck_name)) % (10**10)
    deck = genanki.Deck(deck_id, deck_name)

    for front, back in cards:
        note = genanki.Note(
            model=basic_model,
            fields=[front, back],
        )
        deck.add_note(note)

    output_path = output_dir / f"{deck_name.replace('::', '_')}.apkg"
    genanki.Package(deck).write_to_file(output_path)
    print(f"✅ Created {output_path}")
    return output_path
