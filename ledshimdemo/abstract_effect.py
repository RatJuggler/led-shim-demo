from abc import ABC, abstractmethod

from ledshimdemo.canvas import Canvas


class AbstractEffect(ABC):
    """
    An abstract class which forms the basis of all effects.
    """

    def __init__(self, name: str, description: str, speed: float, canvas: Canvas) -> None:
        self.__name = name
        self.__description = description
        self.__speed = speed
        self.canvas = canvas
        super().__init__()

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_speed(self) -> float:
        return self.__speed

    def __str__(self) -> str:
        return "Effect: {0}, Speed: {1}".format(self.get_name(), self.get_speed())

    @abstractmethod
    def compose(self) -> None:
        pass   # pragma: no cover
