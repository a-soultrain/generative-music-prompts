"""
This module handles the menu window output display for the project.
"""
from audio_brainstorm.modules.prompt_generation import mood_synonyms_dict
from audio_brainstorm.data.dictionaries import (
    parent_genre,
    main_genre,
    modes,
    time_signatures
)

# --- Introductory Output ---


def display_welcome():
    """Displays the welcome message for application."""
    print("\nWelcome to Play the Wrong Notes!\n")
    print("Your creative partner for generating music song prompts.")
    print("Tailored for Google Generative AI, PyTorch, pretty_MIDI, FluidSynth, Musixmatch, Spotify, and pre-defined music theory.\n")
    print("Key mood associations and data translation based on the study found here:\n")
    print("Affective Musical Key Characteristics")
    print("https://legacy.wmich.edu/mus-theo/courses/keys.html \n")
    print("pretty_midi 0.2.10")
    print("Colin Raffel and Daniel P. W. Ellis. Intuitive Analysis, Creation and Manipulation of MIDI Data with pretty_midi.")
    print("https://colinraffel.com/publications/ismir2014intuitive.pdf")
    print("In 15th International Conference on Music Information Retrieval Late Breaking and Demo Papers, 2014. \n")

# --- User Selections ---


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
                chosen_genre = genres[choice - 1]
                # --- Optional Subgenre Selection ---
                use_subgenre = input(
                    f"Would you like to specify a subgenre for {chosen_genre}? (yes/no): ").lower()
                if use_subgenre == 'y':
                    return get_subgenre(parent_genre_choice, chosen_genre)
                else:
                    return chosen_genre
        except ValueError:
            print("Invalid input. Please enter a number")


def get_subgenre(parent_genre_choice, genre):
    """Prompts the user to select a subgenre for the chosen genre."""
    print(f"\nAvailable Subgenres for {genre}:")
    subgenres = main_genre[parent_genre_choice][genre]["subgenres"]

    for i, subgenre in enumerate(subgenres):
        print(f"{i + 1}. {subgenre}")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to your desired subgenre: "))
            if 1 <= choice <= len(subgenres):
                return subgenres[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_time_signature():
    """Prompts the user to select a time signature."""
    print("\nAvailable Time Signatures:")

    for i, (signature, description) in enumerate(time_signatures.items()):
        print(f"{i + 1}. {signature} ({description})")

    while True:
        try:
            choice = int(
                input("Enter the number corresponding to your desired time signature: "))
            if 1 <= choice <= len(time_signatures):
                return list(time_signatures.keys())[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_mood():
    """Prompts the user to enter a mood and provides the best matching keys and descriptions."""
    while True:
        mood_input = input("Enter a mood (or press Enter to skip): ").lower()
        if not mood_input:
            return None, None  # Allow skipping, return None for mood and key

        input_words = set(word.lower() for word in mood_input.split())
        matching_moods = []

        for key, data in mood_synonyms_dict.items():
            if any(word in data["synonyms"] for word in input_words):
                matching_moods.append((key, data["description"]))

        if matching_moods:
            print("\nMatching Moods:")
            # Show up to 5 matches
            for i, (key, description) in enumerate(matching_moods[:5]):
                print(f"{i + 1}. {description} (Key: {key})")

            while True:
                try:
                    choice = int(
                        input("Enter the number for your desired mood: "))
                    if 1 <= choice <= len(matching_moods[:5]):
                        selected_key, selected_description = matching_moods[choice - 1]
                        return selected_description, selected_key
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
