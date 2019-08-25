from random import randint

# Supported display options:
# Cycle - go through the selected effects in order.
# Random - out of the selected effects pick one at random each time.
CYCLE_DISPLAY = "CYCLE"
RANDOM_DISPLAY = "RANDOM"


def get_display_options():
    return [CYCLE_DISPLAY, RANDOM_DISPLAY]


def get_default_option():
    return CYCLE_DISPLAY


def select_effect_display(effect_display: str):
    assert effect_display in (CYCLE_DISPLAY, RANDOM_DISPLAY), \
        "Effect display must be {0} or {1}!".format(CYCLE_DISPLAY, RANDOM_DISPLAY)
    if effect_display == CYCLE_DISPLAY:
        return next_cycle_effect
    if effect_display == RANDOM_DISPLAY:
        return next_random_effect


def next_cycle_effect(previous_effect: int, effects_selected: int):
    return (previous_effect + 1) % effects_selected


def next_random_effect(previous_effect: int, effects_selected: int):
    return randint(0, effects_selected - 1)
