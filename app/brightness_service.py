import screen_brightness_control as sbc


def set_brightness(value):
    if value > 100:
        value = 100
    
    elif value < 0:
        value = 0

    sbc.set_brightness(value)

    print(f"Brightness set to: {value}")

    return value


def get_brightness():
    return sbc.get_brightness()[0] #We currently only support one monitor.


def calculate_rounded_brightness(current_brightness, step, increase):
    if increase:
        return(current_brightness // step + 1) * step
    
    return ((current_brightness - 1) // step) * step


def increase_brightness(step, round_to_step=False):
    current_brightness = get_brightness()

    if round_to_step:
        new_brightness = calculate_rounded_brightness(
            current_brightness,
            step,
            True
        )
    else:
        new_brightness = current_brightness + step

    return set_brightness(new_brightness)


def decrease_brightness(step, round_to_step=False):
    current_brightness = get_brightness()

    if round_to_step:
        new_brightness = calculate_rounded_brightness(
            current_brightness,
            step,
            False
        )
    else:
        new_brightness = current_brightness - step

    return set_brightness(new_brightness)