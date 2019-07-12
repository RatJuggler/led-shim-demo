

class Canvas:
    """
    Abstract representation of a line of LEDs.

    Each pixel is composed of the list: [r, g, b, brightness]
    """

    BLANK_PIXEL = [0, 0, 0, 0]
    RED     = [255, 0, 0, 1]
    GREEN   = [0, 255, 0, 1]
    BLUE    = [0, 0, 255, 1]
    CYAN    = [0, 255, 255, 1]
    WHITE   = [255, 255, 255, 1]
    OLDLACE = [253, 245, 230, 1]
    PURPLE  = [128, 0, 128, 1]
    MAGENTA = [255, 0, 255, 1]
    YELLOW  = [255, 255, 0, 1]
    ORANGE  = [255, 165, 0, 1]
    PINK    = [255, 192, 203, 1]

    def __init__(self, size):
        self.__canvas = [None] * size

    @staticmethod
    def hex_to_rgb(col_hex):
        """Convert a hex colour to an RGB tuple."""
        return bytearray.fromhex(col_hex.lstrip('#'))

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

    def print_canvas(self):
        for i in range(self.get_size()):
            print("{0:2d} = {1}".format(i, self.get_pixel(i)))
