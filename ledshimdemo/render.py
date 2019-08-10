import logging
from random import randint
from time import sleep

import ledshim

from abstract_effect import AbstractEffect


def render(show_effects: str, effects: list, effect_time: int, invert: bool):
    """
    Render the effects provided,
    :param show_effects: In a CYCLE or at RANDOM
    :param effects: A list of the effects to show
    :param effect_time: How long to display each effect for
    :param invert: Depending on which way round the Pi is
    :return: No meaningful return
    """
    ledshim.set_clear_on_exit()
    show_time = 0
    effect_no = len(effects) - 1
    effect: AbstractEffect = effects[effect_no]
    try:
        while True:
            if show_time <= 0:
                if show_effects == "CYCLE":
                    effect_no = (effect_no + 1) % len(effects)
                if show_effects == "RANDOM":
                    effect_no = randint(0, len(effects))
                effect = effects[effect_no]
                show_time = effect_time / effect.get_speed()
                logging.info(str(effect))
            effect.compose()
            logging.info(repr(effect))
            logging.debug(repr(effect.canvas))
            for i in range(effect.canvas.get_size()):
                pixel = effect.canvas.get_pixel(i)
                position = (effect.canvas.get_size() - 1 - i) if invert else i
                ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
            ledshim.show()
            show_time -= 1
            sleep(effect.get_speed())
    except KeyboardInterrupt:
        pass
        ledshim.clear()
        ledshim.show()
