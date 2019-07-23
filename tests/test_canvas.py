import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.colours import Colours


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
        self.canvas.set_pixel(2, Colours.PINK)

    def test_get_pixel_blank(self):
        pixel = self.canvas.get_pixel(0)
        self.assertEqual(pixel, self.canvas.BLANK_PIXEL)

    def test_get_pixel_color1(self):
        pixel = self.canvas.get_pixel(1)
        self.assertEqual(pixel, Colours.RED)

    def test_get_pixel_color2(self):
        pixel = self.canvas.get_pixel(2)
        self.assertEqual(pixel, Colours.PINK)

    def test_get_pixel_color3(self):
        with self.assertRaises(ValueError):
            self.canvas.get_pixel(3)

    def test_get_pixel_negative_index(self):
        with self.assertRaises(ValueError):
            self.canvas.get_pixel(-10)

    def test_get_pixel_enormous_index(self):
        with self.assertRaises(ValueError):
            self.canvas.get_pixel(1000)


class TestCanvasSetPixel(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(3)

    def test_set_pixel_none(self):
        self.canvas.set_pixel(0, None)
        self.assertIsNone(self.canvas.get_pixel(0))
        self.assertTrue(self.canvas.is_blank_pixel(1))
        self.assertTrue(self.canvas.is_blank_pixel(2))

    def test_set_pixel_color(self):
        self.canvas.set_pixel(1, Colours.BLUE)
        self.assertTrue(self.canvas.is_blank_pixel(0))
        self.assertEqual(self.canvas.get_pixel(1), Colours.BLUE)
        self.assertTrue(self.canvas.is_blank_pixel(2))

    def test_set_pixel_negative_index(self):
        with self.assertRaises(ValueError):
            self.canvas.set_pixel(-10, Colours.BLUE)

    def test_set_pixel_enormous_index(self):
        with self.assertRaises(ValueError):
            self.canvas.set_pixel(1000, Colours.BLUE)


class TestCanvasBlankPixel(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(3)
        self.canvas.set_all(Colours.GREEN)

    def test_blank_pixel_valid(self):
        for i in range(self.canvas.get_size()):
            self.assertEqual(self.canvas.get_pixel(i), Colours.GREEN)
        self.canvas.blank_pixel(0)
        self.assertTrue(self.canvas.is_blank_pixel(0))
        self.assertEqual(self.canvas.get_pixel(1), Colours.GREEN)
        self.assertEqual(self.canvas.get_pixel(2), Colours.GREEN)

    def test_blank_pixel_negative_index(self):
        with self.assertRaises(ValueError):
            self.canvas.blank_pixel(-10)

    def test_blank_pixel_enormous_index(self):
        with self.assertRaises(ValueError):
            self.canvas.blank_pixel(1000)


class TestCanvasClearAll(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(3)
        self.canvas.set_all(Colours.PURPLE)

    def test_clear_all(self):
        for i in range(self.canvas.get_size()):
            self.assertEqual(self.canvas.get_pixel(i), Colours.PURPLE)
        self.canvas.clear_all()
        for i in range(self.canvas.get_size()):
            self.assertTrue(self.canvas.is_blank_pixel(i))


class TestCanvasSetAll(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(3)

    def test_set_all(self):
        for i in range(self.canvas.get_size()):
            self.assertTrue(self.canvas.is_blank_pixel(i))
        self.canvas.set_all(Colours.ORANGE)
        for i in range(self.canvas.get_size()):
            self.assertEqual(self.canvas.get_pixel(i), Colours.ORANGE)


class TestCanvasRepr(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(3)
        self.canvas.set_pixel(1, Colours.YELLOW)
        self.canvas.set_pixel(2, Colours.WHITE)

    def test_repr(self):
        canvas = ["Canvas(",
                  "[ 0, Pixel(r:0, g:0, b:0, brightness:0)]",
                  "[ 1, Pixel(r:255, g:255, b:0, brightness:0.8)]",
                  "[ 2, Pixel(r:255, g:255, b:255, brightness:0.8)]",
                  ")"]
        expected_repr = "\n".join(canvas)
        actual_repr = repr(self.canvas)
        self.assertEqual(expected_repr, actual_repr)
