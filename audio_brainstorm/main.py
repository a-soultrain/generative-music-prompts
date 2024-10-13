from audio_brainstorm.modules.user_interface import (
    display_welcome,
    get_user_genre,
    get_user_time_signature,
    get_user_mood,
    get_user_mode,
    display_output
)


def main():
    display_welcome()
    genre = get_user_genre()
    time_signature = get_user_time_signature()
    mood = get_user_mood()
    mode = get_user_mode()

    output_data = {
        "Genre": genre,
        "Time Signature": time_signature,
        "Mood": mood,
        "Mode": mode
    }

    display_output(output_data)


if __name__ == "__main__":
    main()
