import logging
from time import time

import ledshim

from .effect_factory import EffectFactory


def render(effect_display: str, effect_duration: int, effect_run: int,
           invert: bool, effect_factory: EffectFactory) -> None:
    """
    Render the effects provided,
    :param effect_display: In a CYCLE or at RANDOM
    :param effect_duration: How long to display each effect for
    :param effect_run: How many times to run effects
    :param invert: Depending on which way round the Pi is
    :param effect_factory: A list of the effects to show
    :return: No meaningful return
    """
    ledshim.set_clear_on_exit()
    start_effect = time() - effect_duration
    effect = None
    try:
        while True:
            elapsed_time = time() - start_effect
            if elapsed_time > effect_duration:
                effect_run -= 1
                if effect_run < 0:
                    break
                effect = effect_factory.get_next_effect(effect_display)
                logging.info(str(effect))
                start_effect = time()
            effect.render(invert)
    except KeyboardInterrupt:
        logging.info("Execution interrupted!")
    except:
        logging.exception("Unexpected exception!")
    finally:
        ledshim.clear()
        ledshim.show()
