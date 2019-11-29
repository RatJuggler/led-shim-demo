from unittest import TestCase
from unittest.mock import Mock
import sys

sys.modules['smbus'] = Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.random_blink import RandomBlinkEffect


class TestRandomBlink(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = RandomBlinkEffect(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^RandomBlink\\(Blink:\\[\\d(\\, \\d)?\\]\\)$")
