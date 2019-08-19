from ledshimdemo.canvas import Canvas
from ledshimdemo.abstract_effect import AbstractEffect


class Dummy2Effect(AbstractEffect):
    """
    A dummy effect.
    """

    def __init__(self, canvas: Canvas) -> None:
        self.__colour = 0
        super(Dummy2Effect, self).__init__("Dummy2Effect", "A dummy effect.", 1, canvas)

    def compose(self) -> None:
        pass

    def __repr__(self) -> str:
        return "Dummy2Effect()"
