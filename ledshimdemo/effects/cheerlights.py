import requests

from ledshimdemo.canvas import Canvas
from ledshimdemo.pixel import Pixel
from ledshimdemo.abstract_effect import AbstractEffect


class CheerLightsEffect(AbstractEffect):
    """
    Synchronize with the CheerLights "Internet of Things" project, see https://cheerlights.com
    """

    URL = "http://api.thingspeak.com/channels/1417/field/2/last.json"

    @staticmethod
    def get_colour_from_channel(url: str) -> str:
        try:
            response = requests.get(url, timeout=3)
            response.raise_for_status()
            return response.json()["field2"]
        except requests.exceptions.RequestException:
            return None

    def __init__(self, canvas: Canvas) -> None:
        self.__colour = None
        super(CheerLightsEffect, self)\
            .__init__("CheerLights", "Synchronize with the CheerLights \"Internet of Things\" project.", 5, canvas)

    def compose(self) -> None:
        self.__colour = self.get_colour_from_channel(self.URL)
        if self.__colour is None:
            pixel = self.canvas.BLANK_PIXEL
        else:
            pixel = Pixel.hex_to_pixel(self.__colour)
        self.canvas.set_all(pixel)

    def __repr__(self) -> str:
        return "CheerLights(Colour:{0})".format(self.__colour)
