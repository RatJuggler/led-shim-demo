from colorsys import hsv_to_rgb
import numpy as np

from ledshimdemo.canvas import Canvas
from ledshimdemo.colours import Colours
from ledshimdemo.pixel import Pixel
from ledshimdemo.abstract_effect import AbstractEffect


class CandleEffect(AbstractEffect):
    """
    A candle in the wind.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__CANDLE_SIZE = canvas.get_size() // 2
        self.__FLAME_MAX = canvas.get_size() - self.__CANDLE_SIZE
        self.__flame_size = 0
        # Flame hue goes from 0 (red) to 60 (yellow).
        self.__HUE_SPACING = 60 / float(self.__FLAME_MAX)
        super(CandleEffect, self).__init__("Candle", "A flickering candle.", 0.01, canvas)

    def show_candle(self, size: int) -> None:
        for i in range(size):
            self.canvas.set_pixel(i, Colours.OLDLACE)

    @staticmethod
    def get_flame_size(max_size: int) -> int:
        n = np.random.choice(np.random.noncentral_chisquare(max_size / 2, 0.1, 1000), 1)
        flame_size = int(n[0])
        return max_size if flame_size > max_size else flame_size

    def show_flame(self, size: int) -> None:
        for i in range(size):
            hue = self.__HUE_SPACING * i
            pixel = [int(c * 255) for c in hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
            self.canvas.set_pixel(self.__CANDLE_SIZE + i, Pixel.from_tuple(pixel))

    def compose(self) -> None:
        self.canvas.clear_all()
        self.show_candle(self.__CANDLE_SIZE)
        self.__flame_size = self.get_flame_size(self.__FLAME_MAX)
        self.show_flame(self.__flame_size)

    def __repr__(self) -> str:
        return "Candle(Candle Size:{0}, Flame Size:{0})".format(self.__CANDLE_SIZE, self.__flame_size)
