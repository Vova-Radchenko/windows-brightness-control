from app.brightness_service import (
    set_brightness,
    get_brightness,
    increase_brightness, 
    decrease_brightness
)
from app.constants import BRIGHTNESS_STEP


def start_cli():
    print("Brightness Control started")

    actions = {
        "1": show_current_brightness,
        "2": set_brightness_from_input,
        "3": increase_brightness_by_step,
        "4": decrease_brightness_by_step
    }

    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice in actions:
            actions[choice]()

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Unknown option")


def show_menu():
    print()
    print("1 - Show current brightness")
    print("2 - Set brightness")
    print("3 - Increase brightness")
    print("4 - Decrease brightness")
    print("5 - Exit")


def show_current_brightness():
    current_brightness = get_brightness()
    print(f"Current brightness = {current_brightness}")


def set_brightness_from_input():
    try:
        brightness = int(input("Enter brightness value: "))
        set_brightness(brightness)

    except ValueError:
        print("Please enter a valid number")


def increase_brightness_by_step():
    increase_brightness(BRIGHTNESS_STEP)


def decrease_brightness_by_step():
    decrease_brightness(BRIGHTNESS_STEP)