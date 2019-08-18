from ..canvas import Canvas
from ..colours import Colours
from ..effects import AbstractEffect


class SolidColoursEffect(AbstractEffect):
    """
    A basic effect which just shows a sequence of solid colours.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__colour = 0
        super(SolidColoursEffect, self).__init__("SolidColours", "A sequence of solid colours.", 0.5, canvas)

    def compose(self) -> None:
        self.canvas.set_all(Colours.COLOURS[self.__colour])
        self.__colour = (self.__colour + 1) % len(Colours.COLOURS)

    def __repr__(self) -> str:
        return "SolidColours(Step:{0})".format(self.__colour)
