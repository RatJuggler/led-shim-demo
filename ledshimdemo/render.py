import logging
from random import randint
from time import sleep

import ledshim

from abstract_effect import AbstractEffect


def get_next_effect_no(effect_display: str, num_effects: int, effect_no: int):
    if effect_display == "CYCLE":
        return (effect_no + 1) % num_effects
    if effect_display == "RANDOM":
        return randint(0, num_effects)
    raise ValueError("Unknown effect_display type!")


def copy_to_shim(effect: AbstractEffect, invert: bool):
    for i in range(effect.canvas.get_size()):
        pixel = effect.canvas.get_pixel(i)
        position = (effect.canvas.get_size() - 1 - i) if invert else i
        ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())


def render(effect_display: str, effect_duration: int, effect_run: int, invert: bool, effects: list):
    """
    Render the effects provided,
    :param effect_display: In a CYCLE or at RANDOM
    :param effect_duration: How long to display each effect for
    :param effect_run: How many times to run effects
    :param invert: Depending on which way round the Pi is
    :param effects: A list of the effects to show
    :return: No meaningful return
    """
    ledshim.set_clear_on_exit()
    show_time = 0
    effect_no = len(effects) - 1
    effect: AbstractEffect = effects[effect_no]
    try:
        while effect_run >= 0:
            if show_time <= 0:
                effect_run -= 1
                effect_no = get_next_effect_no(effect_display, len(effects), effect_no)
                effect = effects[effect_no]
                show_time = effect_duration / effect.get_speed()
                logging.info(str(effect))
            effect.compose()
            logging.info(repr(effect))
            logging.debug(repr(effect.canvas))
            copy_to_shim(effect, invert)
            ledshim.show()
            show_time -= 1
            sleep(effect.get_speed())
    except KeyboardInterrupt:
        ledshim.clear()
        ledshim.show()
