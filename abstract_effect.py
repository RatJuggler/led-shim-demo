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

    def print_name(self):
        print("Effect: {0}".format(self.__name))

    def get_speed(self):
        return self.__speed

    @abstractmethod
    def compose(self):
        pass

    @abstractmethod
    def print_compose(self):
        pass
