import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.coloured_lights import ColouredLights


class TestColouredLights(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = ColouredLights(canvas)
        effect.compose()
        self.assertEqual(repr(effect), "ColouredLights(Number Colours:3, Colour:1)")
