from .abstract_effect import AbstractEffect
from pixel import Pixel

from time import time
from colorsys import hsv_to_rgb


class Rainbow(AbstractEffect):
    """
    A slowly moving rainbow.
    """

    def __init__(self, canvas, debug):
        self.__SPACING = 360.0 / canvas.get_size()
        self.__base_hue = 0
        super(Rainbow, self).__init__("rainbow", 0.01, canvas, debug)

    def show_rainbow(self, base_hue):
        for x in range(self.canvas.get_size()):
            offset = x * self.__SPACING
            hue = ((base_hue + offset) % 360) / 360.0
            pixel = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
            self.canvas.set_pixel(x, Pixel.from_tuple(pixel))

    def compose(self):
        self.__base_hue = int(time() * 100) % 360
        self.show_rainbow(self.__base_hue)

    def print_debug(self):
        print("Base Hue: {0}".format(self.__base_hue))
