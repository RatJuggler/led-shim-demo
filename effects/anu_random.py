from .abstract_effect import AbstractEffect

import requests


class ANURandom(AbstractEffect):
    """
    Random effect using the ANU Quantum Random Numbers Server, see http://qrng.anu.edu.au
    """

    data = None

    def __init__(self, canvas, debug):
        self.__url = "https://qrng.anu.edu.au/API/jsonI.php?type=hex16&length={0}&size=3".format(canvas.get_size())
        super(ANURandom, self).__init__("anu_random", 3, canvas, debug)

    def get_random_numbers(self):
        try:
            response = requests.get(self.__url, timeout=3)
            response.raise_for_status()
            return response.json()["data"]
        except requests.exceptions.RequestException:
            return

    def compose(self):
        self.data = self.get_random_numbers()
        if self.data is None:
            self.canvas.set_all(self.canvas.BLANK_PIXEL)
        else:
            for i in range(self.canvas.get_size()):
                pixel = self.canvas.hex_to_pixel(self.data[i])  # Get a random block and convert to a pixel.
                self.canvas.set_pixel(i, pixel)

    def print_debug(self):
        print("Quantum: {0}".format(self.data))
