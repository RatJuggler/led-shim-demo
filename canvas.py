from pixel import Pixel


class Canvas:
    """
    Abstract representation of a line of LEDs.

    Each pixel is composed of: [r, g, b, brightness]
    """

    __BLANK_PIXEL = Pixel(0, 0, 0, 0)

    def __init__(self, size):
        self.__canvas = [None] * size

    def get_pixel(self, p):
        return self.__canvas[p]

    def set_pixel(self, p, pixel):
        self.__canvas[p] = pixel

    def blank_pixel(self, p):
        self.set_pixel(p, self.__BLANK_PIXEL)

    def clear_all(self):
        self.set_all(self.__BLANK_PIXEL)

    def set_all(self, pixel):
        for i in range(self.get_size()):
            self.set_pixel(i, pixel)

    def get_size(self):
        return self.__canvas.__len__()

    def __repr__(self):
        canvas = ["Canvas("]
        for i in range(self.get_size()):
            canvas.append("[{0:2d}, {1}]".format(i, repr(self.get_pixel(i))))
        canvas.append(")")
        return "\n".join(canvas)
