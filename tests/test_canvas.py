import unittest

from ledshimeffects.canvas import Canvas


class TestCanvas(unittest.TestCase):

    def test_constructor_valid_size(self):
        canvas = Canvas(10)
        self.assertEqual(canvas.get_size(), 10)

    def test_constructor_negative_size(self):
        size = -10
        self.assertRaises(ValueError, Canvas, size)

    def test_constructor_enormous_size(self):
        size = 1000
        self.assertRaises(ValueError, Canvas, size)


if __name__ == '__main__':
    unittest.main()
