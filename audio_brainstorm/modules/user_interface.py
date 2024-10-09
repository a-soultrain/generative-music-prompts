"""
This module handles the menu window output display for the project.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

from audio_brainstorm.modules.prompt_generation import get_synonyms
from audio_brainstorm.data.dictionaries import (
    key_mood_description,
    modes
)

# --- Main Window


def create_main_window():
    window = tk.Tk()
    window.title("Audio Brainstorm Menu")
    window.geometry("600x700")  # Adjust size, as needed
    return window

    # --- Genre Selection ---


def create_genre_selection(window):
    genre_frame = ttk.LabelFrame(window, text="Genre Selection")
    genre_frame.pack(fill="x", padx=10, pady=5)

    ttk.Label(genre_frame, text="Select Genre:").pack(pady=5)
    genres = ["Ambient", "Downtempo", "Breakbeat", "Disco", "House", "Techno",
              "Trance", "Electro", "Industrial", "Jungle", "Drum and Bass",
              "Hardcore", "Chiptune"]
    selected_genre = tk.StringVar(window)
    genre_combobox = ttk.Combobox(
        window, textvariable=selected_genre, values=genres, state="readonly")
    genre_combobox.current(0)  # Set default to Ambient
    genre_combobox.pack(pady=5, padx=10)

    # --- Time Signature Selection


def create_time_signature_selection(window):
    time_signature_frame = ttk.LabelFrame(
        window, text="Time Signature Selection")
    time_signature_frame.pack(fill="x", padx=10, pady=5)

    ttk.Label(time_signature_frame, text="Select Time Signature:").pack(pady=5)
    time_signatures = ["4/4", "3/4", "6/8", "5/4", "7/8", "12/8"]
    selected_time_signature = tk.StringVar(window)
    time_signature_combobox = ttk.Combobox(
        window, textvariable=selected_time_signature, values=time_signatures, state="readonly")
    time_signature_combobox.current(0)  # Set default to 4/4
    time_signature_combobox.pack(pady=5, padx=10)

    # --- Mood Selection


def create_mood_selection(window):
    mood_frame = ttk.LabelFrame(window, text="Mood Selection")
    mood_frame.pack(fill="both", padx=10, pady=5, expand=True)

    ttk.Label(mood_frame, text="Select Mood:").pack(pady=5)

    mood_options = list(key_mood_description.values())

    selected_mood = tk.StringVar(window)
    mood_entry = ttk.Entry(mood_frame, textvariable=selected_mood)
    mood_entry.pack(pady=5, padx=10, fill="x")

    listbox = tk.Listbox(mood_frame, height=5)
    listbox.pack(pady=5, padx=10, fill="both", expand=True)

    def update_listbox(event=None):
        """Updates the listbox with matching mood options."""
        typed_text = mood_entry.get().lower()
        listbox.delete(0, tk.END)  # Clear the listbox
        if typed_text:
            typed_synonyms = get_synonyms(typed_text)
            for option in mood_options:
                combined_description = f"{option['original']} {
                    option['paraphrased']}".lower()
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

        # Bind event to update listbox
    mood_entry.bind("<KeyRelease>", update_listbox)
    listbox.bind("<<ListboxSelect>>", fill_entry)  # Bind event to fill entry

    # --- Mode Selection


def create_mood_selection(window):
    mode_frame = ttk.LabelFrame(window, text="Mode Selection")
    mode_frame.pack(fill="x", padx=10, pady=5)

    ttk.Label(mode_frame, text="Select mode:").pack(pady=5)

    mode_var = tk.StringVar(value="Ionian")

    for mode, mode_data in modes.items():
        radiobutton = ttk.Radiobutton(mode_frame, text=f"{
                                      mode} ({mode_data['description']})", variable=mode_var, value=mode)
        radiobutton.pack(anchor="w", padx=10, pady=2)

    # --- Create Output Display ---


def create_output_display(window):
    output_frame = ttk.LabelFrame(window, text="Generated Prompt")
    output_frame.pack(fill="both", padx=10, pady=5, expand=True)

    output_text = scrolledtext.ScrolledText(
        output_frame, wrap=tk.WORD, state='disabled', height=15)
    output_text.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

    output_frame.columnconfigure(0, weight=1)
    output_frame.rowconfigure(0, weight=1)

    # --- Confirm Button ---
    confirm_button = ttk.Button(
        window, text="Generate Prompt", command=confirm_selections)
    confirm_button.pack(pady=10)

    # --- Output Display ---
    output_frame = ttk.LabelFrame(window, text="Generated Prompt")
    output_frame.pack(fill="both", padx=10, pady=5, expand=True)

    output_text = scrolledtext.ScrolledText(
        output_frame, wrap=tk.WORD, state='disabled', height=15)
    output_text.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

    output_frame.columnconfigure(0, weight=1)
    output_frame.rowconfigure(0, weight=1)

    # --- Toggle Editing Button ---
    def toggle_editable():
        if output_text.cget('state') == 'disabled':
            output_text.configure(state='normal')
            toggle_button.configure(text="Lock Editing")
        else:
            output_text.configure(state='disabled')
            toggle_button.configure(text="Unlock Editing")

    toggle_button = ttk.Button(
        window, text="Unlock Editing", command=toggle_editable)
    toggle_button.grid(row=4, column=0, pady=5)

    # --- Export Button ---
    export_button = ttk.Button(window, text="Export Prompt",
                               command=lambda: export_prompt(output_text.get(1.0, tk.END)))
    export_button.grid(row=5, column=0, pady=5)

    window.mainloop()


def export_prompt(output):
    """Exports the generated prompt to a text file."""
    try:
        with open('generated_prompt.txt', 'w') as file:
            file.write(output)
        messagebox.showinfo(
            "Exported", "Prompt exported to generated_prompt.txt")
    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to export prompt: {e}")


def visualize_chord_progression(chord_progression_notes):
    """Visualizes the chord progression using Tkinter Canvas"""
    vis_window = tk.Toplevel()
    vis_window.title("Chord Progression Visualization")
    vis_window.geometry("600x100")
    canvas = tk.Canvas(vis_window, width=600, height=100)
    canvas.pack()

    # Simple horizontal layout of chords
    x_start = 50
    y = 50
    spacing = 80

    for chord in chord_progression_notes:
        canvas.create_rectangle(
            x_start, y - 20, x_start + 60, y + 20, fill="lightblue")
        canvas.create_text(x_start + 30, y, text=chord)
        x_start += spacing
