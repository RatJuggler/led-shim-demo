import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.candle import Candle


class TestCandle(unittest.TestCase):

    TEST_CANVAS_SIZE = 28  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = Candle(canvas)
        effect.compose()
        self.assertEqual(repr(effect), "Candle(Candle Size:14, Flame Size:14)")
