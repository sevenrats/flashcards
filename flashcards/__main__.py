#!/usr/bin/env python3
"""CLI entry-point: ``python -m flashcards``."""

import argparse
from pathlib import Path

from flashcards.languages import Language


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Anki flashcard decks (.apkg files).",
    )
    parser.add_argument(
        "--language",
        "-l",
        required=True,
        choices=Language.choices(),
        help="Target language for the flashcard decks.",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        required=True,
        type=Path,
        help="Directory where .apkg deck files will be written.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    language = Language(args.language)
    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Import here so the module is only loaded once args are validated.
    from flashcards.flashcards import create_deck, basic_model  # noqa: F401
    from flashcards.decks import get_decks

    decks = get_decks(language)

    for name, cards in decks.items():
        create_deck(name, cards, output_dir)

    print("\n🎉 All decks generated successfully.")


if __name__ == "__main__":
    main()
