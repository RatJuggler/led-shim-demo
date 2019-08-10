import unittest
from click.testing import CliRunner

from ledshimdemo.__main__ import display_effects


class Test(unittest.TestCase):

    def test_help(self):
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

    def test_default_options_no_log(self):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--test'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, "")

    def test_default_options_log(self):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--loglevel', 'INFO',
                                                 '--test'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Active Options(effect_display=CYCLE, effect_duration=10, effect_run=24, brightness=8, invert=False, loglevel=INFO)", result.output)

    def test_all_options(self):
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
