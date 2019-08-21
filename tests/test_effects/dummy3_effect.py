from ledshimdemo.canvas import Canvas
from ledshimdemo.colours import Colours
from ledshimdemo.abstract_effect import AbstractEffect


class Dummy3Effect(AbstractEffect):
    """
    A dummy effect.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__colour = 0
        super(Dummy3Effect, self).__init__("Dummy3Effect", "A dummy effect 3.", 0.25, canvas)

    def compose(self) -> None:
        self.canvas.set_all(Colours.BLUE)

    def __repr__(self) -> str:
        return "Dummy3Effect(BLUE)"   # pragma: no cover
