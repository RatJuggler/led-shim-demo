from typing import List

from .abstract_effect import AbstractEffect
from .canvas import Canvas
from .configure_logging import logging
from .effect_parade import AbstractEffectParade
from .pixel import Pixel


class EffectController:

    def __init__(self, parade: str, duration: int, repeat: int,
                 brightness: int, invert: bool, effects: List[str]) -> None:
        """
        Initialise with chosen options.
        :param parade: In a CYCLE or at RANDOM
        :param duration: How long to display each effect for
        :param repeat: How many times to run the effects
        :param brightness: How bright the effects will be
        :param invert: Depending on which way round the Pi is
        :param effects: User entered list of effects to use, defaults to all effects
        """
        self.parade = parade
        self.duration = duration
        self.repeat = repeat
        self.brightness = brightness
        self.invert = invert
        self.effects = effects

    @classmethod
    def from_dict(cls, options: dict) -> 'EffectController':
        """
        Instantiate from a dict.
        :return: an EffectController instance
        """
        return EffectController(options["parade"],
                                options["duration"],
                                options["repeat"],
                                options["brightness"],
                                options["invert"],
                                options["effects"])

    def encode_options_used(self) -> dict:
        """
        Encode the current effect options.
        :return: a dict of effect options
        """
        return dict(parade=self.parade,
                    duration=self.duration,
                    repeat=self.repeat,
                    brightness=self.brightness,
                    invert=self.invert,
                    effects=self.effects)

    def options_used(self) -> str:
        """
        Human readable string showing the display options to be used.
        :return: One line string of the display options to be used
        """
        options = ["Effect Options(",
                   "parade={0}, ".format(self.parade),
                   "duration={0} secs, ".format(self.duration),
                   "repeat={0}, ".format(self.repeat),
                   "brightness={0}, ".format(self.brightness),
                   "invert={0}, ".format(self.invert),
                   "effects={0}".format(self.effects if self.effects else "ALL"),
                   ")"]
        return "".join(options)

    def process(self, instances: List[AbstractEffect]) -> None:
        logging.info(self.options_used())
        Pixel.set_default_brightness(self.brightness / 10.0)
        if self.invert:
            Canvas.invert_display()
        effects_parade = AbstractEffectParade.select_effect_parade(self.parade, instances)
        effects_parade.render(self.duration, self.repeat)
