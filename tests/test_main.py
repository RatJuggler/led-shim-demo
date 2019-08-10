import unittest
from click.testing import CliRunner

from ledshimdemo.__main__ import display_effects


class Test(unittest.TestCase):

    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" --version ", result.output)
        self.assertIn(" --show_effects ", result.output)
        self.assertIn(" --effect_time ", result.output)
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
        self.assertIn(" - INFO - Active Options(show_effects=CYCLE, effect_time=10, brightness=8, invert=False, loglevel=INFO)", result.output)

    def test_all_options(self):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--show_effects', 'RANDOM',
                                                 '--effect_time', '999',
                                                 '--brightness', '3',
                                                 '--invert',
                                                 '--loglevel', 'DEBUG',
                                                 '--test'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(" - INFO - Active Options(show_effects=RANDOM, effect_time=999, brightness=3, invert=True, loglevel=DEBUG)", result.output)
