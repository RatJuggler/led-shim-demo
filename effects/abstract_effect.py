from abc import ABC, abstractmethod


class AbstractEffect(ABC):
    """
    An abstract class which forms the basis of all effects.
    """

    def __init__(self, name, speed, canvas, debug=False):
        self.__name = name
        self.__speed = speed
        self.canvas = canvas
        self.__debug = debug
        super().__init__()

    def get_name(self):
        return self.__name

    def get_speed(self):
        return self.__speed

    def is_debug(self):
        return self.__debug

    def __str__(self):
        return "Effect: {0}".format(self.get_name())

    @abstractmethod
    def compose(self):
        pass
