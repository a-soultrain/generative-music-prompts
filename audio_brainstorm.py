import tkinter as tk

def display_welcome():
  """Displays the welcome message for the Audio Brainstorm Gem."""
  print("\nWelcome to Audio Brainstorm!\n")
  print("Your creative partner for generating electronic music song prompts.")
  print("Tailored for Ableton Live 12 Standard Edition, Novation Launchpad X, Splice, and Xfer Serum.\n")

def display_genre_selection():
  """Displays a dropdown menu for genre selection."""

  window = tk.Tk()
  window.title("Genre Selection")

  genres = ["Lofi PS1 Jungle", "Liquid Drum & Bass", "Dreamy/Poppy Drum & Bass"]

  selected_genre = tk.StringVar(window)
  selected_genre.set(genres[0]) # default value

  genre_dropdown = tk.OptionMenu(window, selected_genre, *genres)
  genre_dropdown.pack()

  def confirm_genre():
    print(f"Selected genre: {selected_genre.get()}")
    window.destroy()  # Close the window after selection

  confirm_button = tk.Button(window, text="Confirm", command=confirm_genre)
  confirm_button.pack()

  window.mainloop()


# Call the functions
display_welcome()
display_genre_selection()