import tkinter as tk
from tkinter import ttk  # More modern-looking widgets
import random
import re
import nltk
from nltk.corpus import wordnet

  # Necessary NLTK ddta
nltk.download('wordnet')
nltk.download('omw-1.4')

selected_genre = None
selected_bpm = None
selected_time_signature = None
selected_mood = None
selected_key = None
selected_mode = None

def display_welcome():
  """Displays the welcome message for the Audio Brainstorm Gem."""
  print("\nWelcome to Audio Brainstorm!\n")
  print("Your creative partner for generating electronic music song prompts.")
  print("Tailored for Ableton Live 12 Standard Edition, Novation Launchpad X, Splice, and Xfer Serum.\n")
  print("Key mood associations and data translation based on the study found here:\n")
  print("Affective Musical Key Characteristics")
  print("https://legacy.wmich.edu/mus-theo/courses/keys.html \n")

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace(' - ', ' '))
    return synonyms
  
  # --- BPM Generation Logic ---
bpm_ranges = {
      "Ambient": [(70, 120)],  # 70-120 BPM
      "Downtempo": [(70, 110)],  # 70-110 BPM
      "Breakbeat": [(110, 150)],  # 110-150 BPM
      "Disco": [(110, 130)],  # 110-130 BPM
      "House": [(110, 140)],  # 110-140 BPM
      "Techno": [(110, 160)],  # 110-160 BPM
      "Trance": [(110, 150)],  # 110-150 BPM
      "Electro": [(120, 140)],  # 120-140 BPM
      "Industrial": [(130, 150)],  # 130-150 BPM
      "Jungle": [(150, 170)],  # 150-170 BPM
      "Drum and Bass": [(160, 180)],  # 160-180 BPM
      "Hardcore": [(90, 300)],  # 90-300 BPM 
      "Chiptune": [(80, 200)]  # 80-200 BPM
}

  # --- Affective Musical Key Characteristics ---
key_mood_description = {
  "C Major": {
    "original": "Completely Pure. Its character is: innocence, simplicity, naivety, children's talk.",
    "paraphrased": "Pure, innocent, naive, simplicity.",
    "notes": ["C", "D", "E", "F", "G", "A", "B", "C"]
  },
  "C Minor": {
    "original": "Declaration of love and at the same time the lament of unhappy love. All languishing, longing, sighing of the love-sick soul lies in this key.",
    "paraphrased": "Love's declaration and lament for lost love-longing and heartache.",
    "notes": ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"]
  },
  "Db Major": {
    "original": "A leering key, degenerating into grief and rapture. It cannot laugh, but it can smile; it cannot howl, but it can at least grimace its crying. Consequently only unusual characters and feelings can be brought out in this key.",
    "paraphrased": "A strange key, balancing between grief and jow, with unusual emotions. Enigma.",
    "notes": ["Db", "Eb", "F", "G", "Ab", "Bb", "C", "Db"]
  },
  "C# Minor": {
    "original": "Penitential lamentation, intimate conversation with God, the friend and help-meet of life; sighs of disappointed friendship and love lie in its radius.",
    "paraphrased": "Sorrowful prayers, disappointed love and friendship.",
    "notes": ["C#", "D#", "E", "F#", "G#", "A", "B", "C#"]
  },
  "D Major": {
    "original": "The key of triumph, of Hallejuahs, of war-cries, of victory-rejoicing. Thus, the inviting symphonies, the marches, holiday songs and heaven-rejoicing choruses are set in this key.",
    "paraphrased": "Triumphant, victorious, filled with joy and celebration. Ceremony",
    "notes": ["D", "E", "F#", "G", "A", "B", "C#", "D"]
  },
  "D Minor": {
    "original": "Melancholy womanliness, the spleen and humours brood.",
    "paraphrased": "Melancholy, sadness, gloom.",
    "notes": ["D", "E", "F", "G", "A", "Bb", "C", "D"]
  },
  "Eb Major": {
    "original": "The key of love, of devotion, of intimate conversation with God.",
    "paraphrased": "Devotion, love, and spiritual connection. Religion or religious.",
    "notes": ["Eb", "F", "G", "Ab", "Bb", "C", "D", "Eb"]
  },
  "D# Minor": {
    "original": "Feelings of the anxiety of the soul's deepest distress, of brooding despair, of blackest depresssion, of the most gloomy condition of the soul. Every fear, every hesitation of the shuddering heart, breathes out of horrible D# minor. If ghosts could speak, their speech would approximate this key.",
    "paraphrased": "Deep despair, soul-crushing anxiety and fear.",
    "notes": ["D#", "E#", "F#", "G#", "A#", "B", "C#", "D#"]
  },
  "E Major": {
    "original": "Noisy shouts of joy, laughing pleasure and not yet complete, full delight lies in E Major.",
    "paraphrased": "Joyous, cheerful, but not fully content. Complacent.",
    "notes": ["E", "F#", "G#", "A", "B", "C#", "D#", "E"]
  },
  "E Minor": {
    "original": "Naive, innocent declaration of love, lament without grumbling; sighs accompanied by few tears; this key speaks of the imminent hope of resolving in the pure happiness of C major.",
    "paraphrased": "Innocent love, gentle lament, with hope for happiness. Happy.",
    "notes": ["E", "F#", "G", "A", "B", "C", "D", "E"]
  },
  "F Major": {
    "original": "Complaisance & Calm.",
    "paraphrased": "Calm and agreeable.",
    "notes": ["F", "G", "A", "Bb", "C", "D", "E", "F"]
  },
  "F Minor": {
    "original": "Deep depression, funereal lament, groans of misery and longing for the grave.",
    "paraphrased": "Grief, deep depression, longing for death.",
    "notes": ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"]
  },
  "F# Major": {
    "original": "Triumph over difficulty, free sigh of relief utered when hurdles are surmounted; echo of a soul which has fiercely struggled and finally conquered lies in all uses of this key.",
    "paraphrased": "Triumphant relief after struggle and hardship. Adventurous.",
    "notes": ["F#", "G#", "A#", "B", "C#", "D#", "E#", "F#"]
  },
  "F# Minor": {
    "original": "A gloomy key: it tugs at passion as a dog biting a dress. Resentment and discontent are its language.",
    "paraphrased": "Dark, passionate, filled with resentment.",
    "notes": ["F#", "G#", "A", "B", "C#", "D", "E", "F#"]
  },
  "G Major": {
    "original": "Everything rustic, idyllic and lyrical, every calm and satisfied passion, every tender gratitude for true friendship and faithful love,--in a word every gentle and peaceful emotion of the heart is correctly expressed by this key.",
    "paraphrased": "Rustic, peaceful, gratitude for love and friendship.",
    "notes": ["G", "A", "B", "C", "D", "E", "F#", "G"]
  },
  "G Minor": {
    "original": "Discontent, uneasiness, worry about a failed scheme; bad-tempered gnashing of teeth; in a word: resentment and dislike.",
    "paraphrased": "Discontent, anxiety, and resentment.",
    "notes": ["G", "A", "Bb", "C", "D", "Eb", "F", "G"]
  },
  "Ab Major": {
    "original": "Key of the grave. Death, grave, putrefaction, judgment, eternity lie in its radius.",
    "paraphrased": "Death, eternity, and judgment. Grim. Morbid.",
    "notes": ["Ab", "Bb", "C", "Db", "Eb", "F", "G", "Ab"]
  },
  "Ab Minor": {
    "original": "Grumbler, heart squeezed until it suffocates; wailing lament, difficult struggle; in a word, the color of this key is everything struggling with difficulty.",
    "paraphrased": "Struggles, wailing, and suffocating grief.",
    "notes": ["Ab", "Bb", "C", "C#", "Eb", "F", "Gb", "Ab"]
  },
  "A Major": {
    "original": "This key includes declarations of innocent love, satisfaction with one's state of affairs; hope of seeing one's beloved again when parting; youthful cheerfulness and trust in God.",
    "paraphrased": "Innocent love, contentment, and youthful hope.",
    "notes": ["A", "B", "C#", "D", "E", "F#", "G#", "A"]
  },
  "A Minor": {
    "original": "Pious virtue and tenderness of character. Sincere, but unlikely to be fulfilled",
    "paraphrased": "Tender, piety, hope, sincere, devote, devotion.",
    "notes": ["A", "B", "C", "D", "E", "F", "G", "A"]
  },
  "Bb Major": {
    "original": "Cheerful love, clear conscience, hope aspiration for a better world.",
    "paraphrased": "Cheerful love, hope for a better future.",
    "notes": ["Bb", "C", "D", "Eb", "F", "G", "A", "Bb"]
  },
  "Bb Minor": {
    "original": "A quaint creature, often dressed in the garment of night. It is somewhat surly and very seldom takes on a pleasant countenance. Mocking God and the world; discontented with itself and with everything; preparation for suicide sounds in this key.",
    "paraphrased": "Dark, discontent, mocking, sarcastic, often contemplating death.",
    "notes": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab", "Bb"]
  },
  "B Major": {
    "original": "Strongly coloured, announcing wild passions, composed from the most glaring coulors. Anger, rage, jealousy, fury, despair and every burden of the heart lies in its sphere.",
    "paraphrased": "Wild, passionate, full of anger and despair.",
    "notes": ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"]
  },
  "B Minor": {
    "original": "This is as it were the key of patience, of calm awaiting ones's fate and of submission to divine dispensation.",
    "paraphrased": "Patience, calm acceptance of fate. Stone. Stoic.",
    "notes": ["B", "C#", "D", "E", "F#", "G", "A", "B"]
  }
}

  # --- Common Chord Progressions ---
major_progressions = [
  "I - IV - V - I",
  "I - V - vi - IV",
  "I - vi - IV - V",
  "I - IV - I - V",
  "I - IV - V - vi",
  "I - iii - IV - V",
  "I - V - IV - I",
  "I - ii - V - I"
]
minor_progressions = [
  "i - iv - v",
  "i - VI - III - VII",
  "i - v - i",
  "i - iv - VII - III",
  "i - v - iv - VII",
  "i - VI - iv - V",
  "i - VII - VI - VII",
  "i - iv - III - v"
]

  # --- Modes ---
modes = {
  "Ionian": {
    "description": "Happy, bright, simple",
    "tonic positions": "I - ii - iii - IV - V - vi - vii - I"
  },
  "Dorian": {
    "description": "Bluesy, dark but optimistic",
    "tonic positions": "ii - iii - IV - V - vi - vii - I - ii"
  },
  "Phrygian": {
    "description": "Extra dark, exotic",
    "tonic positions": "iii - IV - V - vi - vii - I - ii - iii"
  },
  "Lydian": {
    "description": "Fantastical, futuristic, spacey",
    "tonic positions": "IV - V - vi - vii - I - ii - iii - IV"
  },
  "Mixolydian": {
    "description": "Even more cool, more chill",
    "tonic positions": "V - vi - vii - I - ii - iii - IV - V"
  },
  "Aeolian": {
    "description": "Dark, sad, serious, dangerous",
    "tonic positions": "vi - vii - I - ii - iii - IV - V - vi"
  }
}

def get_bpm_from_genre(genre):
  """
  Returns a random BPM within the range for the given genre
  and stores it in the global variable 'selected_bpm'.
  """
  global selected_bpm
  if genre in bpm_ranges:
    bpm_range = random.choice(bpm_ranges[genre])  # Choose a range if there are multiple
    selected_bpm = random.randint(bpm_range[0], bpm_range[1])
  else:
    selected_bpm = 120  # Default to 120 BPM if no genre found
  return selected_bpm

def get_key_from_mood(mood, threshold=1):
    """
    Returns the key and its original description associated with the given mood
    (case-insensitive and trimmed).
    """
    mood = mood.lower()  #  Converts mood to lowercase
    mood = re.sub(r'[^a-zA-Z\s]', '', mood)  # Removes non-alphabetical characters
    mood_tokens = set(mood.split())

    best_match = None
    max_overlap = 0

    for key, mood_data in key_mood_description.items():
      combined_description = f"{mood_data['original']} {mood_data['paraphrased']}".lower()
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


def display_menu():
  """Displays a menu with genre, time signature selection, and mood selection."""

  global selected_genre, selected_bpm, selected_time_signature, selected_mood

  window = tk.Tk()
  window.title("Audio Brainstorm Menu")

  # --- Genre Selection ---
  ttk.Label(window, text="Select Genre:").pack(pady=5)
  genres = ["Ambient", "Downtempo", "Breakbeat", "Disco", "House", "Techno",
            "Trance", "Electro", "Industrial", "Jungle", "Drum and Bass",
            "Hardcore", "Chiptune"]
  selected_genre = tk.StringVar(window)
  genre_combobox = ttk.Combobox(window, textvariable=selected_genre, values=genres, state="readonly")
  genre_combobox.current(0)  # Set default to Ambient
  genre_combobox.pack()

  # --- Time Signature Selection ---
  ttk.Label(window, text="Select Time Signature:").pack(pady=5)
  time_signatures = ["4/4", "3/4", "6/8", "5/4", "7/8", "12/8"]
  selected_time_signature = tk.StringVar(window)
  time_signature_combobox = ttk.Combobox(window, textvariable=selected_time_signature, values=time_signatures, state="readonly")
  time_signature_combobox.current(0)  # Set default to 4/4
  time_signature_combobox.pack()

  # --- Mood Selection ---
  ttk.Label(window, text="Select Mood:").pack(pady=5)

  mood_options = list(key_mood_description.values())

  selected_mood = tk.StringVar(window)
  mood_entry = ttk.Entry(window, textvariable=selected_mood)
  mood_entry.pack()

  listbox = tk.Listbox(window)
  listbox.pack()

  def update_listbox(event=None):
      """Updates the listbox with matching mood options."""
      typed_text = mood_entry.get().lower()
      listbox.delete(0, tk.END)  # Clear the listbox
      if typed_text:
        typed_synonyms = get_synonyms(typed_text)
        for option in mood_options:
          combined_description = f"{option['original']} {option['paraphrased']}".lower()
          if typed_text in combined_description or any(syn in combined_description for syn in typed_synonyms):
            listbox.insert(tk.END, option["paraphrased"])
  
  def fill_entry(event):
      """Fills the entry with the selected listbox item."""
      try:
        selected_index = listbox.curselection()[0]
        selected_mood.set(listbox.get(selected_index))
        listbox.delete(0, tk.END)  # Clear the listbox
      except IndexError:
        pass  # Ignore if no item is selected

  mood_entry.bind("<KeyRelease>", update_listbox)  # Bind event to update listbox
  listbox.bind("<<ListboxSelect>>", fill_entry)  # Bind event to fill entry

  # --- Mode Selection ---
  ttk.Label(window, text="Select mode:").pack(pady=5)

  mode_var = tk.StringVar(value="Ionian")

  for mode, mode_data in modes.items():
    radiobutton = ttk.Radiobutton(window, text=f"{mode} ({mode_data['description']})", variable=mode_var, value=mode)
    radiobutton.pack(anchor="w")

  def confirm_selections():
    global selected_genre, selected_bpm, selected_time_signature, selected_mood
    confirmed_genre = selected_genre.get()
    selected_genre = confirmed_genre
    selected_time_signature = selected_time_signature.get()
    selected_mood = mood_entry.get()

    selected_key, original_description, key_notes = get_key_from_mood(selected_mood)

      # Key error handling
    if selected_key is None:
      tk.messagebox.showerror("Error", "No matching key found for the selected mood.")

    if "Major" in selected_key:
      chord_progression = random.choice(major_progressions)
    else:  # Minor key
      chord_progression = random.choice(minor_progressions)

    selected_mode = mode_var.get()
    selected_bpm = get_bpm_from_genre(selected_genre)

    chord_progression_notes = [translate_roman_to_note(selected_key, roman, key_notes, is_chord=True) for roman in chord_progression.split(' - ')]

    if selected_mode in modes and "tonic positions" in modes[selected_mode]:
      tonic_positions_notes = [translate_roman_to_note(selected_key, roman, key_notes, is_chord=False) for roman in modes[selected_mode]["tonic positions"].split(' - ')]

        # Format chord progression (remove brackets and separate with hyphens)
      chord_progression_formatted = ' - '.join(chord_progression_notes)

        # Format tonic notes (removes brackets and separate with hyphens)
      tonic_positions_notes_formatted = ' - '.join(tonic_positions_notes)

        # Format mode (remove curly braces and trailing colon)
      mode_formatted = f"{selected_mode} {'Mode:':<13}"

    output = f"""
    {'Main genre: ':<20} {selected_genre}
    {'Key: ':<20} {selected_key}
    {'Key description: ':<20} {original_description}
    {'Generated BPM: ':<20} {selected_bpm}
    {'Time signature: ':<20} {selected_time_signature}
    {'Chord progression: ':<20} {chord_progression_formatted}
    {mode_formatted} {tonic_positions_notes_formatted}
    """
    print(output)  # Print the formatted output

    window.destroy()

  confirm_button = tk.Button(window, text="Confirm", command=confirm_selections)
  confirm_button.pack(pady=10)

  window.mainloop()

# Call the functions
display_welcome()
display_menu()