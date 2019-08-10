import unittest
from click.testing import CliRunner

from ledshimdemo.__main__ import display_effects


class Test(unittest.TestCase):

    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(display_effects, ['--help'])
        assert result.exit_code == 0
        assert '--version ' in result.output
        assert '--show_effects ' in result.output
        assert '--effect_time ' in result.output
        assert '--brightness ' in result.output
        assert '--invert ' in result.output
        assert '--loglevel ' in result.output
        assert '--help ' in result.output
