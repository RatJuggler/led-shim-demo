from unittest import TestCase
import mock
import sys

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.rainbow import RainbowEffect


class TestRainbow(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = RainbowEffect(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^Rainbow\\(Base Hue:\\d{1,3}\\)$")
