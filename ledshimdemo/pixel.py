

class Pixel:
    """
    Abstract representation of a pixel LED.
    """

    DEFAULT_BRIGHTNESS = 0.8

    @staticmethod
    def __validate_component(colour: str, c: int):
        """
        Validate an RGB component is in the range 0-255.
        :param colour: name of the component being validated
        :param c: the component value
        :return: Will raise a ValueError if the component is not in range
        """
        if c < 0 or c > 255:
            raise ValueError(colour + " colour component out of range (0-255) for Pixel!")

    @staticmethod
    def __validate_components(r: int, g: int, b: int):
        """
        Validate the R,G and B components.
        :param r: red component value
        :param g: green component value
        :param b: blue component value
        :return: No meaningful return
        """
        Pixel.__validate_component("Red", r)
        Pixel.__validate_component("Green", g)
        Pixel.__validate_component("Blue", b)

    @staticmethod
    def __validate_brightness(b: float):
        """
        Validate the brightness level is in the range 0.0-1.0.
        :param b: the brightness level to valdidate
        :return: Will raise a ValueError if the brightness is not in range
        """
        if b < 0.0 or b > 1.0:
            raise ValueError("Brightness level out of range (0.0-1.0) for Pixel!")

    def __init__(self, r, g, b, brightness=DEFAULT_BRIGHTNESS):
        """
        Initialise a Pixel.
        :param r: red component
        :param g: green component
        :param b: blue component
        :param brightness: level of brightness
        """
        Pixel.__validate_components(r, g, b)
        self.__r = r
        self.__g = g
        self.__b = b
        Pixel.__validate_brightness(brightness)
        self.__brightness = brightness

    @classmethod
    def from_tuple(cls, pixel):
        """
        Alternative constructor using a list.
        :param pixel: list of three (r,g,b) or four (r,g,b,brightness) elements
        :return: a pixel instance
        """
        if len(pixel) == 3:
            return Pixel(pixel[0], pixel[1], pixel[2])
        if len(pixel) == 4:
            return Pixel(pixel[0], pixel[1], pixel[2], pixel[3])
        raise Exception("Pixel constructor requirements not met, found: {0}".format(pixel))

    @classmethod
    def hex_to_pixel(cls, col_hex):
        """
        Convert a hex colour to an RGB tuple.
        :param col_hex: the hex colour to convert e.g. #FF3C1A
        :return: a pixel instance representing the hex colour
        """
        pixel = list(bytearray.fromhex(col_hex.lstrip('#')))
        return cls.from_tuple(pixel)

    def get_r(self):
        return self.__r

    def get_g(self):
        return self.__g

    def get_b(self):
        return self.__b

    def get_brightness(self):
        return self.__brightness

    def __repr__(self):
        return "Pixel(r:{0}, g:{1}, b:{2}, brightness:{3})".format(self.__r, self.__g, self.__b, self.__brightness)
