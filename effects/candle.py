from .abstract_effect import AbstractEffect

from colorsys import hsv_to_rgb
import numpy as np


class Candle(AbstractEffect):
    """
    A candle in the wind.
    """

    CANDLE_SIZE = 7

    def __init__(self, canvas, debug):
        self.__flame_size = 0
        self.__FLAME_MAX = canvas.get_size() - self.CANDLE_SIZE
        self.__from_hue = 60 / float(canvas.get_size())
        super(Candle, self).__init__("candle", 0.01, canvas, debug)

    def show_candle(self, size):
        for i in range(size):
            self.canvas.set_pixel(i, self.canvas.OLDLACE)

    def get_flame_size(self, max_size):
        n = np.random.choice(np.random.noncentral_chisquare(max_size / 2, 0.1, 1000), 1)
        flame_size = int(n[0])
        if flame_size > max_size:
            flame_size = max_size
        return flame_size

    def show_flame(self, size):
        for i in range(size):
            hue = self.__from_hue * i
            r, g, b = [int(c * 255) for c in hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
            self.canvas.set_pixel(self.CANDLE_SIZE + i, [r, g, b, 1])

    def compose(self):
        self.canvas.set_all(self.canvas.BLANK_PIXEL)
        self.show_candle(self.CANDLE_SIZE)
        self.__flame_size = self.get_flame_size(self.__FLAME_MAX)
        self.show_flame(self.__flame_size)

    def print_debug(self):
        print("Flame: {0}".format(self.__flame_size))