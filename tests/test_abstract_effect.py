import unittest
from unittest.mock import patch

from ledshimdemo.canvas import Canvas
from ledshimdemo.abstract_effect import AbstractEffect


class TestAbstractEffect(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    @patch.multiple(AbstractEffect, __abstractmethods__=set())
    def test_base_properties(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effect = AbstractEffect("Test", "Test description.", 7, canvas)
        self.assertEqual(effect.get_name(), "Test")
        self.assertEqual(effect.get_display_list_entry(6), "Test   - Test description.")
        self.assertEqual(str(effect), "Effect: Test - Test description. Update Frequency: 7 secs")
