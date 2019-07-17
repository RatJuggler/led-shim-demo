import unittest

from ledshimeffects.canvas import Canvas


class TestCanvas(unittest.TestCase):

    def test_constructor(self):
        canvas = Canvas(10)
        self.assertEqual(canvas.get_size(), 10)


if __name__ == '__main__':
    unittest.main()
