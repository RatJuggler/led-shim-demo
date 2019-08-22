import unittest
import mock
import sys

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.candle import CandleEffect


class TestCandle(unittest.TestCase):

    TEST_CANVAS_SIZE = 28  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CandleEffect(canvas)
        effect.compose()
        self.assertEqual(repr(effect), "Candle(Candle Size:14, Flame Size:14)")
