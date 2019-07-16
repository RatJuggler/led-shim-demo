from .abstract_effect import AbstractEffect

import random


class RandomBlink(AbstractEffect):
    """
    Blink a random subset of pixels.
    """

    def __init__(self, canvas, debug):
        self.__pixels = None
        super(RandomBlink, self).__init__("random_blink", 0.05, canvas, debug)

    def compose(self):
        self.__pixels = random.sample(range(self.canvas.get_size()), random.randint(1, 5))
        for i in range(self.canvas.get_size()):
            if i in self.__pixels:
                self.canvas.set_pixel(i, self.canvas.OLDLACE)
            else:
                self.canvas.set_pixel(i, self.canvas.BLANK_PIXEL)

    def __repr__(self):
        return "RandomBlink(Blink:{0})".format(self.__pixels)


