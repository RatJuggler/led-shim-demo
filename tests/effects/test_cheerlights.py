from unittest import TestCase
from unittest.mock import Mock, patch
import sys

sys.modules['smbus'] = Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.cheerlights import CheerLightsEffect


class TestCheerLights(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_cheerlight_call(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLightsEffect(canvas)
        self.assertIsNone(effect.get_colour_from_channel("http://ejiferfneciudwedwojcmeiocnw.com"))

    @patch('ledshimdemo.effects.cheerlights.CheerLightsEffect.get_colour_from_channel', return_value=None)
    def test_effect_failed_cheerlights(self, patch_function):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLightsEffect(canvas)
        effect.compose()
        patch_function.assert_called_once()
        for i in range(canvas.get_size()):
            self.assertEqual(canvas.get_pixel(i), canvas.BLANK_PIXEL)

    def test_effect_working_cheerlights(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = CheerLightsEffect(canvas)
        # Must check before and after in case it changes during the test.
        before = effect.get_colour_from_channel(effect.URL)
        effect.compose()
        after = effect.get_colour_from_channel(effect.URL)
        self.assertRegex(repr(effect), "^CheerLights\\(Colour:({0}|{1})\\)$".format(before, after))
