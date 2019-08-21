import unittest
import os

from ledshimdemo.canvas import Canvas
from ledshimdemo.load_effect import validate_effect_names, load_effect, load_effects

from tests.test_effects.dummy1_effect import Dummy1Effect
from tests.test_effects.dummy2_effect import Dummy2Effect
from tests.test_effects.dummy3_effect import Dummy3Effect


class TestLoadEffect(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int
    canvas = Canvas(TEST_CANVAS_SIZE)  # type: Canvas

    def build_dummy_effects_available(self):
        return {"Dummy1Effect": Dummy1Effect(self.canvas),
                "Dummy2Effect": Dummy2Effect(self.canvas),
                "Dummy3Effect": Dummy3Effect(self.canvas)}

    def test_validate_effect_names_valid(self):
        effects_selected = ["Dummy1Effect"]
        effects_available = self.build_dummy_effects_available()
        names_in_error = validate_effect_names(effects_selected, effects_available)
        self.assertFalse(names_in_error)

    def test_validate_effect_names_invalid(self):
        effects_selected = ["Apple", "Banana"]
        effects_available = self.build_dummy_effects_available()
        names_in_error = validate_effect_names(effects_selected, effects_available)
        self.assertEqual(names_in_error, effects_selected)

    def test_load_dummy_effects(self):
        effects = load_effects(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", self.canvas)
        self.assertEqual(len(effects), 3)
        self.assertIsInstance(effects["Dummy1Effect"], Dummy1Effect)
        self.assertIsInstance(effects["Dummy2Effect"], Dummy2Effect)
        self.assertIsInstance(effects["Dummy3Effect"], Dummy3Effect)

    def test_load_non_existent_effect(self):
        with self.assertRaises(ImportError):
            load_effect("tests.test_effects.dummy_effect", "DummyEffect")

    def test_load_existent_effect(self):
        dummy_effect = load_effect("tests.test_effects.dummy1_effect", "Dummy1Effect", self.canvas)
        self.assertIsInstance(dummy_effect, Dummy1Effect)

    def test_load_misnamed_effect(self):
        with self.assertRaises(TypeError):
            load_effect("tests.effects.not_an_effect", "NotAnEffect")
