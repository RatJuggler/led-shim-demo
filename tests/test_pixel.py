import unittest

from ledshimeffects.pixel import Pixel


class TestPixel(unittest.TestCase):

    def test_constructor_default_brightness(self):
        pixel = Pixel(10, 20, 30)
        self.assertEqual(pixel.get_r(), 10)
        self.assertEqual(pixel.get_g(), 20)
        self.assertEqual(pixel.get_b(), 30)
        self.assertEqual(pixel.get_brightness(), pixel.DEFAULT_BRIGHTNESS)

    def test_constructor_with_brightness(self):
        pixel = Pixel(10, 20, 30, 1)
        self.assertEqual(pixel.get_r(), 10)
        self.assertEqual(pixel.get_g(), 20)
        self.assertEqual(pixel.get_b(), 30)
        self.assertEqual(pixel.get_brightness(), 1)

    def test_from_tuple_default_brightness(self):
        pixel = Pixel.from_tuple([40, 50, 60])
        self.assertEqual(pixel.get_r(), 40)
        self.assertEqual(pixel.get_g(), 50)
        self.assertEqual(pixel.get_b(), 60)
        self.assertEqual(pixel.get_brightness(), pixel.DEFAULT_BRIGHTNESS)

    def test_from_tuple_with_brightness(self):
        pixel = Pixel.from_tuple([40, 50, 60, 1])
        self.assertEqual(pixel.get_r(), 40)
        self.assertEqual(pixel.get_g(), 50)
        self.assertEqual(pixel.get_b(), 60)
        self.assertEqual(pixel.get_brightness(), 1)

    def test_hex_to_pixel_default_brightness(self):
        pixel = Pixel.hex_to_pixel("#708090")
        self.assertEqual(pixel.get_r(), 112)
        self.assertEqual(pixel.get_g(), 128)
        self.assertEqual(pixel.get_b(), 144)
        self.assertEqual(pixel.get_brightness(), pixel.DEFAULT_BRIGHTNESS)


if __name__ == '__main__':
    unittest.main()
