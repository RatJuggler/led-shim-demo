import logging
from time import time

import ledshim

from .effect_factory import EffectFactory


def render(effect_display: str, effect_duration: int, effect_run: int,
           invert: bool, effect_factory: EffectFactory) -> None:
    """
    Render the effects selected,
    :param effect_display: In a CYCLE or at RANDOM
    :param effect_duration: How long to display each effect for
    :param effect_run: How many times to run effects
    :param invert: Depending on which way round the Pi is
    :param effect_factory: Determines the effects to show
    :return: No meaningful return
    """
    ledshim.set_clear_on_exit()
    try:
        for i in range(effect_run):
            for j in range(effect_factory.get_count_effects_selected()):
                effect = effect_factory.get_next_effect(effect_display)
                start_effect = time()
                while (time() - start_effect) < effect_duration:
                    effect.render(invert)
    except KeyboardInterrupt:
        logging.info("Execution interrupted!")
    finally:
        ledshim.clear()
        ledshim.show()
