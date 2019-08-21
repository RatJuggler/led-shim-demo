import unittest
import mock
import sys
import os

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.render import get_next_effect, copy_to_shim, render
from ledshimdemo.effect_factory import load_effects


class TestRender(unittest.TestCase):

    CANVAS_SIZE = 3
    EFFECT_DISPLAY = 'CYCLE'
    EFFECT_DURATION = 2

    def setUp(self):
        canvas = Canvas(self.CANVAS_SIZE)
        effects_dict = load_effects(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", canvas)
        self.effects = list(effects_dict.values())

    def test_get_next_effect_cycle(self):
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, type(self.effects[0]))
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, type(self.effects[1]))
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, type(self.effects[2]))
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, type(self.effects[0]))

    def test_get_next_effect_random(self):
        effect = get_next_effect('RANDOM', self.effects)
        self.assertTrue(isinstance(effect, (type(self.effects[0]), type(self.effects[1]), type(self.effects[2]))))

    @mock.patch('ledshim.set_pixel')
    @mock.patch('ledshim.show')
    def test_copy_to_shim(self, show_mock, set_pixel_mock):
        set_pixel_mock.reset_mock()
        show_mock.reset_mock()
        copy_to_shim(self.effects[0], False)
        self.assertEqual(set_pixel_mock.call_count, self.CANVAS_SIZE)
        show_mock.assert_called_once()

    @mock.patch('ledshim.set_clear_on_exit')
    @mock.patch('ledshim.set_pixel')
    @mock.patch('ledshim.show')
    @mock.patch('ledshim.clear')
    def test_render(self, clear_mock, show_mock, set_pixel_mock, clear_on_exit_mock):
        set_pixel_mock.reset_mock()
        show_mock.reset_mock()
        render(self.EFFECT_DISPLAY, self.EFFECT_DURATION, len(self.effects), False, self.effects)
        clear_on_exit_mock.assert_called_once()
        set_pixel_call_count = 0
        show_call_count = 0
        for effect in self.effects:
            set_pixel_call_count += self.CANVAS_SIZE * (self.EFFECT_DURATION / effect.get_speed())
            show_call_count += self.EFFECT_DURATION / effect.get_speed()
        show_call_count += 1  # Final call to show cleared shim.
        self.assertEqual(set_pixel_call_count, set_pixel_mock.call_count)
        self.assertEqual(show_call_count, show_mock.call_count)
        clear_mock.assert_called_once()
