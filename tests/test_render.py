import unittest
import mock
import sys

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects import SolidColours, RandomBlink, Rainbow


class TestRender(unittest.TestCase):

    def setUp(self):
        canvas = Canvas(3)
        self.effects = [SolidColours(canvas),
                        RandomBlink(canvas),
                        Rainbow(canvas)]

    def test_get_next_effect_cycle(self):
        sys.modules['ledshim'] = mock.Mock()
        from ledshimdemo.render import get_next_effect
        effect = get_next_effect('CYCLE', self.effects)
        self.assertIsInstance(effect, SolidColours)
        effect = get_next_effect('CYCLE', self.effects)
        self.assertIsInstance(effect, RandomBlink)
        effect = get_next_effect('CYCLE', self.effects)
        self.assertIsInstance(effect, Rainbow)
        effect = get_next_effect('CYCLE', self.effects)
        self.assertIsInstance(effect, SolidColours)

    def test_get_next_effect_random(self):
        sys.modules['ledshim'] = mock.Mock()
        from ledshimdemo.render import get_next_effect
        effect = get_next_effect('RANDOM', self.effects)
        self.assertTrue(isinstance(effect, (SolidColours, RandomBlink, Rainbow)))

    def test_copy_to_shim(self):
        sys.modules['ledshim'] = mock.Mock()
        from ledshimdemo.render import copy_to_shim
        copy_to_shim(self.effects[0], False)

    def test_render(self):
        sys.modules['ledshim'] = mock.Mock()
        from ledshimdemo.render import render
        render("CYCLE", 3, 1, False, self.effects)
        self.assertTrue(True)
