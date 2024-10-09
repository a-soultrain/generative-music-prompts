"""
This module serves as a music dictionary for the audio_brainstorm project.

It includes:
- BPM Ranges
- Key-Mood Associations
- Major Chord Progressions
- Minor Chord Progressions
- Modes
"""
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
