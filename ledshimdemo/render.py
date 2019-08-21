import logging
from random import randint
from time import sleep
from typing import List

import ledshim

from .abstract_effect import AbstractEffect


def get_next_effect(effect_display: str, effects: List[AbstractEffect]) -> AbstractEffect:
    """
    Pick the next effect to display.
    :param effect_display: In a CYCLE or at RANDOM
    :param effects: A list of the effects to show
    :return: The next effect to show
    """
    if "effect_no" not in get_next_effect.__dict__:  # Dynamically add tracker if not already defined.
        get_next_effect.effect_no = -1
    if effect_display == "CYCLE":
        get_next_effect.effect_no = (get_next_effect.effect_no + 1) % len(effects)
    if effect_display == "RANDOM":
        get_next_effect.effect_no = randint(0, len(effects) - 1)
    return effects[get_next_effect.effect_no]


def copy_to_shim(effect: AbstractEffect, invert: bool) -> None:
    """
    Display the effect canvas on the shim.
    :param effect: being shown
    :param invert: Orientation of the display
    :return: No meaningful return
    """
    for i in range(effect.canvas.get_size()):
        pixel = effect.canvas.get_pixel(i)
        position = (effect.canvas.get_size() - 1 - i) if invert else i
        ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
    ledshim.show()


def render(effect_display: str, effect_duration: int, effect_run: int,
           invert: bool, effects: List[AbstractEffect]) -> None:
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
    effect = effects[0]
    try:
        while True:
            if show_time <= 0:
                effect_run -= 1
                if effect_run < 0:
                    break
                effect = get_next_effect(effect_display, effects)
                show_time = effect_duration / effect.get_speed()
                logging.info(str(effect))
            effect.compose()
            logging.verbose(repr(effect))
            logging.debug(repr(effect.canvas))
            copy_to_shim(effect, invert)
            show_time -= 1
            sleep(effect.get_speed())
    except KeyboardInterrupt:
        logging.info("Execution interrupted!")
    except:
        logging.exception("Unexpected exception!")
    finally:
        ledshim.clear()
        ledshim.show()
