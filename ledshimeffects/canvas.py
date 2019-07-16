from ledshimeffects.pixel import Pixel


class Canvas:
    """
    Abstract representation of a single line of LEDs.

    Each LED is represented by a Pixel instance.
    """

    __BLANK_PIXEL = Pixel(0, 0, 0, 0)   # An unlit LED.

    def __init__(self, size):
        """
        Initialise LED line.
        :param size: the number of LEDs in the line
        """
        self.__canvas = [None] * size

    def get_pixel(self, p):
        """
        Get a pixel.
        :param p: the position to return the pixel for
        :return: the pixel instance at the requested position
        """
        return self.__canvas[p]

    def set_pixel(self, p, pixel):
        """
        Set a pixel.
        :param p: the position of the pixel to set
        :param pixel: the pixel to set at the given p
        :return: No meaningful return
        """
        self.__canvas[p] = pixel

    def blank_pixel(self, p):
        """
        Blank a pixel.
        :param p: the position of the pixel to blank
        :return: No meaningful return
        """
        self.set_pixel(p, self.__BLANK_PIXEL)

    def clear_all(self):
        """
        Clear all the pixels.
        :return: No meaningful return
        """
        self.set_all(self.__BLANK_PIXEL)

    def set_all(self, pixel):
        """
        Set all the pixels.
        :param pixel: the pixel instance to set
        :return: No meaningful return
        """
        for i in range(self.get_size()):
            self.set_pixel(i, pixel)

    def get_size(self):
        """
        Get the current number of LEDs.
        :return: The number of LEDs represented in this instance.
        """
        return self.__canvas.__len__()

    def __repr__(self):
        canvas = ["Canvas("]
        for i in range(self.get_size()):
            canvas.append("[{0:2d}, {1}]".format(i, repr(self.get_pixel(i))))
        canvas.append(")")
        return "\n".join(canvas)
