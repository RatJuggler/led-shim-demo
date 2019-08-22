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

    def test_get_all_effects(self):
        effects = self.effect_factory.get_all_effects()
        self.assertIsInstance(effects, list)
        self.assertEqual(len(effects), 3)
        self.assertIsInstance(effects[0], Dummy1Effect)
        self.assertIsInstance(effects[1], Dummy2Effect)
        self.assertIsInstance(effects[2], Dummy3Effect)

    def test_load_non_existent_effect(self):
        with self.assertRaises(ImportError):
            EffectFactory.load_effect("tests.test_effects.dummy_effect", "DummyEffect", self.canvas)

    def test_load_existent_effect(self):
        dummy_effect = EffectFactory.load_effect("tests.test_effects.dummy1_effect", "Dummy1Effect", self.canvas)
        self.assertIsInstance(dummy_effect, Dummy1Effect)

    def test_load_misnamed_effect(self):
        with self.assertRaises(TypeError):
            EffectFactory.load_effect("tests.effects.not_an_effect", "NotAnEffect")

    def test_get_effect_valid(self):
        effect = self.effect_factory.get_effect("dummy1effect")
        self.assertIsInstance(effect, Dummy1Effect)

    def test_get_effect_invalid(self):
        with self.assertRaises(KeyError):
            self.effect_factory.get_effect("apple")


class EffectFactoryGetNextEffect(unittest.TestCase):

    TEST_CANVAS_SIZE = 3  # type: int
    EFFECT_DISPLAY = 'CYCLE'

    def setUp(self):
        self.canvas = Canvas(self.TEST_CANVAS_SIZE)
        self.effect_factory = \
            EffectFactory(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", self.canvas)

    def test_get_next_effect_none_selected(self):
        with self.assertRaises(ValueError):
            self.effect_factory.get_next_effect(self.EFFECT_DISPLAY)

    def test_get_next_effect_cycle(self):
        self.effect_factory.set_effects_selected([])
        effect = self.effect_factory.get_next_effect(self.EFFECT_DISPLAY)
        self.assertIsInstance(effect, type(self.effect_factory.get_effect("Dummy1Effect")))
        effect = self.effect_factory.get_next_effect(self.EFFECT_DISPLAY)
        self.assertIsInstance(effect, type(self.effect_factory.get_effect("Dummy2Effect")))
        effect = self.effect_factory.get_next_effect(self.EFFECT_DISPLAY)
        self.assertIsInstance(effect, type(self.effect_factory.get_effect("Dummy3Effect")))
        effect = self.effect_factory.get_next_effect(self.EFFECT_DISPLAY)
        self.assertIsInstance(effect, type(self.effect_factory.get_effect("Dummy1Effect")))

    def test_get_next_effect_random(self):
        self.effect_factory.set_effects_selected([])
        effect = self.effect_factory.get_next_effect('RANDOM')
        self.assertTrue(isinstance(effect, (type(self.effect_factory.get_effect("Dummy1Effect")),
                                            type(self.effect_factory.get_effect("Dummy2Effect")),
                                            type(self.effect_factory.get_effect("Dummy3Effect")))))
