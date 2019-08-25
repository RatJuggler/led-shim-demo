import unittest

from ledshimdemo.effect_display import AbstractEffectDisplay, CycleEffects, RandomEffects


class TestEffectDisplayGetNextEffect(unittest.TestCase):

    EFFECT_COUNT = 3  # type: int

    def setUp(self):
        pass

    def test_select_effect_display_invalid(self):
        with self.assertRaises(AssertionError):
            AbstractEffectDisplay.select_effect_display("Banana", self.EFFECT_COUNT)

    def test_select_effect_display_cycle(self):
        self.assertIsInstance(AbstractEffectDisplay.select_effect_display(AbstractEffectDisplay.CYCLE_DISPLAY, self.EFFECT_COUNT),
                              CycleEffects)

    def test_select_effect_display_random(self):
        self.assertIsInstance(AbstractEffectDisplay.select_effect_display(AbstractEffectDisplay.RANDOM_DISPLAY, self.EFFECT_COUNT),
                              RandomEffects)

    def test_next_cycle_effect(self):
        effect_display = CycleEffects(3)
        self.assertEqual(effect_display.get_next_effect(), 0)
        self.assertEqual(effect_display.get_next_effect(), 1)
        self.assertEqual(effect_display.get_next_effect(), 2)
        self.assertEqual(effect_display.get_next_effect(), 0)

    def test_next_random_effect(self):
        effects = 3
        effect_display = RandomEffects(effects)
        self.assertTrue(effect_display.get_next_effect() in range(effects))
        self.assertTrue(effect_display.get_next_effect() in range(effects))
        self.assertTrue(effect_display.get_next_effect() in range(effects))
