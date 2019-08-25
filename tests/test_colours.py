from unittest import TestCase

from ledshimdemo.colours import Colours
from ledshimdemo.pixel import Pixel


class TestColours(TestCase):

    DEFAULT_BRIGHTNESS = 0.8

    def setUp(self):
        Pixel.set_default_brightness(self.DEFAULT_BRIGHTNESS)

    def test_red(self):
        self.assertEqual(Colours.RED.get_r(), 255)
        self.assertEqual(Colours.RED.get_g(), 0)
        self.assertEqual(Colours.RED.get_b(), 0)
        self.assertEqual(Colours.RED.get_brightness(), self.DEFAULT_BRIGHTNESS)

    def test_green(self):
        self.assertEqual(Colours.GREEN.get_r(), 0)
        self.assertEqual(Colours.GREEN.get_g(), 255)
        self.assertEqual(Colours.GREEN.get_b(), 0)
        self.assertEqual(Colours.GREEN.get_brightness(), self.DEFAULT_BRIGHTNESS)

    def test_blue(self):
        self.assertEqual(Colours.BLUE.get_r(), 0)
        self.assertEqual(Colours.BLUE.get_g(), 0)
        self.assertEqual(Colours.BLUE.get_b(), 255)
        self.assertEqual(Colours.BLUE.get_brightness(), self.DEFAULT_BRIGHTNESS)

    def test_red_brightness_change(self):
        Pixel.set_default_brightness(0.42)
        self.assertEqual(Colours.RED.get_r(), 255)
        self.assertEqual(Colours.RED.get_g(), 0)
        self.assertEqual(Colours.RED.get_b(), 0)
        self.assertEqual(Colours.RED.get_brightness(), 0.42)

    def test_colours(self):
        self.assertEqual(len(Colours.COLOURS), 12)
