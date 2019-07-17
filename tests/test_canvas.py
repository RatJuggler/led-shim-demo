import unittest

from ledshimeffects.canvas import Canvas
from ledshimeffects.colours import Colours


class TestCanvasConstructor(unittest.TestCase):

    def test_constructor_valid_size(self):
        canvas = Canvas(10)
        self.assertEqual(canvas.get_size(), 10)

    def test_constructor_negative_size(self):
        size = -10
        self.assertRaises(ValueError, Canvas, size)

    def test_constructor_enormous_size(self):
        size = 1000
        self.assertRaises(ValueError, Canvas, size)


class TestCanvasGetPixel(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(2)
        self.canvas.set_pixel(1, Colours.BLUE)

    def test_get_pixel_none(self):
        pixel = self.canvas.get_pixel(0)
        self.assertIsNone(pixel)

    def test_get_pixel_color(self):
        pixel = self.canvas.get_pixel(1)
        self.assertEqual(pixel, Colours.BLUE)

    def test_get_pixel_invalid(self):
        with self.assertRaises(ValueError):
            self.canvas.get_pixel(99)


class TestCanvasSetPixel(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(2)

    def test_set_pixel_none(self):
        self.canvas.set_pixel(0, None)
        self.assertIsNone(self.canvas.get_pixel(0))

    def test_set_pixel_color(self):
        self.canvas.set_pixel(1, Colours.BLUE)
        self.assertEqual(self.canvas.get_pixel(1), Colours.BLUE)

    def test_set_pixel_invalid(self):
        with self.assertRaises(ValueError):
            self.canvas.set_pixel(99, Colours.RED)


if __name__ == '__main__':
    unittest.main()
