from pixel import Pixel


class Canvas:
    """
    Abstract representation of a line of LEDs.

    Each pixel is composed of: [r, g, b, brightness]
    """

    BLANK_PIXEL = Pixel(0, 0, 0, 0)
    RED     = Pixel(255, 0, 0)
    GREEN   = Pixel(0, 255, 0)
    BLUE    = Pixel(0, 0, 255)
    CYAN    = Pixel(0, 255, 255)
    WHITE   = Pixel(255, 255, 255)
    OLDLACE = Pixel(253, 245, 230)
    PURPLE  = Pixel(128, 0, 128)
    MAGENTA = Pixel(255, 0, 255)
    YELLOW  = Pixel(255, 255, 0)
    ORANGE  = Pixel(255, 165, 0)
    PINK    = Pixel(255, 192, 203)
    GOLD    = Pixel(255, 215, 0)

    def __init__(self, size):
        self.__canvas = [None] * size

    def get_pixel(self, p):
        return self.__canvas[p]

    def set_pixel(self, p, pixel):
        self.__canvas[p] = pixel

    def blank_pixel(self, p):
        self.set_pixel(p, self.BLANK_PIXEL)

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
