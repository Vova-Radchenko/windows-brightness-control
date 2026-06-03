import tkinter as tk
from tkinter import ttk, messagebox

from app.hotkeys import reload_hotkeys
from app.settings_service import (
    get_brightness_step,
    get_increase_hotkey,
    get_decrease_hotkey,
    save_settings
)


settings_window = None


def save_button_clicked(
        step_entry,
        increase_entry,
        decrease_entry
):
    try:
        brightness_step = int(step_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid value",
            "Brightness step must be a number."
        )
        return
    
    if brightness_step <= 0 or brightness_step > 100:
        messagebox.showerror(
            "Invalid value",
            "Brightness step must be between 1 and 100."
        )
        return

    settings = {
        "brightness_step": brightness_step,
        "hotkeys": {
            "increase": increase_entry.get(),
            "decrease": decrease_entry.get()
        }
    }

    save_settings(settings)
    
    reload_hotkeys()

    messagebox.showinfo(
        "Settings saved",
        "Settings were successfully updated."
    )

    print("Settings saved")


def open_settings_window():
    global settings_window

    if settings_window is not None and settings_window.winfo_exists():
        settings_window.lift()
        settings_window.focus_force()
        return

    settings_window = tk.Tk()
    settings_window.title("Brightness Control Settings")
    settings_window.geometry("360x220")
    settings_window.resizable(False, False)

    settings_window.protocol(
        "WM_DELETE_WINDOW",
        lambda: close_settings_window()
    )

    main_frame = ttk.Frame(settings_window, padding=20)
    main_frame.pack(fill="both", expand=True)

    ttk.Label(main_frame, text="Brightness step:").grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    step_entry = ttk.Entry(main_frame)
    step_entry.insert(0, str(get_brightness_step()))
    step_entry.grid(row=0, column=1, pady=5)

    ttk.Label(main_frame, text="Increase hotkey:").grid(
        row=1,
        column=0,
        sticky="w",
        pady=5
    )

    increase_entry = ttk.Entry(main_frame)
    increase_entry.insert(0, get_increase_hotkey())
    increase_entry.grid(row=1, column=1, pady=5)

    ttk.Label(main_frame, text="Decrease hotkey:").grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    decrease_entry = ttk.Entry(main_frame)
    decrease_entry.insert(0, get_decrease_hotkey())
    decrease_entry.grid(row=2, column=1, pady=5)

    ttk.Button(
        main_frame,
        text="Save",
        command=lambda: save_button_clicked(
            step_entry,
            increase_entry,
            decrease_entry
        )
    ).grid(row=3, column=0, columnspan=2, pady=20)

    settings_window.mainloop()


def close_settings_window():
    global settings_window

    if settings_window is not None:
        settings_window.destroy()
        settings_window = None