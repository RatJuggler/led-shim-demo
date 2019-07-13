from .abstract_effect import AbstractEffect

from time import localtime, strftime


class BinaryClock(AbstractEffect):
    """
    A binary clock.

    Assumes 28 LEDs giving the following layout:

    00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
    ||                         ||                         ||
    Red (hours)                ||                         ||
          32 16 08 04 02 01    ||                         ||
                               Green (minutes)            ||
                                     32 16 08 04 02 01    ||
                                                          Blue (seconds)
                                                                32 16 08 04 02 01
    """

    def __init__(self, canvas, debug):
        self.__t = localtime()
        super(BinaryClock, self).__init__("binary_clock", 1, canvas, debug)

    def compose_binary(self, n, start):
        for x in range(6):
            bit = (n & (1 << x)) > 0
            pixel = self.canvas.OLDLACE if bit else self.canvas.BLANK_PIXEL
            self.canvas.set_pixel(start - x, pixel)

    def compose(self):
        self.__t = localtime()
        self.canvas.set_pixel(0, self.canvas.RED)
        self.canvas.blank_pixel(1)
        self.compose_binary(self.__t.tm_hour, 7)
        self.canvas.blank_pixel(8)
        self.canvas.set_pixel(9, self.canvas.GREEN)
        self.canvas.blank_pixel(10)
        self.compose_binary(self.__t.tm_min, 16)
        self.canvas.blank_pixel(17)
        self.canvas.set_pixel(18, self.canvas.BLUE)
        self.canvas.blank_pixel(19)
        self.compose_binary(self.__t.tm_sec, 25)
        self.canvas.blank_pixel(26)
        self.canvas.blank_pixel(27)

    def print_debug(self):
        print("Time: {0}".format(strftime("%H:%M:%S", self.__t)))
