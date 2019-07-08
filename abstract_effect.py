from abc import ABC, abstractmethod


class AbstractEffect(ABC):
    def __init__(self, name, canvas):
        self.name = name
        self.canvas = canvas
        super().__init__()

    def print_name(self):
        print("Effect: {0}".format(self.name))

    @abstractmethod
    def compose(self):
        pass

    @abstractmethod
    def print_compose(self):
        pass
