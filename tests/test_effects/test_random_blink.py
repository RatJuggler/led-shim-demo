import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.random_blink import RandomBlink


class TestRandomBlink(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = RandomBlink(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^RandomBlink\\(Blink:\\[\\d(\\, \\d)?\\]\\)$")
