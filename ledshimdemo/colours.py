from .pixel import Pixel


class Colours:
    """
    Encapsulate a selection of standard colours to use.
    """

    RED = Pixel(255, 0, 0)
    GREEN = Pixel(0, 255, 0)
    BLUE = Pixel(0, 0, 255)
    CYAN = Pixel(0, 255, 255)
    WHITE = Pixel(255, 255, 255)
    OLDLACE = Pixel(253, 245, 230)
    PURPLE = Pixel(128, 0, 128)
    MAGENTA = Pixel(255, 0, 255)
    YELLOW = Pixel(255, 255, 0)
    ORANGE = Pixel(255, 165, 0)
    PINK = Pixel(255, 192, 203)
    GOLD = Pixel(255, 215, 0)

    COLOURS = [RED, GREEN, BLUE, CYAN, WHITE, OLDLACE, PURPLE, MAGENTA, YELLOW, ORANGE, PINK, GOLD]
