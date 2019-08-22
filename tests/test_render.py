import unittest
import mock
import sys
import os

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effect_factory import EffectFactory
from ledshimdemo.render import render


class TestRender(unittest.TestCase):

    CANVAS_SIZE = 3
    EFFECT_DISPLAY = 'CYCLE'
    EFFECT_DURATION = 2

    def setUp(self):
        canvas = Canvas(self.CANVAS_SIZE)
        self.effect_factory = EffectFactory(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", canvas)
        self.effect_factory.set_effects_selected([])

    @mock.patch('ledshim.set_clear_on_exit')
    @mock.patch('ledshim.set_pixel')
    @mock.patch('ledshim.show')
    @mock.patch('ledshim.clear')
    def test_render(self, clear_mock, show_mock, set_pixel_mock, clear_on_exit_mock):
        set_pixel_mock.reset_mock()
        show_mock.reset_mock()
        render(self.EFFECT_DISPLAY, self.EFFECT_DURATION, self.effect_factory.get_count_effects_selected(), False, self.effect_factory)
        clear_on_exit_mock.assert_called_once()
        set_pixel_call_count = 0
        show_call_count = 0
#        for effect in self.effects:
#            set_pixel_call_count += self.CANVAS_SIZE * (self.EFFECT_DURATION / effect.get_update_frequency())
#            show_call_count += self.EFFECT_DURATION / effect.get_update_frequency()
        show_call_count += 1  # Final call to show cleared shim.
        self.assertEqual(set_pixel_call_count, set_pixel_mock.call_count)
        self.assertEqual(show_call_count, show_mock.call_count)
        clear_mock.assert_called_once()
