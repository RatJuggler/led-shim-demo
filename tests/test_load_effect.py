import unittest
import os

from ledshimdemo.load_effect import load_effect, load_effects


class TestLoadEffect(unittest.TestCase):

    def test_load_effects(self):
        effects = load_effects(os.path.dirname(__file__) + "/effects", "ledshimdemo.effects.")
        self.assertEqual(True, False)

    def test_load_effect(self):
        with self.assertRaises(ImportError):
            load_effect("test.test_effects.dummy_effect", "DummyEffect")
