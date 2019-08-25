import unittest

from ledshimdemo import effect_display


class TestEffectDisplayGetNextEffect(unittest.TestCase):

    def setUp(self):
        pass

    def test_select_effect_display_invalid(self):
        with self.assertRaises(AssertionError):
            effect_display.select_effect_display("Banana")

    def test_select_effect_display_cycle(self):
        self.assertEqual(effect_display.select_effect_display(effect_display.CYCLE_DISPLAY),
                         effect_display.next_cycle_effect)

    def test_select_effect_display_random(self):
        self.assertEqual(effect_display.select_effect_display(effect_display.RANDOM_DISPLAY),
                         effect_display.next_random_effect)

    def test_next_cycle_effect(self):
        effects = 3
        self.assertEqual(effect_display.next_cycle_effect(0, effects), 1)
        self.assertEqual(effect_display.next_cycle_effect(1, effects), 2)
        self.assertEqual(effect_display.next_cycle_effect(2, effects), 0)
        self.assertEqual(effect_display.next_cycle_effect(0, effects), 1)

    def test_next_random_effect(self):
        effects = 3
        self.assertTrue(effect_display.next_random_effect(0, effects) in range(effects))
        self.assertTrue(effect_display.next_random_effect(0, effects) in range(effects))
        self.assertTrue(effect_display.next_random_effect(0, effects) in range(effects))
        self.assertTrue(effect_display.next_random_effect(0, effects) in range(effects))
