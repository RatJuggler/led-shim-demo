import unittest
import mock
import sys
import logging
from click.testing import CliRunner

sys.modules['smbus'] = mock.Mock()  # Mock the hardware layer to avoid errors.

from ledshimdemo.__main__ import display_effects


@mock.patch('ledshimdemo.render.render')
class Test(unittest.TestCase):

    def setUp(self):
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    def test_help(self, render_mock):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" --version ", result.output)
        self.assertIn(" --effect_display ", result.output)
        self.assertIn(" --effect_duration ", result.output)
        self.assertIn(" --effect_run ", result.output)
        self.assertIn(" --brightness ", result.output)
        self.assertIn(" --invert ", result.output)
        self.assertIn(" --loglevel ", result.output)
        self.assertIn(" --help ", result.output)
        self.assertNotIn(" --test ", result.output)
        render_mock.assert_not_called()

    def test_version(self, render_mock):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--version'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("display-effects, version ", result.output)
        render_mock.assert_not_called()

    def test_effect_list(self, render_mock):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--effect_list'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Available Effects:\nbinary_clock\ncandle\ncheerlights\ncoloured_lights\ndigital_rain\ngradient_graph\nrainbow\nrandom_blink\nsolid_colours\n", result.output)
        render_mock.assert_not_called()

    def test_default_options_no_log(self, render_mock):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--test'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "")
        render_mock.assert_not_called()

    def test_default_options_log(self, render_mock):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--loglevel', 'INFO',
                                                 '--test'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Active Options(effect_display=CYCLE, effect_duration=10, effect_run=24, brightness=8, invert=False, loglevel=INFO)", result.output)
        render_mock.assert_not_called()

    def test_all_options(self, render_mock):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--effect_display', 'RANDOM',
                                                 '--effect_duration', '180',
                                                 '--effect_run', '240',
                                                 '--brightness', '3',
                                                 '--invert',
                                                 '--loglevel', 'DEBUG',
                                                 '--test'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Active Options(effect_display=RANDOM, effect_duration=180, effect_run=240, brightness=3, invert=True, loglevel=DEBUG)", result.output)
        render_mock.assert_not_called()
