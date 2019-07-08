from abstract_effect import AbstractEffect


class SolidColours(AbstractEffect):
    def __init__(self, canvas):
        self.__step = 0
        super(SolidColours, self).__init__("solid_colours", canvas)

    def compose(self):
        if self.__step == 0:
            self.canvas.set_all([128, 0, 0, 1])
        if self.__step == 1:
            self.canvas.set_all([0, 128, 0, 1])
        if self.__step == 2:
            self.canvas.set_all([0, 0, 128, 1])

        self.__step += 1
        self.__step %= 3

        return self.canvas

    def print_compose(self):
        print("Step: {0}".format(self.__step))
