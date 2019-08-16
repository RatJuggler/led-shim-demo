import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.digital_rain import DigitalRain


class TestDigitalRain(unittest.TestCase):

    TEST_CANVAS_SIZE = 14  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = DigitalRain(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^DigitalRain\\(Tick:1, Drops:\\[Drop\\(Falling:12, Trail:\\d, IntensityStep:\\d\\d, Speed:\\d\\)\\]\\)$")
