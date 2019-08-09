import unittest

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.gradient_graph import GradientGraph


class TestGradientGraph(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = GradientGraph(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^GradientGraph\\(Height:0\\.\\d{1,18}\\)$")
