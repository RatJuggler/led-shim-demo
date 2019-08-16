import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.digital_rain import DigitalRain


class TestDigitalRain(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = DigitalRain(canvas)
        effect.compose()
        self.assertEqual(repr(effect), "DigitalRain(Tick:1)")
