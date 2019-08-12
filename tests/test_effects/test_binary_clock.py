from time import localtime, strftime
import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.binary_clock import BinaryClock


class TestBinaryClock(unittest.TestCase):

    TEST_CANVAS_SIZE = 28  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = BinaryClock(canvas)
        # Must check before and after in case it changes during the test.
        before = strftime("%H:%M:%S", localtime())
        effect.compose()
        after = strftime("%H:%M:%S", localtime())
        self.assertRegex(repr(effect), "^BinaryClock\\(Time:({0}|{1})\\)$".format(before, after))
