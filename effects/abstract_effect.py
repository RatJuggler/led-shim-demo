from abc import ABC, abstractmethod


class AbstractEffect(ABC):
    """
    An abstract class which forms the basis of all effects.
    """

    def __init__(self, name, speed, canvas, debug):
        self.__name = name
        self.__speed = speed
        self.canvas = canvas
        self.__debug = debug
        super().__init__()

    def print_name(self):
        print("Effect: {0}".format(self.__name))

    def get_speed(self):
        return self.__speed

    def is_debug(self):
        return self.__debug

    @abstractmethod
    def compose(self):
        pass

    @abstractmethod
    def print_debug(self):
        pass
