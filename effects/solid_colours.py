from .abstract_effect import AbstractEffect


class SolidColours(AbstractEffect):
    """
    A basic effect which just shows a sequence of solid colours.
    """

    def __init__(self, canvas, debug):
        self.__step = 0
        super(SolidColours, self).__init__("solid_colours", 0.5, canvas, debug)

    def compose(self):
        if self.__step == 0:
            self.canvas.set_all([128, 0, 0, 1])
        if self.__step == 1:
            self.canvas.set_all([0, 128, 0, 1])
        if self.__step == 2:
            self.canvas.set_all([0, 0, 128, 1])

        self.__step += 1
        self.__step %= 3

    def print_debug(self):
        print("Step: {0}".format(self.__step))
