"""
This module handles the menu window output display for the project.
"""
import tkinter as tk
from tkinter import ttk

from audio_brainstorm.modules.prompt_generation import get_synonyms
from audio_brainstorm.data.dictionaries import (
    key_mood_description,
    modes
)

# --- Introductory Output ---


def display_welcome():
    """Displays the welcome message for the Audio Brainstorm Gem."""
    print("\nWelcome to Play the Wrong Notes!\n")
    print("Your creative partner for generating electronic music song prompts.")
    print("Tailored for Google Generative AI, pretty_MIDI, Musixmatch, Spotify, and pre-defined music theory.\n")
    print("Key mood associations and data translation based on the study found here:\n")
    print("Affective Musical Key Characteristics")
    print("https://legacy.wmich.edu/mus-theo/courses/keys.html \n")
    print("pretty_midi 0.2.10")
    print("Colin Raffel and Daniel P. W. Ellis. Intuitive Analysis, Creation and Manipulation of MIDI Data with pretty_midi.")
    print("https://colinraffel.com/publications/ismir2014intuitive.pdf")
    print("In 15th International Conference on Music Information Retrieval Late Breaking and Demo Papers, 2014. \n")


# --- Genre Selection ---
genre_frame = ttk.LabelFrame(window, text="Genre Selection")
genre_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(genre_frame, text="Select Genre:").pack(pady=5)
genres = ["Ambient", "Downtempo", "Breakbeat", "Disco", "House", "Techno",
          "Trance", "Electro", "Industrial", "Jungle", "Drum and Bass",
          "Hardcore", "Chiptune"]
selected_genre = tk.StringVar(window)
genre_combobox = ttk.Combobox(
    window, textvariable=selected_genre, values=genres, state="readonly")
genre_combobox.current(0)  # Set default to Ambient
genre_combobox.pack(pady=5, padx=10)

# --- Time Signature Selection ---
time_signature_frame = ttk.LabelFrame(window, text="Time Signature Selection")
time_signature_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(time_signature_frame, text="Select Time Signature:").pack(pady=5)
time_signatures = ["4/4", "3/4", "6/8", "5/4", "7/8", "12/8"]
selected_time_signature = tk.StringVar(window)
time_signature_combobox = ttk.Combobox(
    window, textvariable=selected_time_signature, values=time_signatures, state="readonly")
time_signature_combobox.current(0)  # Set default to 4/4
time_signature_combobox.pack(pady=5, padx=10)

# --- Mood Selection ---
mood_frame = ttk.LabelFrame(window, text="Mood Selection")
mood_frame.pack(fill="both", padx=10, pady=5, expand=True)

ttk.Label(mood_frame, text="Select Mood:").pack(pady=5)

mood_options = list(key_mood_description.values())

selected_mood = tk.StringVar(window)
mood_entry = ttk.Entry(mood_frame, textvariable=selected_mood)
mood_entry.pack(pady=5, padx=10, fill="x")

listbox = tk.Listbox(mood_frame, height=5)
listbox.pack(pady=5, padx=10, fill="both", expand=True)

typed_text = mood_entry.get().lower()
listbox.delete(0, tk.END)  # Clear the listbox
if typed_text:
    typed_synonyms = get_synonyms(typed_text)
    for option in mood_options:
        combined_description = f"{option['original']} {
            option['paraphrased']}".lower()
        if typed_text in combined_description or any(
                syn in combined_description for syn in typed_synonyms):
            listbox.insert(tk.END, option["paraphrased"])

# --- Mode Selection
mode_frame = ttk.LabelFrame(window, text="Mode Selection")
mode_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(mode_frame, text="Select mode:").pack(pady=5)

mode_var = tk.StringVar(value="Ionian")

for mode, mode_data in modes.items():
    radiobutton = ttk.Radiobutton(mode_frame, text=f"{
                                  mode} ({
                                      mode_data['description']})", variable=mode_var, value=mode)
    radiobutton.pack(anchor="w", padx=10, pady=2)
