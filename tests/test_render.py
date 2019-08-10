import unittest
import mock
import sys

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects import SolidColours


class TestRender(unittest.TestCase):

    def test_render(self):
        sys.modules['ledshim'] = mock.Mock()
        from render import render

        canvas = Canvas(3)
        effects = [SolidColours(canvas)]

        render("CYCLE", 3, 1, False, effects)
        self.assertTrue(True)
