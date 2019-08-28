from typing import List


class EffectSettings:

    def __init__(self, parade: str, duration: int, repeat: int, brightness: int,
                 invert: bool, effects: List[str]) -> None:
        self.parade = parade
        self.duration = duration
        self.repeat = repeat
        self.brightness = brightness
        self.invert = invert
        self.effects = effects
