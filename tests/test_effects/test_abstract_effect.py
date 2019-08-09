import unittest
from unittest.mock import patch

from ledshimdemo.canvas import Canvas
from ledshimdemo.effects.abstract_effect import AbstractEffect


class TestAbstractEffect(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    @patch.multiple(AbstractEffect, __abstractmethods__=set())
    def test_something(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = AbstractEffect("Test", 7, canvas)
        self.assertEqual(effect.get_name(), "Test")
        self.assertEqual(effect.get_speed(), 7)
        self.assertEqual(str(effect), "Effect: Test, Speed: 7")
