from abstract_effect import AbstractEffect

import requests


class CheerLights(AbstractEffect):
    """
    Synchronize with the CheerLights "Internet of Things" project, see https://cheerlights.com
    """

    data = None

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

    def hex_to_rgb(self, col_hex):
        """Convert a hex colour to an RGB tuple."""
        col_hex = col_hex.lstrip('#')
        return bytearray.fromhex(col_hex)

    def compose(self):
        self.data = self.get_colour_from_channel()
        if self.data is None:
            r, g, b = 0, 0, 0
        else:
            r, g, b = self.hex_to_rgb(self.data)
        for i in range(self.canvas.get_size()):
            self.canvas.set_pixel(i, [r, g, b, 1])

    def print_debug(self):
        print("Colour: {0}".format(self.data))
