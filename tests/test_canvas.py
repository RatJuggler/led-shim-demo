import unittest

from ledshimeffects.canvas import Canvas
from ledshimeffects.colours import Colours
from ledshimeffects.pixel import Pixel


class TestCanvasConstructor(unittest.TestCase):

    def test_constructor_valid_size(self):
        size = 3
        canvas = Canvas(size)
        self.assertEqual(canvas.get_size(), size)
        for i in range(size):
            self.assertTrue(canvas.is_blank_pixel(i))

    def test_constructor_negative_size(self):
        size = -10
        self.assertRaises(ValueError, Canvas, size)

    def test_constructor_enormous_size(self):
        size = 1000
        self.assertRaises(ValueError, Canvas, size)


class TestCanvasGetPixel(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(3)
        self.canvas.set_pixel(1, Colours.RED)

    def test_get_pixel_blank(self):
        pixel = self.canvas.get_pixel(0)
        self.assertEqual(pixel, self.canvas.BLANK_PIXEL)

    def test_get_pixel_color(self):
        pixel = self.canvas.get_pixel(1)
        self.assertEqual(pixel, Colours.RED)

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
            self.canvas.set_pixel(99, Colours.BLUE)


class TestCanvasBlankPixel(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(2)
        self.canvas.set_all(Colours.GREEN)

    def test_blank_pixel_valid(self):
        self.assertEqual(self.canvas.get_pixel(0), Colours.GREEN)
        self.canvas.blank_pixel(0)
        self.assertTrue(self.canvas.is_blank_pixel(0))

    def test_blank_pixel_invalid(self):
        with self.assertRaises(ValueError):
            self.canvas.blank_pixel(99)


class TestCanvasClearAll(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(2)
        self.canvas.set_all(Colours.PURPLE)

    def test_clear_all(self):
        for i in range(self.canvas.get_size()):
            self.assertEqual(self.canvas.get_pixel(i), Colours.PURPLE)
        self.canvas.clear_all()
        for i in range(self.canvas.get_size()):
            self.assertTrue(self.canvas.is_blank_pixel(i))


class TestCanvasSetAll(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(2)

    def test_set_all(self):
        for i in range(self.canvas.get_size()):
            self.assertTrue(self.canvas.is_blank_pixel(i))
        self.canvas.set_all(Colours.ORANGE)
        for i in range(self.canvas.get_size()):
            self.assertEqual(self.canvas.get_pixel(i), Colours.ORANGE)


if __name__ == '__main__':
    unittest.main()
