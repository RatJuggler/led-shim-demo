import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.cheerlights import CheerLights


class TestCheerLights(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_cheerlight_call(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLights(canvas)
        self.assertIsNone(effect.get_colour_from_channel("http://invalidtest.com"))

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLights(canvas)
        # Must check before and after in case it changes during the test.
        before = effect.get_colour_from_channel(effect.URL)
        effect.compose()
        after = effect.get_colour_from_channel(effect.URL)
        self.assertRegex(repr(effect), "^CheerLights\\(Colour:({0}|{1})\\)$".format(before, after))
