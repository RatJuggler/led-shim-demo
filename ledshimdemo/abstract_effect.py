from abc import ABC, abstractmethod

from ledshimdemo.canvas import Canvas


class AbstractEffect(ABC):
    """
    An abstract class which forms the basis of all effects.

    Effects inheriting this class must implement the "compose()" function and render their display onto the virtual
    canvas. They must also override the "__repr__" function to provide details on internal state.
    """

    def __init__(self, name: str, description: str, speed: float, canvas: Canvas) -> None:
        """
        Initialise the effect properties.
        :param name: of the effect
        :param description: of the effect
        :param speed: of the effect, in seconds or fractions thereof
        :param canvas: on which the effect should draw
        """
        self.__name = name
        self.__description = description
        self.__speed = speed
        self.canvas = canvas
        super().__init__()

    def get_name(self) -> str:
        """
        The name of the effect.
        :return: The effect name
        """
        return self.__name

    def get_description(self) -> str:
        """
        A description of the effect.
        :return: The effect description
        """
        return self.__description

    def get_speed(self) -> float:
        """
        The speed of the effect, that is the time between updates to the effect.
        :return: The effect speed
        """
        return self.__speed

    def __str__(self) -> str:
        """
        Builds a simple string representation of the effect instance.
        :return: Human readable string representation of the object instance
        """
        return "Effect: {0} - {1} Speed: {2}".format(self.get_name(), self.get_description(), self.get_speed())

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def compose(self) -> None:
        pass   # pragma: no cover
