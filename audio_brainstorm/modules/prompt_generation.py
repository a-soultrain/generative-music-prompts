"""
This module contains generative language models for the audio_brainstorm project.

It includes:
- nltk
- wordnet
- google generativeai
"""
import nltk
from nltk.corpus import wordnet


def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace(' - ', ' '))
    return synonyms
