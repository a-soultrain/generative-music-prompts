"""
This module contains generative language models for the audio_brainstorm project.

It includes:
- google generativeai
"""
from audio_brainstorm.data.dictionaries import key_mood_description


def get_mood_from_input(mood_input):
    """
    Gets the mood from user input by directly matching against dictionary keys and values (case-insensitive).
    """
    mood_input = mood_input.lower()  # make input lowercase
    for key, value in key_mood_description.items():
        # Check if the mood input (lowercase) is in the original or paraphrased description (lowercase)
        if mood_input in value['original'].lower() or mood_input in value['paraphrased'].lower():
            return key, value['original']
    return None, None
