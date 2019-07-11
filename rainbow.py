from abstract_effect import AbstractEffect

from time import time
from colorsys import hsv_to_rgb


class Rainbow(AbstractEffect):
    """
    A slowly changing rainbow.
    """

    SPACING = 360.0 / 16.0
    BRIGHTNESS = 0.8

    def __init__(self, canvas):
        self.__hue = 0
        super(Rainbow, self).__init__("rainbow", 0.0001, canvas)

    def show_rainbow(self, hue):
        for x in range(self.canvas.get_size()):
            offset = x * self.SPACING
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in hsv_to_rgb(h, 1.0, 1.0)]
            self.canvas.set_pixel(x, [r, g, b, self.BRIGHTNESS])

    def compose(self):
        self.__hue = int(time() * 100) % 360
        self.show_rainbow(self.__hue)

    def print_compose(self):
        print("Hue: {0}".format(self.__hue))
