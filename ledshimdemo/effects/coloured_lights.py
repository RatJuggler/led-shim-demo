from ..colours import Colours
from .abstract_effect import AbstractEffect


class ColouredLights(AbstractEffect):
    """
    Simple coloured lights like Xmas lights.
    """

    __LIGHT_COLOURS = [Colours.RED, Colours.GREEN, Colours.BLUE, Colours.WHITE]

    @staticmethod
    def factors(n: int):
        result = set()
        for i in range(1, int(n ** 0.5) + 1):
            div, mod = divmod(n, i)
            if mod == 0:
                result |= {i, div}
        return result

    @classmethod
    def get_num_colours(cls, canvas_size: int) -> int:
        factors = cls.factors(canvas_size)
        for i in range(len(cls.__LIGHT_COLOURS), 1, -1):
            if i in factors:
                return i
        return 1

    def __init__(self, canvas):
        self.__NUM_COLOURS = self.get_num_colours(canvas.get_size())
        self.__NUM_SETS = canvas.get_size() // self.__NUM_COLOURS
        self.__colour = 0  # type: int
        super(ColouredLights, self).__init__("coloured_lights", 0.5, canvas)

    def show_lights(self, light: int):
        for i in range(self.__NUM_SETS):
            offset = (i * self.__NUM_COLOURS) + light
            self.canvas.set_pixel(offset, self.__LIGHT_COLOURS[light])

    def compose(self):
        self.canvas.clear_all()
        self.show_lights(self.__colour)
        self.__colour = (self.__colour + 1) % self.__NUM_COLOURS

    def __repr__(self):
        return "ColouredLights(Number Colours:{0}, Colour:{1})".format(self.__NUM_COLOURS, self.__colour)
