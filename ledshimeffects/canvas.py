from ledshimeffects.pixel import Pixel


class Canvas:
    """
    Abstract representation of a single line of LEDs.

    Each LED is represented by a Pixel instance.
    """

    BLANK_PIXEL = Pixel(0, 0, 0, 0)   # An unlit LED.

    def __init__(self, size: int):
        """
        Initialise LED line.
        :param size: the number of LEDs in the line
        """
        if size < 1 or size > 100:
            raise ValueError("Canvas size outside reasonable range of 1 to 100!")
        self.__canvas = [self.BLANK_PIXEL] * size

    def __validate_index(self, p: int):
        if p < 0 or p >= len(self.__canvas):
            raise ValueError("Pixel index out of range for Canvas!")

    def get_pixel(self, p: int) -> Pixel:
        """
        Get a pixel.
        :param p: the position to return the pixel for
        :return: the pixel instance at the requested position
        """
        self.__validate_index(p)
        return self.__canvas[p]

    def set_pixel(self, p: int, pixel: Pixel):
        """
        Set a pixel.
        :param p: the position of the pixel to set
        :param pixel: the pixel to set at the given p
        :return: No meaningful return
        """
        self.__validate_index(p)
        self.__canvas[p] = pixel

    def blank_pixel(self, p: int):
        """
        Blank a pixel.
        :param p: the position of the pixel to blank
        :return: No meaningful return
        """
        self.__validate_index(p)
        self.set_pixel(p, self.BLANK_PIXEL)

    def is_blank_pixel(self, p: int):
        """
        Check if a pixel is blank.
        :param p: the position of the pixel to check
        :return: true if the pixel is a __BLANK_PIXEL otherwise false
        """
        return self.get_pixel(p) is self.BLANK_PIXEL

    def clear_all(self):
        """
        Clear all the pixels.
        :return: No meaningful return
        """
        self.set_all(self.BLANK_PIXEL)

    def set_all(self, pixel: Pixel):
        """
        Set all the pixels.
        :param pixel: the pixel instance to set
        :return: No meaningful return
        """
        for i in range(self.get_size()):
            self.set_pixel(i, pixel)

    def get_size(self) -> int:
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
