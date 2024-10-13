"""
This module serves as the main entry point for the Play the Wrong Notes.

It orchestrates the user interaction flow for generating music song prompts,
collecting user preferences for genre, time signature, mood, and mode.

The module utilizes other modules for:
- User interface elements (`audio_brainstorm.modules.user_interface`)
- Music theory logic (`audio_brainstorm.modules.music_theory`)
- Prompt generation (`audio_brainstorm.modules.prompt_generation`)

The generated prompt data is then displayed to the user via Terminal.
"""

from audio_brainstorm.modules.user_interface import (
    display_welcome,
    get_parent_genre,
    get_main_genre,
    get_time_signature,
    get_mood,
    get_mode,
    display_output
)
from audio_brainstorm.modules.music_theory import (
    get_bpm_from_genre
)


def get_user_selections():
    """Collects user selections for genre, time signature, mood, and mode."""
    parent_genre_choice = get_parent_genre()
    main_genre_choice = get_main_genre(parent_genre_choice)
    time_signature_choice = get_time_signature()
    mood_data, key = get_mood()
    mode_choice = get_mode()

    return {
        "Parent Genre": parent_genre_choice,
        "Genre": main_genre_choice,
        "Time Signature": time_signature_choice,
        "Mood": mood_data,
        "Key": key,
        "Mode": mode_choice
    }


def main():
    """Main function to run the Audio Brainstorm Gem."""
    display_welcome()
    user_selections = get_user_selections()

    # --- Calculated BPM from music_theory.py based on genre bpm range ---
    bpm = get_bpm_from_genre(
        user_selections["Parent Genre"], user_selections["Genre"])

    output_data = {
        "Parent Genre": user_selections["Parent Genre"],
        "Genre": user_selections["Genre"],
        "Generated BPM": bpm,
        "Time Signature": user_selections["Time Signature"],
        "Mood": user_selections["Mood"],
        "Key": user_selections["Key"],
        "Mode": user_selections["Mode"]
    }

    display_output(output_data)


if __name__ == "__main__":
    main()
