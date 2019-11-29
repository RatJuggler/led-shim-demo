from unittest import TestCase
from unittest.mock import Mock
import sys

from time import localtime, strftime

sys.modules['smbus'] = Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.binary_clock import BinaryClockEffect


class TestBinaryClock(TestCase):

    TEST_CANVAS_SIZE = 28  # type: int

    def test_canvas_size(self):
        canvas = Canvas(3)
        with self.assertRaises(AssertionError):
            BinaryClockEffect(canvas)

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = BinaryClockEffect(canvas)
        # Must check before and after in case it changes during the test.
        before = strftime("%H:%M:%S", localtime())
        effect.compose()
        after = strftime("%H:%M:%S", localtime())
        self.assertRegex(repr(effect), "^BinaryClock\\(Time:({0}|{1})\\)$".format(before, after))
