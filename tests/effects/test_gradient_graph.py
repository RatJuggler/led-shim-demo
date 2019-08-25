from unittest import TestCase
import mock
import sys

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.gradient_graph import GradientGraphEffect


class TestGradientGraph(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = GradientGraphEffect(canvas)
        effect.compose()
        self.assertRegex(repr(effect), "^GradientGraph\\(Height:0\\.\\d{1,8}\\)$")
