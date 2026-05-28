import tkinter as tk
from tkinter import ttk


overlay_window = None
overlay_label = None
overlay_close_timer = None
overlay_progressbar = None


def show_overlay(brightness_value):
    global overlay_window
    global overlay_label
    global overlay_close_timer
    global overlay_progressbar

    if overlay_window is None:
        return
    
    overlay_label.config(text=f"☀ {brightness_value}%")

    overlay_progressbar["value"] = brightness_value

    overlay_window.deiconify()

    if overlay_close_timer is not None:
        overlay_window.after_cancel(overlay_close_timer)

    overlay_close_timer = overlay_window.after(2000, hide_overlay)


def close_overlay():
    global overlay_window
    global overlay_label
    global overlay_close_timer

    if overlay_window is not None:
        overlay_window.destroy()
        overlay_window = None
        overlay_label = None
        overlay_close_timer = None


def start_overlay_loop():
    global overlay_window
    global overlay_label
    global overlay_progressbar

    overlay_window = tk.Tk()

    overlay_window.overrideredirect(True)
    overlay_window.attributes("-topmost", True)

    screen_width = overlay_window.winfo_screenwidth()
    screen_height = overlay_window.winfo_screenheight()

    window_width = 300
    window_height = 130

    x = screen_width - window_width - 20
    y = screen_height - window_height - 60

    overlay_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    overlay_window.configure(bg="#1E1E1E")

    overlay_label = tk.Label(
        overlay_window,
        font = ("Segoe UI", 24, "bold"),
        fg = "white",
        bg = "#1E1E1E",
        padx = 20,
        pady = 10
    )

    overlay_label.pack(expand=True)

    overlay_progressbar = ttk.Progressbar(
        overlay_window,
        orient="horizontal",
        length=220,
        mode="determinate",
        maximum=100
    )

    overlay_progressbar.pack(pady=(0,15))

    overlay_window.withdraw()
    overlay_window.mainloop()


def hide_overlay():
    global overlay_window
    global overlay_close_timer

    if overlay_window is not None:
        overlay_window.withdraw()

    overlay_close_timer = None