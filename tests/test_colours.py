import unittest

from ledshimdemo.colours import Colours
from ledshimdemo.pixel import Pixel


class TestColours(unittest.TestCase):

    def test_red(self):
        self.assertEqual(Colours.RED.get_r(), 255)
        self.assertEqual(Colours.RED.get_g(), 0)
        self.assertEqual(Colours.RED.get_b(), 0)
        self.assertEqual(Colours.RED.get_brightness(), Pixel.DEFAULT_BRIGHTNESS)

    def test_green(self):
        self.assertEqual(Colours.GREEN.get_r(), 0)
        self.assertEqual(Colours.GREEN.get_g(), 255)
        self.assertEqual(Colours.GREEN.get_b(), 0)
        self.assertEqual(Colours.GREEN.get_brightness(), Pixel.DEFAULT_BRIGHTNESS)

    def test_blue(self):
        self.assertEqual(Colours.BLUE.get_r(), 0)
        self.assertEqual(Colours.BLUE.get_g(), 0)
        self.assertEqual(Colours.BLUE.get_b(), 255)
        self.assertEqual(Colours.BLUE.get_brightness(), Pixel.DEFAULT_BRIGHTNESS)

    def test_colours(self):
        self.assertEqual(len(Colours.COLOURS), 12)
