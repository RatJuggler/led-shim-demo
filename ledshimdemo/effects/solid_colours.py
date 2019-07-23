from ..colours import Colours
from .abstract_effect import AbstractEffect


class SolidColours(AbstractEffect):
    """
    A basic effect which just shows a sequence of solid colours.
    """

    def __init__(self, canvas):
        self.__colour = 0
        super(SolidColours, self).__init__("solid_colours", 0.5, canvas)

    def compose(self):
        self.canvas.set_all(Colours.COLOURS[self.__colour])
        self.__colour = (self.__colour + 1) % len(Colours.COLOURS)

    def __repr__(self):
        return "SolidColours(Step:{0})".format(self.__colour)
