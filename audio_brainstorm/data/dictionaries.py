"""
This module serves as a musical dictionary for the Play the Wrong Notes project.

It includes:
- Parent Genres, Arrangements, Common Instruments, and Characteristics
- Main Genres, BPM Ranges, and Subgenres
- Key-Mood Associations
- Major Chord Progressions
- Minor Chord Progressions
- Modes
- Time Signatures
"""

# --- Parent Genres, Arrangements, Common Instruments, Characteristics ---
parent_genre = {
    "Electronic": {
        "arrangement_options": [
            ["Intro", "Verse", "Chorus", "Breakdown", "Drop", "Outro"],
            ["Intro", "Verse", "Chorus", "Verse",
                "Chorus", "Bridge", "Chorus", "Outro"],
            ["Intro", "Loop A", "Loop B", "Breakdown", "Loop A", "Outro"]
        ],
        "common_instruments": ["Synthesizer", "Drum Machine", "Sampler", "Sequencer"],
        "defining_characteristics": ["Electronic Instruments", "Focus on Rhythmn and Groove", "Often Repetitive and Loop-Based"]
    },
    "Acoustic": {
        "arrangement_options": [
            ["Intro", "Verse", "Chorus", "Bridge", "Outro"]
        ],
        "common_instruments": ["Vocals", "Guitar", "Slide Guitar", "Bass", "Drums", "Percussion"],
        "defining_characteristics": ["Acoustic Instruments", "Focus on Melody and Harmony", "Often Song-Based"]
    }
}

# --- Main Genres ---
main_genre = {
    "Electronic": {
        "Ambient": {
            "bpm_range": (70, 120),
            "subgenres": ["Dark Ambient", "Ambient Techno", "Space Ambient", "Drone Ambient", "Environmental Ambient"]
        },
        "Downtempo": {
            "bpm_range": (70, 110),
            "subgenres": ["Trip-Hop", "Chillout", "Lounge", "Nu Jazz", "Glitch Hop"]
        },
        "Breakbeat": {
            "bpm_range": (110, 150),
            "subgenres": ["Big Beat", "Nu Skool Breaks", "Florida Breaks", "Broken Beat", "Jungle Breaks"]
        },
        "House": {
            "bpm_range": (110, 140),
            "subgenres": ["Deep House", "Tech House", "Progressive House", "Electro House", "Acid House", "Soulful House"]
        },
        "Techno": {
            "bpm_range": (110, 160),
            "subgenres": ["Detroit Techno", "Minimal Techno", "Acid Techno", "Dub Techno", "Hard Techno"]
        },
        "Trance": {
            "bpm_range": (110, 150),
            "subgenres": ["Progressive Trance", "Psytrance", "Uplifting Trance", "Tech Trance", "Vocal Trance", "Hard Trance"]
        },
        "Electro": {
            "bpm_range": (120, 140),
            "subgenres": ["Electroclash", "Freestyle Techno", "Electro House", "Dubstep Electro", "Electro Swing"]
        },
        "Industrial": {
            "bpm_range": (130, 150),
            "subgenres": ["Electronic Body Music", "Industrial Metal", "Power Noise", "Martial Industrial", "Dark Ambient Industrial", "Cyber Industrial"]
        },
        "Jungle": {
            "bpm_range": (150, 170),
            "subgenres": ["Dark Jungle", "Liquid Jungle", "Jump Up Jungle", "Neurofunk Jungle", "Ragga Jungle", "90s Game Station Jungle"]
        },
        "Drum and Bass": {
            "bpm_range": (160, 180),
            "subgenres": ["Liquid Drum and Bass", "Neurofunk", "Jump Up Drum and Bass", "Darkstep", "Techstep", "Jungle Drum and Bass"]
        },
        "Hardcore": {
            "bpm_range": (90, 300),
            "subgenres": ["Gabber", "Happy Hardcore", "UK Hardcore", "Industrial Hardcore", "Terrorcore", "Freeform Hardcore"]
        },
        "Chiptune": {
            "bpm_range": (80, 200),
            "sungenres": ["Bitpop", "8-bit Hardcore", "80s Video Game Chiptune", "Demoscene Chiptune", "Chillwave", "Video Game Music"]
        }
    }
}


# --- Affective Musical Key Characteristics ---
key_mood_description = {
    "C Major": {
        "original": "Completely Pure. Its character is: innocence, simplicity, naivety, children's talk.",
        "paraphrased": "Pure, innocent, naive, simplicity.",
        "notes": ["C", "D", "E", "F", "G", "A", "B"]
    },
    "C Minor": {
        "original": "Declaration of love and at the same time the lament of unhappy love. All languishing, longing, sighing of the love-sick soul lies in this key.",
        "paraphrased": "Love's declaration and lament for lost love-longing and heartache.",
        "notes": ["C", "D", "Eb", "F", "G", "Ab", "Bb"]
    },
    "Db Major": {
        "original": "A leering key, degenerating into grief and rapture. It cannot laugh, but it can smile; it cannot howl, but it can at least grimace its crying. Consequently only unusual characters and feelings can be brought out in this key.",
        "paraphrased": "A strange key, balancing between grief and jow, with unusual emotions. Enigma.",
        "notes": ["Db", "Eb", "F", "G", "Ab", "Bb", "C"]
    },
    "C# Minor": {
        "original": "Penitential lamentation, intimate conversation with God, the friend and help-meet of life; sighs of disappointed friendship and love lie in its radius.",
        "paraphrased": "Sorrowful prayers, disappointed love and friendship.",
        "notes": ["C#", "D#", "E", "F#", "G#", "A", "B"]
    },
    "D Major": {
        "original": "The key of triumph, of Hallejuahs, of war-cries, of victory-rejoicing. Thus, the inviting symphonies, the marches, holiday songs and heaven-rejoicing choruses are set in this key.",
        "paraphrased": "Triumphant, victorious, filled with joy and celebration. Ceremony",
        "notes": ["D", "E", "F#", "G", "A", "B", "C#"]
    },
    "D Minor": {
        "original": "Melancholy womanliness, the spleen and humours brood.",
        "paraphrased": "Melancholy, sadness, gloom.",
        "notes": ["D", "E", "F", "G", "A", "Bb", "C"]
    },
    "Eb Major": {
        "original": "The key of love, of devotion, of intimate conversation with God.",
        "paraphrased": "Devotion, love, and spiritual connection. Religion or religious.",
        "notes": ["Eb", "F", "G", "Ab", "Bb", "C", "D"]
    },
    "D# Minor": {
        "original": "Feelings of the anxiety of the soul's deepest distress, of brooding despair, of blackest depresssion, of the most gloomy condition of the soul. Every fear, every hesitation of the shuddering heart, breathes out of horrible D# minor. If ghosts could speak, their speech would approximate this key.",
        "paraphrased": "Deep despair, soul-crushing anxiety and fear.",
        "notes": ["D#", "E#", "F#", "G#", "A#", "B", "C#"]
    },
    "E Major": {
        "original": "Noisy shouts of joy, laughing pleasure and not yet complete, full delight lies in E Major.",
        "paraphrased": "Joyous, cheerful, but not fully content. Complacent.",
        "notes": ["E", "F#", "G#", "A", "B", "C#", "D#"]
    },
    "E Minor": {
        "original": "Naive, innocent declaration of love, lament without grumbling; sighs accompanied by few tears; this key speaks of the imminent hope of resolving in the pure happiness of C major.",
        "paraphrased": "Innocent love, gentle lament, with hope for happiness. Happy.",
        "notes": ["E", "F#", "G", "A", "B", "C", "D"]
    },
    "F Major": {
        "original": "Complaisance & Calm.",
        "paraphrased": "Calm and agreeable.",
        "notes": ["F", "G", "A", "Bb", "C", "D", "E"]
    },
    "F Minor": {
        "original": "Deep depression, funereal lament, groans of misery and longing for the grave.",
        "paraphrased": "Grief, deep depression, longing for death.",
        "notes": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"]
    },
    "F# Major": {
        "original": "Triumph over difficulty, free sigh of relief utered when hurdles are surmounted; echo of a soul which has fiercely struggled and finally conquered lies in all uses of this key.",
        "paraphrased": "Triumphant relief after struggle and hardship. Adventurous.",
        "notes": ["F#", "G#", "A#", "B", "C#", "D#", "E#"]
    },
    "F# Minor": {
        "original": "A gloomy key: it tugs at passion as a dog biting a dress. Resentment and discontent are its language.",
        "paraphrased": "Dark, passionate, filled with resentment.",
        "notes": ["F#", "G#", "A", "B", "C#", "D", "E"]
    },
    "G Major": {
        "original": "Everything rustic, idyllic and lyrical, every calm and satisfied passion, every tender gratitude for true friendship and faithful love,--in a word every gentle and peaceful emotion of the heart is correctly expressed by this key.",
        "paraphrased": "Rustic, peaceful, gratitude for love and friendship.",
        "notes": ["G", "A", "B", "C", "D", "E", "F#"]
    },
    "G Minor": {
        "original": "Discontent, uneasiness, worry about a failed scheme; bad-tempered gnashing of teeth; in a word: resentment and dislike.",
        "paraphrased": "Discontent, anxiety, and resentment.",
        "notes": ["G", "A", "Bb", "C", "D", "Eb", "F"]
    },
    "Ab Major": {
        "original": "Key of the grave. Death, grave, putrefaction, judgment, eternity lie in its radius.",
        "paraphrased": "Death, eternity, and judgment. Grim. Morbid.",
        "notes": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"]
    },
    "Ab Minor": {
        "original": "Grumbler, heart squeezed until it suffocates; wailing lament, difficult struggle; in a word, the color of this key is everything struggling with difficulty.",
        "paraphrased": "Struggles, wailing, and suffocating grief.",
        "notes": ["Ab", "Bb", "C", "C#", "Eb", "F", "Gb"]
    },
    "A Major": {
        "original": "This key includes declarations of innocent love, satisfaction with one's state of affairs; hope of seeing one's beloved again when parting; youthful cheerfulness and trust in God.",
        "paraphrased": "Innocent love, contentment, and youthful hope.",
        "notes": ["A", "B", "C#", "D", "E", "F#", "G#"]
    },
    "A Minor": {
        "original": "Pious virtue and tenderness of character. Sincere, but unlikely to be fulfilled",
        "paraphrased": "Tender, piety, hope, sincere, devote, devotion.",
        "notes": ["A", "B", "C", "D", "E", "F", "G"]
    },
    "Bb Major": {
        "original": "Cheerful love, clear conscience, hope aspiration for a better world.",
        "paraphrased": "Cheerful love, hope for a better future.",
        "notes": ["Bb", "C", "D", "Eb", "F", "G", "A"]
    },
    "Bb Minor": {
        "original": "A quaint creature, often dressed in the garment of night. It is somewhat surly and very seldom takes on a pleasant countenance. Mocking God and the world; discontented with itself and with everything; preparation for suicide sounds in this key.",
        "paraphrased": "Dark, discontent, mocking, sarcastic, often contemplating death.",
        "notes": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"]
    },
    "B Major": {
        "original": "Strongly coloured, announcing wild passions, composed from the most glaring coulors. Anger, rage, jealousy, fury, despair and every burden of the heart lies in its sphere.",
        "paraphrased": "Wild, passionate, full of anger and despair.",
        "notes": ["B", "C#", "D#", "E", "F#", "G#", "A#"]
    },
    "B Minor": {
        "original": "This is as it were the key of patience, of calm awaiting ones's fate and of submission to divine dispensation.",
        "paraphrased": "Patience, calm acceptance of fate. Stone. Stoic.",
        "notes": ["B", "C#", "D", "E", "F#", "G", "A"]
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

# --- Time Signatures ---
time_signatures = {"4/4", "3/4", "6/8", "5/4", "7/8", "12/8"}
