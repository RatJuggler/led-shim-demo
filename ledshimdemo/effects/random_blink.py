from random import randint, sample

from ..colours import Colours
from .abstract_effect import AbstractEffect


class RandomBlink(AbstractEffect):
    """
    Blink a random subset of pixels.
    """

    def __init__(self, canvas):
        self.__pixels = None
        super(RandomBlink, self).__init__("random_blink", 0.05, canvas)

    def compose(self):
        self.__pixels = sample(range(self.canvas.get_size()), randint(1, 5))
        for i in range(self.canvas.get_size()):
            if i in self.__pixels:
                self.canvas.set_pixel(i, Colours.OLDLACE)
            else:
                self.canvas.blank_pixel(i)

    def __repr__(self):
        return "RandomBlink(Blink:{0})".format(self.__pixels)
