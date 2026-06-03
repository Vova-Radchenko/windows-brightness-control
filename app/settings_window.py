import tkinter as tk
from tkinter import messagebox

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
    settings_window.geometry("420x400")
    settings_window.resizable(False, False)
    settings_window.configure(bg="#262626")

    settings_window.protocol(
        "WM_DELETE_WINDOW",
        lambda: close_settings_window()
    )

    # main_frame = tk.Frame(
    #     settings_window,
    #     bg="#151515",
    #     padx=30,
    #     pady=30
    # )
    
    # main_frame.pack(
    #     fill="both",
    #     expand=True,
    #     padx=40,
    #     pady=30
    # )
    # main_frame.grid_columnconfigure(0, weight=1)

    content_frame = tk.Frame(
        settings_window,
        bg="#262626",
        padx=20,
        pady=25
    )

    content_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )
    content_frame.grid_columnconfigure(0, weight=1)

    tk.Label(
        content_frame,
        text="Settings",
        bg="#252525",
        fg="white",
        font=("Segoe UI", 16, "bold")
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=(0, 4)
    )

    tk.Label(
        content_frame,
        text="Configure brightness step and keyboard shortcuts.",
        bg="#252525",
        fg="#B8B8B8",
        font=("Segoe UI", 9)
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=(0, 20)
    )

    tk.Label(
        content_frame,
        text="Brightness step:",
        bg="#252525",
        fg="white",
        font=("Segoe UI", 10, "bold")
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=(0, 6)
    )

    step_entry = tk.Entry(
        content_frame,
        bg="#2B2B2B",
        fg="white",
        insertbackground="white",
        relief="flat",
        font=("Segoe UI", 10),
        width=30,
        highlightthickness=1,
        highlightbackground="#3A3A3A",
        highlightcolor="#4CC2FF",
        cursor="xterm",
    )
    step_entry.insert(0, str(get_brightness_step()))
    step_entry.grid(
        row=3,
        column=0,
        sticky="ew",
        pady=(0, 14)
    )

    tk.Label(
        content_frame,
        text="Increase hotkey:",
        bg="#252525",
        fg="white",
        font=("Segoe UI", 10, "bold")
    ).grid(
        row=4,
        column=0,
        sticky="w",
        pady=(0, 6)
    )

    increase_entry = tk.Entry(
        content_frame,
        bg="#2B2B2B",
        fg="white",
        insertbackground="white",
        relief="flat",
        font=("Segoe UI", 10),
        width=30,
        highlightthickness=1,
        highlightbackground="#3A3A3A",
        highlightcolor="#4CC2FF",
        cursor="xterm"
    )
    increase_entry.insert(0, get_increase_hotkey())
    increase_entry.grid(
        row=5,
        column=0,
        sticky="ew",
        pady=(0, 14)
    )

    tk.Label(
        content_frame,
        text="Decrease hotkey:",
        bg="#252525",
        fg="white",
        font=("Segoe UI", 10, "bold")
    ).grid(
        row=6,
        column=0,
        sticky="w",
        pady=(0, 6)
    )

    decrease_entry = tk.Entry(
        content_frame,
        bg="#2B2B2B",
        fg="white",
        insertbackground="white",
        relief="flat",
        font=("Segoe UI", 10),
        width=30,
        highlightthickness=1,
        highlightbackground="#3A3A3A",
        highlightcolor="#4CC2FF",
        cursor="xterm"
    )
    decrease_entry.insert(0, get_decrease_hotkey())
    decrease_entry.grid(
        row=7,
        column=0,
        sticky="ew",
        pady=(0, 14)
    )

    tk.Button(
        content_frame,
        text="Save",
        command=lambda: save_button_clicked(
            step_entry,
            increase_entry,
            decrease_entry
        ),
        bg="#3B82F6",
        fg="white",
        activebackground="#2563EB",
        activeforeground="white",
        relief="flat",
        font=("Segoe UI", 10, "bold"),
        padx=16,
        pady=6,
        cursor="hand2",
        borderwidth=0
    ).grid(
        row=8,
        column=0,
        sticky="e",
        pady=(18, 0)
    )

    settings_window.mainloop()


def close_settings_window():
    global settings_window

    if settings_window is not None:
        settings_window.destroy()
        settings_window = None