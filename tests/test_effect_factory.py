import unittest
import os

from ledshimdemo.canvas import Canvas
from ledshimdemo.effect_factory import EffectFactory

from tests.test_effects.dummy1_effect import Dummy1Effect
from tests.test_effects.dummy2_effect import Dummy2Effect
from tests.test_effects.dummy3_effect import Dummy3Effect


class TestEffectFactoryListAndValidate(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def setUp(self):
        self.canvas = Canvas(self.TEST_CANVAS_SIZE)
        self.effect_factory = \
            EffectFactory(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", self.canvas)

    def test_create_list_effects_display(self):
        effects = ["Available Effects:",
                   "Dummy1Effect - A dummy effect 1.",
                   "Dummy2Effect - A dummy effect 2.",
                   "Dummy3Effect - A dummy effect 3."]
        display = self.effect_factory.create_list_effects_display()
        self.assertEqual(display, "\n".join(effects))

    def test_validate_effect_names_valid(self):
        effects_selected = ["Dummy1Effect"]
        names_in_error = self.effect_factory.validate_effect_names(effects_selected)
        self.assertFalse(names_in_error)

    def test_validate_effect_names_valid_case_insensitive(self):
        effects_selected = ["duMmy1eFFect"]
        names_in_error = self.effect_factory.validate_effect_names(effects_selected)
        self.assertFalse(names_in_error)

    def test_validate_effect_names_valid_multiple_effects(self):
        effects_selected = ["Dummy3Effect", "duMmy1eFFect"]
        names_in_error = self.effect_factory.validate_effect_names(effects_selected)
        self.assertFalse(names_in_error)

    def test_validate_effect_names_valid_multiple_with_duplicates(self):
        effects_selected = ["Dummy3Effect", "Dummy1Effect", "Dummy2Effect", "Dummy1Effect"]
        names_in_error = self.effect_factory.validate_effect_names(effects_selected)
        self.assertFalse(names_in_error)

    def test_validate_effect_names_invalid(self):
        effects_selected = ["Apple", "Banana"]
        names_in_error = self.effect_factory.validate_effect_names(effects_selected)
        self.assertEqual(names_in_error, effects_selected)


class TestEffectFactoryLoad(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def setUp(self):
        self.canvas = Canvas(self.TEST_CANVAS_SIZE)
        self.effect_factory = \
            EffectFactory(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", self.canvas)

    def test_load_dummy_effects(self):
        effects = self.effect_factory.get_all_effects()
        self.assertIsInstance(effects, list)
        self.assertEqual(len(effects), 3)
        self.assertIsInstance(self.effect_factory.get_effect("DUMMY1EFFECT"), Dummy1Effect)
        self.assertIsInstance(self.effect_factory.get_effect("DUMMY2EFFECT"), Dummy2Effect)
        self.assertIsInstance(self.effect_factory.get_effect("DUMMY3EFFECT"), Dummy3Effect)

    def test_load_non_existent_effect(self):
        with self.assertRaises(ImportError):
            EffectFactory.load_effect("tests.test_effects.dummy_effect", "DummyEffect", self.canvas)

    def test_load_existent_effect(self):
        dummy_effect = EffectFactory.load_effect("tests.test_effects.dummy1_effect", "Dummy1Effect", self.canvas)
        self.assertIsInstance(dummy_effect, Dummy1Effect)

    def test_load_misnamed_effect(self):
        with self.assertRaises(TypeError):
            EffectFactory.load_effect("tests.effects.not_an_effect", "NotAnEffect")

    def test_get_all_effects(self):
        effects = self.effect_factory.get_all_effects()
        self.assertIsInstance(effects, list)
        self.assertEqual(len(effects), 3)

    def test_get_effect_valid(self):
        effect = self.effect_factory.get_effect("dummy1effect")
        self.assertIsInstance(effect, Dummy1Effect)

    def test_get_effect_invalid(self):
        with self.assertRaises(KeyError):
            self.effect_factory.get_effect("apple")
