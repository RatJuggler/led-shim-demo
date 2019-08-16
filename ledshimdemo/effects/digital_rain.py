from random import randrange

from ..canvas import Canvas
from ..pixel import Pixel
from .abstract_effect import AbstractEffect


class Drop:

    def __init__(self) -> None:
        self.falling = 0
        self.trail = randrange(3, 8)
        self.intensity_step = 255 / self.trail
        self.speed = randrange(1, 3)

    def fall(self, tick: int) -> None:
        if tick % self.speed == 0.0:
            self.falling += 1
            if self.falling > (28 + self.trail):
                self.falling = 0


class DigitalRain(AbstractEffect):
    """
    A digital rain effect.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__tick = 0
        self.__drops = []
        super(DigitalRain, self).__init__("digital_rain", 0.02, canvas)

    def rain_drop(self, drop: Drop) -> None:
        intensity = 0
        for i in range(drop.trail, 0, -1):
            intensity += drop.intensity_step
            position = drop.falling - i
            if 0 <= position < 28:
                self.canvas.set_pixel(position, Pixel(0, intensity, 0))

    def compose(self) -> None:
        if randrange(10) > 8:
            self.__drops.append(Drop())
        for i in range(len(self.__drops)):
            self.rain_drop(self.__drops[i])
            self.__drops[i].fall(self.__tick)
        self.__drops = [drop for drop in self.__drops if drop.falling != 0]
        self.__tick += 1

    def __repr__(self) -> str:
        return "DigitalRain(Tick:{0})".format(self.__tick)
