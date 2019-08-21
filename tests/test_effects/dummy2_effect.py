from ledshimdemo.canvas import Canvas
from ledshimdemo.colours import Colours
from ledshimdemo.abstract_effect import AbstractEffect


class Dummy2Effect(AbstractEffect):
    """
    A dummy effect.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__colour = 0
        super(Dummy2Effect, self).__init__("Dummy2Effect", "A dummy effect 2.", 0.5, canvas)

    def compose(self) -> None:
        self.canvas.set_all(Colours.GREEN)

    def __repr__(self) -> str:
        return "Dummy2Effect(GREEN)"   # pragma: no cover
