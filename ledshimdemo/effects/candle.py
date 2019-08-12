from colorsys import hsv_to_rgb
import numpy as np

from ..colours import Colours
from ..pixel import Pixel
from .abstract_effect import AbstractEffect


class Candle(AbstractEffect):
    """
    A candle in the wind.
    """

    def __init__(self, canvas):
        self.__CANDLE_SIZE = canvas.get_size() // 2
        self.__FLAME_MAX = canvas.get_size() - self.__CANDLE_SIZE
        self.__flame_size = 0
        # Flame hue goes from 0 (red) to 60 (yellow).
        self.__HUE_SPACING = 60 / float(self.__FLAME_MAX)
        super(Candle, self).__init__("candle", 0.01, canvas)

    def show_candle(self, size):
        for i in range(size):
            self.canvas.set_pixel(i, Colours.OLDLACE)

    @staticmethod
    def get_flame_size(max_size):
        n = np.random.choice(np.random.noncentral_chisquare(max_size / 2, 0.1, 1000), 1)
        flame_size = int(n[0])
        if flame_size > max_size:
            flame_size = max_size
        return flame_size

    def show_flame(self, size):
        for i in range(size):
            hue = self.__HUE_SPACING * i
            pixel = [int(c * 255) for c in hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
            self.canvas.set_pixel(self.__CANDLE_SIZE + i, Pixel.from_tuple(pixel))

    def compose(self):
        self.canvas.clear_all()
        self.show_candle(self.__CANDLE_SIZE)
        self.__flame_size = self.get_flame_size(self.__FLAME_MAX)
        self.show_flame(self.__flame_size)

    def __repr__(self):
        return "Candle(Candle Size:{0}, Flame Size:{0})".format(self.__CANDLE_SIZE, self.__flame_size)
