import unittest
import mock
import sys
import logging
from click.testing import CliRunner

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.
import ledshimdemo.__main__ as main


@mock.patch('ledshimdemo.__main__.render')
class TestMain(unittest.TestCase):

    def setUp(self):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        self.runner = CliRunner()

    def test_help(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" --version ", result.output)
        self.assertIn(" --effect-list ", result.output)
        self.assertIn(" --effect-display ", result.output)
        self.assertIn(" --effect-duration ", result.output)
        self.assertIn(" --repeat-run ", result.output)
        self.assertIn(" --brightness ", result.output)
        self.assertIn(" --invert ", result.output)
        self.assertIn(" --log-level ", result.output)
        self.assertIn(" --help ", result.output)
        render_mock.assert_not_called()

    def test_version(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['--version'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("display-effects, version ", result.output)
        render_mock.assert_not_called()

    def test_effect_list(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['--effect-list'])
        self.assertEqual(result.exit_code, 0)
        effects = ["Available Effects:",
                   "BinaryClock    - Shows hours, minutes and seconds.",
                   "Candle         - A flickering candle.",
                   "CheerLights    - Synchronize with the CheerLights \"Internet of Things\" project.",
                   "ColouredLights - Simple coloured lights like Xmas lights.",
                   "DigitalRain    - Cut price Matrix effect.",
                   "GradientGraph  - Sine wave colour gradient effect.",
                   "Rainbow        - A slowly moving rainbow.",
                   "RandomBlink    - Some random blinking.",
                   "SolidColours   - A sequence of solid colours."]
        effects_list = "\n".join(effects)
        self.assertIn(effects_list, result.output)
        render_mock.assert_not_called()

    def test_default_options_no_log(self, render_mock):
        result = self.runner.invoke(main.display_effects, [])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "")
        render_mock.assert_called_once()

    def test_default_options_info_log(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['--log-level', 'INFO'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Logging level enabled!", result.output)
        self.assertIn(" - INFO - Active Options(effect-display=CYCLE, effect-duration=10, repeat-run=1, brightness=8, "
                      "invert=False, log-level=INFO, effects_selected=ALL)", result.output)
        render_mock.assert_called_once()

    def test_default_options_debug_log(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['--log-level', 'DEBUG'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - DEBUG - Logging level enabled!", result.output)
        self.assertIn(" - INFO - Active Options(effect-display=CYCLE, effect-duration=10, repeat-run=1, brightness=8, "
                      "invert=False, log-level=DEBUG, effects_selected=ALL)", result.output)
        render_mock.assert_called_once()

    def test_all_options_verbose_log(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['--effect-display', 'RANDOM',
                                                           '--effect-duration', '180',
                                                           '--repeat-run', '240',
                                                           '--brightness', '3',
                                                           '--invert',
                                                           '--log-level', 'VERBOSE',
                                                           'Candle', 'Rainbow'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - VERBOSE - Logging level enabled!", result.output)
        self.assertIn(" - INFO - Active Options(effect-display=RANDOM, effect-duration=180, repeat-run=240, "
                      "brightness=3, invert=True, log-level=VERBOSE, effects_selected=('Candle', 'Rainbow'))",
                      result.output)
        render_mock.assert_called_once()

    def test_invalid_effect_name(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['Rainbow', 'Unicorn'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn('Error: Invalid value for "[EFFECTS_SELECTED]...": Unknown effect: Unicorn', result.output)
        render_mock.assert_not_called()

    def test_invalid_effect_names(self, render_mock):
        result = self.runner.invoke(main.display_effects, ['Candle', 'Apple', 'Banana'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn('Error: Invalid value for "[EFFECTS_SELECTED]...": Unknown effects: Apple, Banana', result.output)
        render_mock.assert_not_called()
