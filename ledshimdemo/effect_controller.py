from typing import List


class EffectController:

    def __init__(self, parade: str, duration: int, repeat: int, brightness: int,
                 invert: bool, effects: List[str]) -> None:
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
