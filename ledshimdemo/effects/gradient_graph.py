from colorsys import hsv_to_rgb
from math import sin
from time import time

from ledshimdemo.canvas import Canvas
from ledshimdemo.pixel import Pixel
from ledshimdemo.abstract_effect import AbstractEffect


class GradientGraphEffect(AbstractEffect):
    """
    A moving colour gradient effect determined by the height of a sine wave.
    """

    HUE_RANGE = 120
    HUE_START = 180

    def __init__(self, canvas: Canvas) -> None:
        self.__v = 0
        self.__HUE_SPACING = self.HUE_RANGE / canvas.get_size()
        super(GradientGraphEffect, self).__init__("GradientGraph", "Sine wave colour gradient effect.", 0.01, canvas)

    def show_graph(self, v: int) -> None:
        for i in range(self.canvas.get_size()):
            offset = self.__HUE_SPACING * i
            hue = (self.HUE_START + offset) % 360
            pixel = [int(c * 255) for c in hsv_to_rgb(hue / 360.0, 1.0, 1.0)]
            if v < 0:
                pixel.append(0)
            self.canvas.set_pixel(i, Pixel.from_tuple(pixel))
            v -= 1

    def compose(self) -> None:
        self.__v = round((sin(time() * 2) + 1) / 2, 8)        # Get the next point on the graph, a value between 0 and 1
        self.show_graph(self.__v * self.canvas.get_size())    # Scale to the graph height to show.

    def __repr__(self) -> str:
        return "GradientGraph(Height:{0})".format(self.__v)
