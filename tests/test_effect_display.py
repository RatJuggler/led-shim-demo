from unittest import TestCase
import mock
import os
from typing import List, Type, TypeVar

from ledshimdemo.abstract_effect import AbstractEffect
from ledshimdemo.canvas import Canvas
from ledshimdemo.effect_display import AbstractEffectDisplay, CycleEffects, RandomEffects
from ledshimdemo.effect_cache import EffectCache

from tests.test_effects.dummy1_effect import Dummy1Effect
from tests.test_effects.dummy2_effect import Dummy2Effect
from tests.test_effects.dummy3_effect import Dummy3Effect


class TestEffectDisplayConstructor(TestCase):

    def setUp(self):
        pass

    def test_select_effect_display_invalid(self):
        with self.assertRaises(AssertionError):
            AbstractEffectDisplay.select_effect_display("Banana", [])

    def test_select_effect_display_cycle(self):
        self.assertIsInstance(AbstractEffectDisplay.select_effect_display(AbstractEffectDisplay.CYCLE_DISPLAY, []),
                              CycleEffects)

    def test_select_effect_display_random(self):
        self.assertIsInstance(AbstractEffectDisplay.select_effect_display(AbstractEffectDisplay.RANDOM_DISPLAY, []),
                              RandomEffects)


class TestEffectDisplayGetNextEffect(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    AE = TypeVar('AE', bound=AbstractEffect)

    def setUp(self):
        self.canvas = Canvas(self.TEST_CANVAS_SIZE)
        self.effects = [Dummy1Effect(self.canvas), Dummy2Effect(self.canvas), Dummy3Effect(self.canvas)]

    def call_next_and_test(self, effect_display: AbstractEffectDisplay, effect_type: List[Type[AE]]):
        effect = effect_display.get_next_effect()
        is_instance = False
        for cls_type in effect_type:
            if isinstance(effect, cls_type):
                is_instance = True
        self.assertTrue(is_instance)

    def test_get_next_effect_cycle_all_selected(self):
        effect_display = CycleEffects(self.effects)
        self.call_next_and_test(effect_display, [Dummy1Effect])
        self.call_next_and_test(effect_display, [Dummy2Effect])
        self.call_next_and_test(effect_display, [Dummy3Effect])
        self.call_next_and_test(effect_display, [Dummy1Effect])

    def test_get_next_effect_random_all_selected(self):
        effect_display = RandomEffects(self.effects)
        self.call_next_and_test(effect_display, [Dummy1Effect, Dummy2Effect, Dummy3Effect])
        self.call_next_and_test(effect_display, [Dummy1Effect, Dummy2Effect, Dummy3Effect])
        self.call_next_and_test(effect_display, [Dummy1Effect, Dummy2Effect, Dummy3Effect])

    def test_get_next_effect_cycle_selected(self):
        effect_display = CycleEffects([Dummy3Effect(self.canvas), Dummy1Effect(self.canvas)])
        self.call_next_and_test(effect_display, [Dummy3Effect])
        self.call_next_and_test(effect_display, [Dummy1Effect])
        self.call_next_and_test(effect_display, [Dummy3Effect])

    def test_get_next_effect_random_selected(self):
        effect_display = RandomEffects([Dummy3Effect(self.canvas), Dummy1Effect(self.canvas)])
        self.call_next_and_test(effect_display, [Dummy3Effect, Dummy1Effect])
        self.call_next_and_test(effect_display, [Dummy3Effect, Dummy1Effect])


class TestEffectDisplayRender(TestCase):

    CANVAS_SIZE = 3
    EFFECT_DURATION = 2
    EFFECT_RUN = 1

    def setUp(self):
        canvas = Canvas(self.CANVAS_SIZE)
        self.effect_cache = EffectCache(os.path.dirname(__file__) + "/test_effects", "tests.test_effects.", canvas)
        effect_instances = self.effect_cache.get_effect_instances([])
        self.effects_display = CycleEffects(effect_instances)

    @mock.patch('ledshim.set_clear_on_exit')
    @mock.patch('ledshim.set_pixel')
    @mock.patch('ledshim.show')
    @mock.patch('ledshim.clear')
    def test_render(self, clear_mock, show_mock, set_pixel_mock, clear_on_exit_mock):
        set_pixel_mock.reset_mock()
        show_mock.reset_mock()
        self.effects_display.render(self.EFFECT_DURATION, self.EFFECT_RUN, False)
        clear_on_exit_mock.assert_called_once()
        set_pixel_call_count = 0
        show_call_count = 0
        for effect in self.effect_cache.get_all_effects():
            set_pixel_call_count += self.CANVAS_SIZE * (self.EFFECT_DURATION / effect.get_update_frequency())
            show_call_count += self.EFFECT_DURATION / effect.get_update_frequency()
        show_call_count += 1  # Final call to show cleared shim.
        self.assertEqual(set_pixel_call_count, set_pixel_mock.call_count)
        self.assertEqual(show_call_count, show_mock.call_count)
        clear_mock.assert_called_once()
