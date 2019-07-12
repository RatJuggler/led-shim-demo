

class Canvas:
    """
    Abstract representation of a line of LEDs.

    Each pixel is composed of the list: [r, g, b, brightness]
    """

    def __init__(self, size):
        self.__canvas = [None] * size

    def get_pixel(self, p):
        return self.__canvas[p]

    def set_pixel(self, p, pixel):
        self.__canvas[p] = pixel

    def set_all(self, pixel):
        for i in range(self.get_size()):
            self.set_pixel(i, pixel)

    def get_size(self):
        return self.__canvas.__len__()

    def print_canvas(self):
        for i in range(self.get_size()):
            print("{0:2d} = {1}".format(i, self.get_pixel(i)))

