from colours import Colours

import unittest


class TestColours(unittest.TestCase):

    def test_red(self):
        self.assertEqual(Colours.RED.get_r(), 255)
        self.assertEqual(Colours.RED.get_g(), 0)
        self.assertEqual(Colours.RED.get_b(), 0)

    def test_colours(self):
        self.assertEqual(len(Colours.COLOURS), 12)


if __name__ == '__main__':
    unittest.main()
