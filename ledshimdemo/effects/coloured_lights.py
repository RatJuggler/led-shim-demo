from ..colours import Colours
from .abstract_effect import AbstractEffect


class ColouredLights(AbstractEffect):
    """
    Simple coloured lights like Xmas lights.
    """

    __LIGHT_COLOURS = [Colours.RED, Colours.GREEN, Colours.BLUE, Colours.WHITE]
    __NUM_COLOURS = len(__LIGHT_COLOURS)

    def __init__(self, canvas):
        assert 28 % self.__NUM_COLOURS == 0, "The number of colours to be used must be a factor of 28!"
        self.__light = 0
        super(ColouredLights, self).__init__("colour_procession", 0.5, canvas)

    def show_lights(self, light):
        for i in range(7):
            offset = (i * self.__NUM_COLOURS) + light
            self.canvas.set_pixel(offset, self.__LIGHT_COLOURS[light])

    def compose(self):
        self.canvas.clear_all()
        self.show_lights(self.__light)
        self.__light = (self.__light + 1) % self.__NUM_COLOURS

    def __repr__(self):
        return "ColouredLights(Light:{0})".format(self.__light)
