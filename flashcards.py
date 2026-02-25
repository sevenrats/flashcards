#!/usr/bin/env python3

import genanki
import os
from pathlib import Path

OUTPUT_DIR = Path("anki_apkg_decks")
OUTPUT_DIR.mkdir(exist_ok=True)

# Unique model ID (must stay constant once created)
MODEL_ID = 1607392319

basic_model = genanki.Model(
    MODEL_ID,
    "German Basic Model",
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

def create_deck(deck_name, cards):
    deck_id = abs(hash(deck_name)) % (10**10)
    deck = genanki.Deck(deck_id, deck_name)

    for front, back in cards:
        note = genanki.Note(
            model=basic_model,
            fields=[front, back],
        )
        deck.add_note(note)

    output_path = OUTPUT_DIR / f"{deck_name.replace('::', '_')}.apkg"
    genanki.Package(deck).write_to_file(output_path)
    print(f"✅ Created {output_path}")

# -----------------------------
# Deck Definitions
# -----------------------------

decks = {
    "German Cases::Nominative Pronouns": [
        ("I", "ich"),
        ("you (informal singular)", "du"),
        ("he", "er"),
        ("she", "sie"),
        ("it", "es"),
        ("we", "wir"),
        ("you (plural informal)", "ihr"),
        ("they", "sie"),
        ("you (formal)", "Sie"),
    ],
    "German Cases::Accusative Pronouns": [
        ("me", "mich"),
        ("you (informal singular)", "dich"),
        ("him", "ihn"),
        ("her", "sie"),
        ("it", "es"),
        ("us", "uns"),
        ("you (plural informal)", "euch"),
        ("them", "sie"),
        ("you (formal)", "Sie"),
    ],
    "German Cases::Dative Pronouns": [
        ("to/for me", "mir"),
        ("to/for you (informal singular)", "dir"),
        ("to/for him", "ihm"),
        ("to/for her", "ihr"),
        ("to/for it", "ihm"),
        ("to/for us", "uns"),
        ("to/for you (plural informal)", "euch"),
        ("to/for them", "ihnen"),
        ("to/for you (formal)", "Ihnen"),
    ],
    "German Cases::Accusative Prepositions": [
        ("through", "durch"),
        ("for", "für"),
        ("against", "gegen"),
        ("without", "ohne"),
        ("around", "um"),
        ("along", "entlang"),
    ],
    "German Cases::Dative Prepositions": [
        ("from (origin)", "aus"),
        ("except", "außer"),
        ("with", "mit"),
        ("after", "nach"),
        ("since (time)", "seit"),
        ("from (person/place)", "von"),
        ("at/near", "bei"),
        ("opposite", "gegenüber"),
    ],
    "German Cases::Dual-Purpose Prepositions": [
        ("on (vertical surface)", "an"),
        ("on (horizontal surface)", "auf"),
        ("behind", "hinter"),
        ("in", "in"),
        ("next to", "neben"),
        ("over", "über"),
        ("under", "unter"),
        ("in front of", "vor"),
        ("between", "zwischen"),
        ("When do dual prepositions take accusative?",
         "When there is motion toward a destination."),
        ("When do dual prepositions take dative?",
         "When describing location (no movement)."),
    ],
    "German Cases::Dative Verbs": [
        ("to answer", "antworten"),
        ("to thank", "danken"),
        ("to help", "helfen"),
        ("to give", "geben"),
        ("to belong to", "gehören"),
        ("to please", "gefallen"),
        ("to believe", "glauben"),
        ("to congratulate", "gratulieren"),
        ("to fit", "passen"),
        ("to happen", "passieren"),
        ("to hurt", "wehtun"),
        ("What case do these verbs take?", "Dative"),
    ],
    "German Cases::Motion vs Location Contrast": [
        ("Ich gehe in ___ Park. (motion)", "den (Akk)"),
        ("Ich bin in ___ Park. (location)", "dem (Dat)"),
        ("Ich stelle das Buch auf ___ Tisch. (motion)", "den (Akk)"),
        ("Das Buch liegt auf ___ Tisch. (location)", "dem (Dat)"),
        ("Ich hänge das Bild an ___ Wand. (motion)", "die (Akk)"),
        ("Das Bild hängt an ___ Wand. (location)", "der (Dat)"),
    ],
    "German Cases::Sentence Drills": [
        ("I see him.", "Ich sehe ihn. (Akk)"),
        ("She helps me.", "Sie hilft mir. (Dat)"),
        ("I’m going into the park.", "Ich gehe in den Park. (Akk)"),
        ("I’m in the park.", "Ich bin im Park. (Dat)"),
        ("He puts the cup on the table.",
         "Er stellt die Tasse auf den Tisch. (Akk)"),
        ("The cup is on the table.",
         "Die Tasse steht auf dem Tisch. (Dat)"),
    ],
}

# -----------------------------
# Generate All Decks
# -----------------------------

for name, cards in decks.items():
    create_deck(name, cards)

print("\n🎉 All decks generated successfully.")