import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.rainbow import Rainbow


class TestRainbow(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = Rainbow(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^Rainbow\\(Base Hue:\\d{1,3}\\)$")
