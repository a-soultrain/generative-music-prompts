"""
This modules handles music theory logic and configuration for Play the Wrong Notes.

It includes:
- BPM Ranges
- Key-Mood Associations
- Roman numeral/Note translation
"""
import random
import re
from audio_brainstorm.data.dictionaries import (
    main_genre,
    key_mood_description
)


def get_bpm_from_genre(parent_genre, genre):
    """Returns a random BPM within the range for the given genre."""
    if parent_genre in main_genre:
        for main_genre_value in main_genre[parent_genre].values():
            if genre in main_genre_value.get("subgenres", []):
                bpm_range = main_genre_value["bpm_range"]
                return random.randint(bpm_range[0], bpm_range[1])
    return None


def get_key_from_mood(mood, threshold=1):
    """
    Returns the key and its original description associated with the given mood
    (case-insensitive and trimmed).
    """
    mood = mood.lower()  # Converts mood to lowercase
    # Removes non-alphabetical characters
    mood = re.sub(r'[^a-zA-Z\s]', '', mood)
    mood_tokens = set(mood.split())

    best_match = None
    max_overlap = 0

    for key, mood_data in key_mood_description.items():
        combined_description = f"{mood_data['original']} {
            mood_data['paraphrased']}".lower()
        combined_description = re.sub(r'[^a-zA-Z\s]', '', combined_description)
        desciption_tokens = set(combined_description.split())

        # Calculate Overlap
        overlap = len(mood_tokens & desciption_tokens)

        if overlap > max_overlap and overlap >= threshold:
            max_overlap = overlap
            best_match = (key, mood_data["original"], mood_data["notes"])

    return best_match if best_match else (None, None, None)


def translate_roman_to_note(key, roman_numeral, key_note, is_chord=True):
    """Translates a Roman numeral to a note based on the given key."""
    roman_to_degree = {
        "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
        "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7
    }
    degree = roman_to_degree.get(roman_numeral)
    if degree is not None:
        note = key_note[(degree - 1) % len(key_note)]

        # Handle accidentals (sharps and flats) based on key
        if "#" in key and note not in ("E", "B") and not "#" in note:
            note += "#"
        elif "b" in key and note not in ("C", "F") and not "b" in note:
            note += "b"

            # Determine chord quality (major or minor)
        if is_chord:
            if roman_numeral.isupper():
                chord_quality = "maj"
            else:
                chord_quality = "min"
            return f"{note}{chord_quality}"  # Return note with chord quality
        else:
            return note
    else:  # For mode tonic positions, just return the note
        return roman_numeral  # Return the original, if not a valid Roman numeral
