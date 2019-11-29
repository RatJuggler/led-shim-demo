from unittest import TestCase
from unittest.mock import Mock
import sys

sys.modules['smbus'] = Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.digital_rain import DigitalRainEffect


class TestDigitalRain(TestCase):

    TEST_CANVAS_SIZE = 14  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = DigitalRainEffect(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^DigitalRain\\(Tick:1, Drops:\\[Drop\\(Falling:12, Trail:\\d, IntensityStep:\\d\\d, Speed:\\d\\)\\]\\)$")
