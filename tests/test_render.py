import unittest
import mock
import sys

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.render import get_next_effect, copy_to_shim, render
from ledshimdemo.load_effect import load_effect


class TestRender(unittest.TestCase):

    CANVAS_SIZE = 3
    EFFECT_DISPLAY = 'CYCLE'
    EFFECT_DURATION = 3
    EFFECT_RUN = 1

    def setUp(self):
        canvas = Canvas(self.CANVAS_SIZE)
        self.effects = [load_effect("ledshimdemo.effects.solid_colours", "SolidColoursEffect", canvas),
                        load_effect("ledshimdemo.effects.random_blink", "RandomBlinkEffect", canvas),
                        load_effect("ledshimdemo.effects.rainbow", "RainbowEffect", canvas)]

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
        effect = self.effects[0]
        copy_to_shim(effect, False)
        self.assertEqual(set_pixel_mock.call_count, self.CANVAS_SIZE)
        show_mock.assert_called_once()

    @mock.patch('ledshim.set_clear_on_exit')
    @mock.patch('ledshim.set_pixel')
    @mock.patch('ledshim.show')
    @mock.patch('ledshim.clear')
    def test_render(self, clear_mock, show_mock, set_pixel_mock, clear_on_exit_mock):
        set_pixel_mock.reset_mock()
        show_mock.reset_mock()
        # We just want to test with one effect and SolidColours is the simplest.
        effects = [self.effects[0]]
        render(self.EFFECT_DISPLAY, self.EFFECT_DURATION, self.EFFECT_RUN, False, effects)
        clear_on_exit_mock.assert_called_once()
        self.assertEqual(set_pixel_mock.call_count,
                         self.CANVAS_SIZE * (self.EFFECT_DURATION / effects[0].get_speed()) * self.EFFECT_RUN)
        self.assertEqual(show_mock.call_count,
                         (self.EFFECT_RUN * (self.EFFECT_DURATION / effects[0].get_speed())) + 1)
        clear_mock.assert_called_once()
