from abstract_effect import AbstractEffect

from time import time, strftime
from math import sin
from colorsys import hsv_to_rgb


class GradientGraph(AbstractEffect):
    """
    A moving colour gradient effect determined by the height of a sine wave.
    """

    HUE_RANGE = 120
    HUE_START = 0
    MAX_BRIGHTNESS = 0.8

    def __init__(self, canvas):
        self.__t = time()
        super(GradientGraph, self).__init__("gradient_graph", 0.01, canvas)

    def show_graph(self, v, r, g, b):
        v *= self.canvas.get_size()
        for x in range(self.canvas.get_size()):
            hue = ((self.HUE_START + ((x / float(self.canvas.get_size())) * self.HUE_RANGE)) % 360) / 360.0
            r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
            if v < 0:
                brightness = 0
            else:
                brightness = min(v, 1.0) * self.MAX_BRIGHTNESS

            self.canvas.set_pixel(x, [r, g, b, brightness])
            v -= 1

    def compose(self):
        self.__t = time()
        v = (sin(self.__t * 2) + 1) / 2   # Get a value between 0 and 1
        self.show_graph(v, 255, 0, 255)  # Use it as the pixel index
        return self.canvas

    def print_compose(self):
        print("Time: {0}".format(self.__t))
