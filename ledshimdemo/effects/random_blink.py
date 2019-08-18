from random import randint, sample

from ledshimdemo.canvas import Canvas
from ledshimdemo.colours import Colours
from ledshimdemo.abstract_effect import AbstractEffect


class RandomBlinkEffect(AbstractEffect):
    """
    Blink a random subset of pixels.
    """

    def __init__(self, canvas: Canvas) -> None:
        # Number to blink must be within range of canvas size.
        self.__number_to_blink = (canvas.get_size() // 5) + 1
        self.__pixels = None
        super(RandomBlinkEffect, self).__init__("RandomBlink", "Some random blinking.", 0.05, canvas)

    def compose(self) -> None:
        self.__pixels = sample(range(self.canvas.get_size()), randint(1, self.__number_to_blink))
        for i in range(self.canvas.get_size()):
            if i in self.__pixels:
                self.canvas.set_pixel(i, Colours.OLDLACE)
            else:
                self.canvas.blank_pixel(i)

    def __repr__(self) -> str:
        return "RandomBlink(Blink:{0})".format(self.__pixels)
