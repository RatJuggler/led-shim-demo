from .abstract_effect import AbstractEffect

import requests


class CheerLights(AbstractEffect):
    """
    Synchronize with the CheerLights "Internet of Things" project, see https://cheerlights.com
    """

    colour = None

    def __init__(self, canvas, debug):
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
        self.colour = self.get_colour_from_channel()
        if self.colour is None:
            pixel = self.canvas.BLANK_PIXEL
        else:
            pixel = self.canvas.hex_to_rgb(self.colour)  # Convert colour to r, g, b.
            pixel.append(1)                              # Add the brightness.
        self.canvas.set_all(pixel)

    def print_debug(self):
        print("Colour: {0}".format(self.colour))
