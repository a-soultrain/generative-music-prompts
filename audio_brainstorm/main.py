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


def display_welcome():
    """Displays the welcome message for the Audio Brainstorm Gem."""
    print("\nWelcome to Audio Brainstorm!\n")
    print("Your creative partner for generating electronic music song prompts.")
    print("Tailored for Google Generative AI, pretty_MIDI, Musixmatch, Spotify, and pre-defined music theory.\n")
    print("Key mood associations and data translation based on the study found here:\n")
    print("Affective Musical Key Characteristics")
    print("https://legacy.wmich.edu/mus-theo/courses/keys.html \n")
    print("pretty_midi 0.2.10")
    print("Colin Raffel and Daniel P. W. Ellis. Intuitive Analysis, Creation and Manipulation of MIDI Data with pretty_midi.")
    print("https://colinraffel.com/publications/ismir2014intuitive.pdf")
    print("In 15th International Conference on Music Information Retrieval Late Breaking and Demo Papers, 2014. \n")


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
