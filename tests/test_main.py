from unittest import TestCase
import mock
import logging
from click.testing import CliRunner

import ledshimdemo.__main__ as main


class TestBaseCommand(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_help(self):
        result = self.runner.invoke(main.ledshimdemo, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" --version ", result.output)
        self.assertIn(" --effect-list ", result.output)
        self.assertIn(" --log-level ", result.output)
        self.assertIn(" --help ", result.output)

    def test_version(self):
        result = self.runner.invoke(main.ledshimdemo, ['--version'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("ledshimdemo, version ", result.output)

    def test_effect_list(self):
        result = self.runner.invoke(main.ledshimdemo, ['--effect-list'])
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


@mock.patch('ledshimdemo.__main__.AbstractEffectDisplay')
class TestDisplayCommand(TestCase):

    def setUp(self):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        self.runner = CliRunner()

    def test_display_help(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['display', '--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" --effect-display ", result.output)
        self.assertIn(" --effect-duration ", result.output)
        self.assertIn(" --repeat-run ", result.output)
        self.assertIn(" --brightness ", result.output)
        self.assertIn(" --invert ", result.output)
        self.assertIn(" --help ", result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()

    def test_display_default_options_default_log(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['display'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Logging level enabled!", result.output)
        self.assertIn(" - INFO - Active Options(effect-display=CYCLE, effect-duration=10 secs, repeat-run=1, "
                      "brightness=8, invert=False, effects_selected=ALL)", result.output)
        effect_display_mock.select_effect_display.assert_called_once()
        effect_display_mock.select_effect_display.return_value.render.assert_called_once()

    def test_display_default_options_warning_log(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['--log-level', 'WARNING', 'display'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "")
        effect_display_mock.select_effect_display.assert_called_once()
        effect_display_mock.select_effect_display.return_value.render.assert_called_once()

    def test_display_default_options_debug_log(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['--log-level', 'DEBUG', 'display'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - DEBUG - Logging level enabled!", result.output)
        self.assertIn(" - INFO - Active Options(effect-display=CYCLE, effect-duration=10 secs, repeat-run=1, "
                      "brightness=8, invert=False, effects_selected=ALL)", result.output)
        effect_display_mock.select_effect_display.assert_called_once()
        effect_display_mock.select_effect_display.return_value.render.assert_called_once()

    def test_display_all_options_verbose_log(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, [
            '--log-level', 'VERBOSE',
            'display',
            '--effect-display', 'RANDOM',
            '--effect-duration', '180',
            '--repeat-run', '240',
            '--brightness', '3',
            '--invert',
            'Candle', 'Rainbow'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - VERBOSE - Logging level enabled!", result.output)
        self.assertIn(" - INFO - Active Options(effect-display=RANDOM, effect-duration=180 secs, repeat-run=240, "
                      "brightness=3, invert=True, effects_selected=('Candle', 'Rainbow'))", result.output)
        effect_display_mock.select_effect_display.assert_called_once()
        effect_display_mock.select_effect_display.return_value.render.assert_called_once()

    def test_display_invalid_effect_name(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['display', 'Rainbow', 'Unicorn'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn('Error: Invalid value for "[EFFECTS_SELECTED]...": Unknown effect: Unicorn', result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()

    def test_display_invalid_effect_names(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['display', 'Candle', 'Apple', 'Banana'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn('Error: Invalid value for "[EFFECTS_SELECTED]...": Unknown effects: Apple, Banana', result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()


@mock.patch('ledshimdemo.__main__.AbstractEffectDisplay')
class TestLeadCommand(TestCase):

    def setUp(self):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        self.runner = CliRunner()

    def test_lead_help(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['lead', '--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" --effect-display ", result.output)
        self.assertIn(" --effect-duration ", result.output)
        self.assertIn(" --repeat-run ", result.output)
        self.assertIn(" --brightness ", result.output)
        self.assertIn(" --invert ", result.output)
        self.assertIn(" --port ", result.output)
        self.assertIn(" --help ", result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()

    def test_lead_valid_ip_address(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['lead', '127.0.0.1'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Logging level enabled!", result.output)
        effect_display_mock.select_effect_display.assert_called_once()
        effect_display_mock.select_effect_display.return_value.render.assert_called_once()

    def test_lead_invalid_ip_address(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['lead', 'localhost'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn('Error: Invalid value for "IP_ADDRESS": localhost is not a valid IP address', result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()



@mock.patch('ledshimdemo.__main__.AbstractEffectDisplay')
class TestFollowCommand(TestCase):

    def setUp(self):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        self.runner = CliRunner()

    def test_follow_help(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['follow', '--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" --port ", result.output)
        self.assertIn(" --help ", result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()

    def test_follow_valid_ip_address(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['follow', '127.0.0.1'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Logging level enabled!", result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()

    def test_follow_invalid_ip_address(self, effect_display_mock):
        result = self.runner.invoke(main.ledshimdemo, ['follow', 'localhost'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn('Error: Invalid value for "IP_ADDRESS": localhost is not a valid IP address', result.output)
        effect_display_mock.select_effect_display.assert_not_called()
        effect_display_mock.select_effect_display.return_value.render.assert_not_called()
