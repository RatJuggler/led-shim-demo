import unittest
import mock
import sys

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.render import get_next_effect, copy_to_shim, render
from ledshimdemo.effects import AbstractEffect, SolidColours, RandomBlink, Rainbow


class TestRender(unittest.TestCase):

    CANVAS_SIZE = 3  # type: int
    EFFECT_DISPLAY = 'CYCLE'  # type: str
    EFFECT_DURATION = 3  # type: int
    EFFECT_RUN = 1  # type: int

    def setUp(self):
        canvas = Canvas(self.CANVAS_SIZE)
        self.effects = [SolidColours(canvas),
                        RandomBlink(canvas),
                        Rainbow(canvas)]

    def test_get_next_effect_cycle(self):
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, SolidColours)
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, RandomBlink)
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, Rainbow)
        effect = get_next_effect(self.EFFECT_DISPLAY, self.effects)
        self.assertIsInstance(effect, SolidColours)

    def test_get_next_effect_random(self):
        effect = get_next_effect('RANDOM', self.effects)  # type: AbstractEffect
        self.assertTrue(isinstance(effect, (SolidColours, RandomBlink, Rainbow)))

    @mock.patch('ledshim.set_pixel')
    @mock.patch('ledshim.show')
    def test_copy_to_shim(self, show_mock, set_pixel_mock):
        effect = self.effects[0]  # type: AbstractEffect
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
        effects = [self.effects[0]]  # We just want to test with one effect.
        render(self.EFFECT_DISPLAY, self.EFFECT_DURATION, self.EFFECT_RUN, False, effects)
        clear_on_exit_mock.assert_called_once()
        self.assertEqual(set_pixel_mock.call_count, 18)
        self.assertEqual(show_mock.call_count, 6 + 1)
        clear_mock.assert_called_once()
