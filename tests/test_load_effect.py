import unittest
import os

from ledshimdemo.canvas import Canvas
from ledshimdemo.load_effect import load_effect, load_effects

from tests.test_effects.dummy1_effect import Dummy1Effect
from tests.test_effects.dummy2_effect import Dummy2Effect
from tests.test_effects.dummy3_effect import Dummy3Effect


class TestLoadEffect(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def test_load_effects(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        effects = load_effects(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", canvas)
        self.assertEqual(len(effects), 3)
        self.assertIsInstance(effects[0], Dummy1Effect)
        self.assertIsInstance(effects[1], Dummy2Effect)
        self.assertIsInstance(effects[2], Dummy3Effect)

    def test_load_non_existent_effect(self):
        with self.assertRaises(ImportError):
            load_effect("tests.test_effects.dummy_effect", "DummyEffect")

    def test_load_existent_effect(self):
        canvas = Canvas(self.TEST_CANVAS_SIZE)
        test_effect = load_effect("tests.test_effects.dummy1_effect", "Dummy1Effect", canvas)
        self.assertIsInstance(test_effect, Dummy1Effect)
