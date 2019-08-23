import ledshim
import logging

from .pixel import Pixel


class Canvas:
    """
    Abstract representation of a single line of pixels (LEDs) on a shim.

    Each LED is represented by a Pixel instance though all instances may not be unique.
    """

    BLANK_PIXEL = Pixel(0, 0, 0, 0)  # An unlit pixel.

    __invert_display = False

    def __init__(self, size: int) -> None:
        """
        Initialise the virtual canvas.
        :param size: the number of pixels on the shim
        """
        if size < 1 or size > 100:
            raise ValueError("Canvas size outside reasonable range of 1 to 100!")
        self.__canvas = [self.BLANK_PIXEL] * size

    @classmethod
    def is_display_inverted(cls) -> float:
        """
        Return the display orientation toggle.
        :return: True if the display should be inverted, otherwise False.
        """
        return cls.__invert_display

    @classmethod
    def invert_display(cls) -> None:
        """
        Reverse the display shown on the shim. This can be toggled to allow for the orientation of the Pi.
        :return: No meaningful return.
        """
        cls.__invert_display = not cls.__invert_display

    def __validate_index(self, p: int) -> None:
        """
        Validate an index position on the current shim is in range.
        :param p: the position on the shim to validate
        :return: Will raise a ValueError if the index position is not in range
        """
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

    def set_pixel(self, p: int, pixel: Pixel) -> None:
        """
        Set a pixel.
        :param p: the position of the pixel to set
        :param pixel: the pixel to set at the given position
        :return: No meaningful return
        """
        self.__validate_index(p)
        self.__canvas[p] = pixel

    def blank_pixel(self, p: int) -> None:
        """
        Blank a pixel.
        :param p: the position of the pixel to blank
        :return: No meaningful return
        """
        self.__validate_index(p)
        self.set_pixel(p, self.BLANK_PIXEL)

    def is_blank_pixel(self, p: int) -> bool:
        """
        Check if a pixel is blank.
        :param p: the position of the pixel to check
        :return: true if the pixel is a __BLANK_PIXEL otherwise false
        """
        return self.get_pixel(p) is self.BLANK_PIXEL

    def clear_all(self) -> None:
        """
        Clear all the pixels.
        :return: No meaningful return
        """
        self.set_all(self.BLANK_PIXEL)

    def set_all(self, pixel: Pixel) -> None:
        """
        Set all the pixels.
        :param pixel: the pixel instance to set
        :return: No meaningful return
        """
        for i in range(self.get_size()):
            self.set_pixel(i, pixel)

    def get_size(self) -> int:
        """
        Get the current number of pixels.
        :return: The number of pixels represented in this instance.
        """
        return len(self.__canvas)

    def __repr__(self) -> str:
        canvas = ["Canvas("]
        for i in range(self.get_size()):
            canvas.append("[{0:2d}, {1}]".format(i, repr(self.get_pixel(i))))
        canvas.append(")")
        return "\n".join(canvas)

    def render_to_shim(self) -> None:
        """
        Display the effect canvas on the shim.
        :return: No meaningful return
        """
        logging.debug(repr(self.__canvas))
        for i in range(self.get_size()):
            pixel = self.get_pixel(i)
            position = (self.get_size() - 1 - i) if Canvas.is_display_inverted() else i
            ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
        ledshim.show()
