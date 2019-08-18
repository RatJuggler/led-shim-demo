import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.solid_colours import SolidColoursEffect


class TestSolidColours(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = SolidColoursEffect(canvas)
        effect.compose()
        self.assertEqual(repr(effect), "SolidColours(Step:1)")
