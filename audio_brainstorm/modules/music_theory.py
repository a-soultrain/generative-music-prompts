"""
This modules handles music theory logic and configuration for the audio_brainstorm project.

It includes:
- BPM Ranges
- Key-Mood Associations
- Roman numeral/Note translation
"""
"""
For archive, here is old code from main.py:

from audio_brainstorm.config.settings import logging
from audio_brainstorm.modules.music_theory import (
    get_key_from_mood,
    get_bpm_from_genre,
    translate_roman_to_note
)
from audio_brainstorm.data.dictionaries import (
    major_progressions,
    minor_progressions,
    modes
)
from audio_brainstorm.modules.user_interface import (
    selected_genre,
    selected_time_signature,
    output_text,
    output_frame,
    messagebox,
    mood_entry,
    mode_var,
    tk,
    random
)

def confirm_selections():
    try:
        logging.info("Confirm Selections Function Called")  # Debugging

        confirmed_genre = selected_genre.get()
        time_signature_val = selected_time_signature.get()
        selected_mood_val = mood_entry.get()
        logging.info(f"{confirmed_genre}")
        logging.info(f"{time_signature_val}")
        logging.info(f"{selected_mood_val}")

        selected_key, original_description, key_notes = get_key_from_mood(
            selected_mood_val)
        logging.info(f"{selected_key}")

        if selected_key is None:
            messagebox.showerror(
                "Error", "No matching key found for the selected mood")
            logging.error("No matching key found")
            return

        chord_progression = random.choice(
            major_progressions if "Major" in selected_key else minor_progressions)
        selected_mode = mode_var.get()
        selected_bpm_val = get_bpm_from_genre(confirmed_genre)
        logging.info(f"{selected_bpm_val}")

        chord_progression_notes = [
            translate_roman_to_note(
                selected_key, roman, key_notes, is_chord=True)
            for roman in chord_progression.split(' - ')
        ]
        logging.info(f"{chord_progression_notes}")

        if selected_mode in modes and "tonic positions" in modes[selected_mode]:
            tonic_positions_notes = [
                translate_roman_to_note(
                    selected_key, roman, key_notes, is_chord=False)
                for roman in modes[selected_mode]["tonic positions"].split(' - ')
            ]
        else:
            tonic_positions_notes = []
        logging.info(f"{tonic_positions_notes}")

        chord_progression_formatted = ' - '.join(chord_progression_notes)
        tonic_positions_notes_formatted = ' - '.join(tonic_positions_notes)
        mode_formatted = f"{selected_mode} Mode:"
        logging.info(f"{mode_formatted}")

        output = (
            f"Main Genre: {confirmed_genre}\n"
            f"Key: {selected_key}\n"
            f"Key Description: {original_description}\n"
            f"Generated BPM: {selected_bpm_val}\n"
            f"Time Signature: {time_signature_val}\n"
            f"Chord Progression: {chord_progression_formatted}\n"
            f"{mode_formatted} {tonic_positions_notes_formatted}"
        )

        # Display the output in the GUI
        output_text.configure(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, output)
        output_text.configure(state='disabled')

        output_frame.update_idletasks()

    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))
        logging.error(f"Error in confirm_selections: {e}")
"""

selected_genre = None
selected_bpm = None
selected_time_signature = None
selected_mood = None
selected_key = None
selected_mode = None


def get_bpm_from_genre(genre):
    """
    Returns a random BPM within the range for the given genre
    and stores it in the global variable 'selected_bpm'.
    """
    import random

    if genre in bpm_ranges:
        bpm_range = random.choice(bpm_ranges[genre])
        selected_bpm = random.randint(bpm_range[0], bpm_range[1])
    else:
        selected_bpm = 120  # Default to 120 BPM if no genre found
    return selected_bpm


def get_key_from_mood(mood, threshold=1):
    """
    Returns the key and its original description associated with the given mood
    (case-insensitive and trimmed).
    """
    import re

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
