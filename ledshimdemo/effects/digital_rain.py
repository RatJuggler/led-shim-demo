from random import randrange

from ledshimdemo.canvas import Canvas
from ledshimdemo.pixel import Pixel
from ledshimdemo.abstract_effect import AbstractEffect


class Drop:

    def __init__(self, start: int) -> None:
        self.falling = start
        self.trail = randrange(3, 8)
        self.intensity_step = 255 // self.trail
        self.speed = randrange(1, 3)

    def fall(self, tick: int) -> None:
        if tick % self.speed == 0:
            self.falling -= 1

    def __repr__(self) -> str:
        return "Drop(Falling:{0}, Trail:{1}, IntensityStep:{2}, Speed:{3})".format(self.falling, self.trail, self.intensity_step, self.speed)


class DigitalRainEffect(AbstractEffect):
    """
    A digital rain effect.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__tick = 0
        self.__drops = []
        super(DigitalRainEffect, self).__init__("DigitalRain", "Cut price Matrix effect.", 0.02, canvas)

    def rain_drop(self, drop: Drop) -> None:
        intensity = 255
        for i in range(drop.trail):
            position = drop.falling + i
            if 0 <= position < self.canvas.get_size():
                self.canvas.set_pixel(position, Pixel(0, intensity, 0))
            intensity -= drop.intensity_step

    def compose(self) -> None:
        self.canvas.clear_all()
        if len(self.__drops) == 0 or randrange(10) > 8:
            self.__drops.append(Drop(self.canvas.get_size() - 1))
        for i in range(len(self.__drops)):
            self.rain_drop(self.__drops[i])
            self.__drops[i].fall(self.__tick)
        self.__drops = [drop for drop in self.__drops if drop.falling + drop.trail >= 0]
        self.__tick += 1

    def __repr__(self) -> str:
        return "DigitalRain(Tick:{0}, Drops:{1})".format(self.__tick, self.__drops)
