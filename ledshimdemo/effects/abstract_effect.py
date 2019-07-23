from abc import ABC, abstractmethod


class AbstractEffect(ABC):
    """
    An abstract class which forms the basis of all effects.
    """

    def __init__(self, name, speed, canvas):
        self.__name = name
        self.__speed = speed
        self.canvas = canvas
        super().__init__()

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return "Effect: {0}, Speed: {1}".format(self.get_name(), self.get_speed())

    @abstractmethod
    def compose(self):
        pass
