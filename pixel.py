

class Pixel:
    """
    Abstract representation of a pixel LED.
    """

    DEFAULT_BRIGHTNESS = 0.8

    def __init__(self, r, g, b, brightness=DEFAULT_BRIGHTNESS):
        """
        Initialise a Pixel.
        :param r: red component
        :param g: green component
        :param b: blue component
        :param brightness: level of brightness
        """
        self.__r = r
        self.__g = g
        self.__b = b
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
