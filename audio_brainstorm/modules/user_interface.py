"""
This module handles the menu window output display for the project.
"""
from audio_brainstorm.modules.prompt_generation import get_synonyms
from audio_brainstorm.data.dictionaries import (
    parent_genre,
    main_genre,
    key_mood_description,
    modes,
    time_signatures
)

# --- Introductory Output ---


def display_welcome():
    """Displays the welcome message for the Audio Brainstorm Gem."""
    print("\nWelcome to Play the Wrong Notes!\n")
    print("Your creative partner for generating music song prompts.")
    print("Tailored for Google Generative AI, pretty_MIDI, Musixmatch, Spotify, and pre-defined music theory.\n")
    print("Key mood associations and data translation based on the study found here:\n")
    print("Affective Musical Key Characteristics")
    print("https://legacy.wmich.edu/mus-theo/courses/keys.html \n")
    print("pretty_midi 0.2.10")
    print("Colin Raffel and Daniel P. W. Ellis. Intuitive Analysis, Creation and Manipulation of MIDI Data with pretty_midi.")
    print("https://colinraffel.com/publications/ismir2014intuitive.pdf")
    print("In 15th International Conference on Music Information Retrieval Late Breaking and Demo Papers, 2014. \n")


def get_parent_genre():
    """Prompts the user to select parent genres."""
    print("Select a Genre Branch: ")
    branches = list(parent_genre.keys())

    for i, branch in enumerate(branches):
        print(f"{i + 1}. {branch}")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to your desired branch: "))
            if 1 <= choice <= len(branches):
                return branches[choice - 1]
        except ValueError:
            print("Invalid input. Please enter a number")


def get_main_genre(parent_genre_choice):
    """Prompts the user to select a genre based on the chosen parent genre."""
    print("Available Genres:")
    genres = list(main_genre[parent_genre_choice].keys())

    for i, genre in enumerate(genres):
        print(f"{i + 1}. {genre}")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to your desired genre: "))
            if 1 <= choice <= len(genres):
                return genres[choice - 1]
        except ValueError:
            print("Invalid input. Please enter a number")


def get_time_signature():
    """Prompts the user to select a time signature."""
    print("\nAvailable Time Signatures:")

    for i, signature in enumerate(time_signatures):
        print(f"{i + 1}. {signature}")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to your desired time signature: "))
            if 1 <= choice <= len(time_signatures):
                return list(time_signatures)[choice - 1]
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_mood():
    """Prompts the user to enter a mood and provides suggestions."""
    mood_options = list(key_mood_description.values())
    while True:
        mood_input = input("Enter a mood (or press Enter to skip): ").lower()
        if not mood_input:
            return None  # Allow skipping mood selection

        suggestions = []
        typed_synonyms = get_synonyms(mood_input)
        for option in mood_options:
            combined_description = f"{option['original']} {
                option['paraphrased']}".lower()
            if mood_input in combined_description or any(syn in combined_description for syn in typed_synonyms):
                suggestions.append(option["paraphrased"])

        if suggestions:
            print("\nHere are some suggestions based on your input:")
            for i, suggestion in enumerate(suggestions):
                print(f"{i+1}. {suggestion}")

            while True:
                try:
                    choice = int(
                        input("Enter the number for the best match (or 0 for none): "))
                    if 0 <= choice <= len(suggestions):
                        if choice == 0:
                            return mood_input  # Use the original input
                        else:
                            return suggestions[choice - 1]
                    else:
                        print("Invalid choice. Please enter a number from the list.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("No matching moods found. Please try again.")


def get_mode():
    """Prompts the user to select a mode from the terminal."""
    print("\nAvailable Modes:")
    for i, (mode, mode_data) in enumerate(modes.items()):
        print(f"{i+1}. {mode} ({mode_data['description']})")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to your desired mode: "))
            if 1 <= choice <= len(modes):
                return list(modes.keys())[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_output(output_data):
    """Displays the generated output data in the terminal."""
    print("\n----- Generated Song Prompt -----\n")
    for key, value in output_data.items():
        print(f"{key}: {value}")
