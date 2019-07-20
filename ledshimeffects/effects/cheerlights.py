import requests

from pixel import Pixel
from .abstract_effect import AbstractEffect


class CheerLights(AbstractEffect):
    """
    Synchronize with the CheerLights "Internet of Things" project, see https://cheerlights.com
    """

    def __init__(self, canvas, debug=False):
        self.__colour = None
        self.__url = "http://api.thingspeak.com/channels/1417/field/2/last.json"
        super(CheerLights, self).__init__("cheerlights", 5, canvas, debug)

    def get_colour_from_channel(self):
        try:
            response = requests.get(self.__url, timeout=3)
            response.raise_for_status()
            return response.json()["field2"]
        except requests.exceptions.RequestException:
            return

    def compose(self):
        self.__colour = self.get_colour_from_channel()
        if self.__colour is None:
            pixel = self.canvas.BLANK_PIXEL
        else:
            pixel = Pixel.hex_to_pixel(self.__colour)
        self.canvas.set_all(pixel)

    def __repr__(self):
        return "CheerLights(Colour:{0})".format(self.__colour)
