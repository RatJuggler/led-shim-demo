from ledshimdemo.canvas import Canvas
from ledshimdemo.abstract_effect import AbstractEffect


class Dummy1Effect(AbstractEffect):
    """
    A dummy effect.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__colour = 0
        super(Dummy1Effect, self).__init__("Dummy1Effect", "A dummy effect 1.", 1, canvas)

    def compose(self) -> None:
        pass   # pragma: no cover

    def __repr__(self) -> str:
        return "Dummy1Effect()"   # pragma: no cover
