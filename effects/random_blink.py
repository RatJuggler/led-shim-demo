from .abstract_effect import AbstractEffect
from colours import Colours

import random


class RandomBlink(AbstractEffect):
    """
    Blink a random subset of pixels.
    """

    def __init__(self, canvas, debug=False):
        self.__pixels = None
        super(RandomBlink, self).__init__("random_blink", 0.05, canvas, debug)

    def compose(self):
        self.__pixels = random.sample(range(self.canvas.get_size()), random.randint(1, 5))
        for i in range(self.canvas.get_size()):
            if i in self.__pixels:
                self.canvas.set_pixel(i, Colours.OLDLACE)
            else:
                self.canvas.blank_pixel(i)

    def __repr__(self):
        return "RandomBlink(Blink:{0})".format(self.__pixels)


