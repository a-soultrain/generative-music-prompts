"""
This module contains generative language models for the audio_brainstorm project.

It includes:
- nltk
- wordnet
- google generativeai
"""
import os
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
from audio_brainstorm.data.dictionaries import key_mood_description

# Initialize the lemmatizer once globally
lemmatizer = WordNetLemmatizer()


def get_synonyms(word):
    """Generates synonyms for a given word, handling different parts of speech."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonym = lemma.name().replace('_', ' ')
            # Lemmatize based on the word's part of speech in the description
            if syn.pos() == 'v':  # Verb
                synonym = lemmatizer.lemmatize(synonym, 'v')
            elif syn.pos() in ('n', 'a'):  # Noun or Adjective
                synonym = lemmatizer.lemmatize(synonym)
            synonyms.add(synonym)
    return synonyms


def generate_mood_synonym_dict(mood_dict):
    mood_synonyms = {}
    for key, value in mood_dict.items():
        synonyms = set()
        description = f"{value['original']} {value['paraphrased']}"
        for word in description.split():
            synonyms.update(get_synonyms(word))
        # Store original description with synonyms
        mood_synonyms[key] = {"synonyms": synonyms,
                              "description": value['original']}
    return mood_synonyms


# Generate the mood synonym dictionary once when the script starts
mood_synonyms_dict = generate_mood_synonym_dict(key_mood_description)


def get_mood_from_input(mood_input):
    input_words = set(word.lower() for word in mood_input.split())
    for key, data in mood_synonyms_dict.items():
        if any(word in data["synonyms"] for word in input_words):
            return key, data["description"]  # Return stored description
    return None, None
