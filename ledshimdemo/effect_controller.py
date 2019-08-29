from typing import List

from .canvas import Canvas
from .effect_cache import EffectCache
from .configure_logging import logging
from .effect_parade import AbstractEffectParade
from .pixel import Pixel


class EffectController:

    def __init__(self, parade: str, duration: int, repeat: int, brightness: int,
                 invert: bool, effects: List[str], effect_cache: EffectCache) -> None:
        """
        Initialise with chosen options.
        :param parade: In a CYCLE or at RANDOM
        :param duration: How long to display each effect for
        :param repeat: How many times to run the effects
        :param brightness: How bright the effects will be
        :param invert: Depending on which way round the Pi is
        :param effects: User entered list of effects to use, defaults to all effects
        :param canvas: Virtual display used by effects
        :param effect_cache: Of all available effects
        """
        self.parade = parade
        self.duration = duration
        self.repeat = repeat
        self.brightness = brightness
        self.invert = invert
        self.effects = effects
        self.effect_cache = effect_cache

    def options_used(self, command: str) -> str:
        """
        Human readable string showing the display options to be used.
        :param command: the command using these options
        :return: One line string of the display options to be used
        """
        options = ["{0}(".format(command),
                   "parade={0}, ".format(self.parade),
                   "duration={0} secs, ".format(self.duration),
                   "repeat={0}, ".format(self.repeat),
                   "brightness={0}, ".format(self.brightness),
                   "invert={0}, ".format(self.invert),
                   "effects={0}".format(self.effects if self.effects else "ALL"),
                   ")"]
        return "".join(options)

    def process(self, command: str):
        logging.info(self.options_used(command))
        Pixel.set_default_brightness(self.brightness / 10.0)
        if self.invert:
            Canvas.invert_display()
        instances = self.effect_cache.get_effect_instances(self.effects)
        effects_parade = AbstractEffectParade.select_effect_parade(self.parade, instances)
        effects_parade.render(self.duration, self.repeat)
