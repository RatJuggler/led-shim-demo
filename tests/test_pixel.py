from unittest import TestCase

from ledshimdemo.pixel import Pixel


class TestPixelConstructor(TestCase):

    DEFAULT_BRIGHTNESS = 0.8

    def setUp(self):
        Pixel.set_default_brightness(self.DEFAULT_BRIGHTNESS)

    def test_get_default_brightness(self):
        self.assertEqual(Pixel.get_default_brightness(), self.DEFAULT_BRIGHTNESS)

    def test_set_default_brightness(self):
        Pixel.set_default_brightness(0.42)
        self.assertEqual(Pixel.get_default_brightness(), 0.42)

    def test_set_invalid_default_brightness1(self):
        with self.assertRaises(ValueError):
            Pixel.set_default_brightness(-1)

    def test_set_invalid_default_brightness2(self):
        with self.assertRaises(ValueError):
            Pixel.set_default_brightness(10)

    def test_constructor_default_brightness(self):
        pixel = Pixel(10, 20, 30)
        self.assertEqual(pixel.get_r(), 10)
        self.assertEqual(pixel.get_g(), 20)
        self.assertEqual(pixel.get_b(), 30)
        self.assertEqual(pixel.get_brightness(), self.DEFAULT_BRIGHTNESS)

    def test_constructor_with_brightness(self):
        pixel = Pixel(10, 20, 30, 1)
        self.assertEqual(pixel.get_r(), 10)
        self.assertEqual(pixel.get_g(), 20)
        self.assertEqual(pixel.get_b(), 30)
        self.assertEqual(pixel.get_brightness(), 1)

    def test_constructor_invalid_red_component1(self):
        with self.assertRaises(ValueError):
            Pixel(-10, 20, 30, 1)

    def test_constructor_invalid_red_component2(self):
        with self.assertRaises(ValueError):
            Pixel(1000, 20, 30, 1)

    def test_constructor_invalid_green_component1(self):
        with self.assertRaises(ValueError):
            Pixel(10, -20, 30, 1)

    def test_constructor_invalid_green_component2(self):
        with self.assertRaises(ValueError):
            Pixel(10, 2000, 30, 1)

    def test_constructor_invalid_blue_component1(self):
        with self.assertRaises(ValueError):
            Pixel(10, 20, -30, 1)

    def test_constructor_invalid_blue_component2(self):
        with self.assertRaises(ValueError):
            Pixel(10, 20, 3000, 1)

    def test_constructor_invalid_brightness1(self):
        with self.assertRaises(ValueError):
            Pixel(10, 20, 30, -1)

    def test_constructor_invalid_brightness2(self):
        with self.assertRaises(ValueError):
            Pixel(10, 20, 30, 10)

    def test_from_tuple_default_brightness(self):
        pixel = Pixel.from_tuple([40, 50, 60])
        self.assertEqual(pixel.get_r(), 40)
        self.assertEqual(pixel.get_g(), 50)
        self.assertEqual(pixel.get_b(), 60)
        self.assertEqual(pixel.get_brightness(), self.DEFAULT_BRIGHTNESS)

    def test_from_tuple_with_brightness(self):
        pixel = Pixel.from_tuple([40, 50, 60, 1])
        self.assertEqual(pixel.get_r(), 40)
        self.assertEqual(pixel.get_g(), 50)
        self.assertEqual(pixel.get_b(), 60)
        self.assertEqual(pixel.get_brightness(), 1)

    def test_from_tuple_insufficient_elements(self):
        with self.assertRaises(Exception):
            Pixel.from_tuple([40, 50])

    def test_from_tuple_excess_elements(self):
        with self.assertRaises(Exception):
            Pixel.from_tuple([40, 50, 60, 70, 80])

    def test_hex_to_pixel_default_brightness(self):
        pixel = Pixel.hex_to_pixel("#708090")
        self.assertEqual(pixel.get_r(), 112)
        self.assertEqual(pixel.get_g(), 128)
        self.assertEqual(pixel.get_b(), 144)
        self.assertEqual(pixel.get_brightness(), self.DEFAULT_BRIGHTNESS)


class TestPixelRepr(TestCase):

    def setUp(self):
        self.pixel = Pixel(123, 221, 56, 0.42)

    def test_repr(self):
        expected_repr = "Pixel(r:123, g:221, b:56, brightness:0.42)"
        actual_repr = repr(self.pixel)
        self.assertEqual(expected_repr, actual_repr)
