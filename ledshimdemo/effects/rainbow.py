from colorsys import hsv_to_rgb
from time import time

from ledshimdemo.canvas import Canvas
from ledshimdemo.pixel import Pixel
from ledshimdemo.abstract_effect import AbstractEffect


class RainbowEffect(AbstractEffect):
    """
    A slowly moving rainbow.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__HUE_SPACING = 360.0 / canvas.get_size()
        self.__base_hue = 0
        super(RainbowEffect, self).__init__("Rainbow", "A slowly moving rainbow.", 0.01, canvas)

    def show_rainbow(self, base_hue: int) -> None:
        for i in range(self.canvas.get_size()):
            offset = self.__HUE_SPACING * i
            hue = (base_hue + offset) % 360
            pixel = [int(c * 255) for c in hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
            self.canvas.set_pixel(i, Pixel.from_tuple(pixel))

    def compose(self) -> None:
        self.__base_hue = int(time() * 100) % 360  # Sync with time to move the rainbow.
        self.show_rainbow(self.__base_hue)

    def __repr__(self) -> str:
        return "Rainbow(Base Hue:{0})".format(self.__base_hue)
