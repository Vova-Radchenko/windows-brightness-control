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


def increase_brightness(step):
    current_brightness = get_brightness()
    new_brightness = current_brightness + step

    return set_brightness(new_brightness)



def decrease_brightness(step):
    current_brightness = get_brightness()
    new_brightness = current_brightness - step

    return set_brightness(new_brightness)