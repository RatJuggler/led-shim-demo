from abc import ABC, abstractmethod

from ledshimdemo.canvas import Canvas


class AbstractEffect(ABC):
    """
    An abstract class which forms the basis of all effects.

    Effects inheriting this class must implement the "compose()" function and compose their display onto the virtual
    canvas each time the function is called. They must also override the "__repr__" function to provide details on their
    internal state at that time.
    """

    def __init__(self, name: str, description: str, update_frequency: float, canvas: Canvas) -> None:
        """
        Initialise the effect properties.
        :param name: of the effect
        :param description: of the effect
        :param update_frequency: of the effect, in seconds or fractions thereof
        :param canvas: on which the effect should compose
        """
        self.__name = name
        self.__description = description
        self.__update_frequency = update_frequency
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

    def get_update_frequency(self) -> float:
        """
        The time between updates to the effect.
        :return: The effect update frequency
        """
        return self.__update_frequency

    def __str__(self) -> str:
        """
        Builds a simple string representation of the effect instance.
        :return: Human readable string representation of the object instance
        """
        return "Effect: {0} - {1} Update Frequency: {2} secs"\
            .format(self.get_name(), self.get_description(), self.get_update_frequency())

    @abstractmethod
    def __repr__(self) -> str:
        pass   # pragma: no cover

    @abstractmethod
    def compose(self) -> None:
        pass   # pragma: no cover
