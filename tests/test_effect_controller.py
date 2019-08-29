from unittest import TestCase
from testfixtures import LogCapture
import mock
import os

from ledshimdemo.canvas import Canvas
import ledshimdemo.configure_logging as cl
from ledshimdemo.effect_cache import EffectCache
from ledshimdemo.effect_controller import EffectController


class TestEffectControllerConstructorAndOptionsUsed(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def setUp(self):
        self.effect_cache = EffectCache(os.path.dirname(__file__) + "/test_effects",
                                        "tests.test_effects.", Canvas(self.TEST_CANVAS_SIZE))

    def test_valid_options1(self):
        controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
        expected_result = "test1(parade=CYCLE, duration=10 secs, repeat=1, brightness=8, invert=False, effects=ALL)"
        options_used = controller.options_used("test1")
        self.assertEqual(options_used, expected_result)

    def test_valid_options2(self):
        controller = EffectController("RANDOM", 15, 3, 9, True, ['Candle', 'Rainbow'], self.effect_cache)
        expected_result =\
            "test2(parade=RANDOM, duration=15 secs, repeat=3, brightness=9, invert=True, effects=['Candle', 'Rainbow'])"
        options_used = controller.options_used("test2")
        self.assertEqual(options_used, expected_result)

    def test_invalid_options(self):
        controller = EffectController("TEST", 27, -1, 100, True, [], self.effect_cache)
        expected_result = "invalid(parade=TEST, duration=27 secs, repeat=-1, brightness=100, invert=True, effects=ALL)"
        options_used = controller.options_used("invalid")
        self.assertEqual(options_used, expected_result)


@mock.patch('ledshimdemo.effect_controller.AbstractEffectParade')
class TestEffectControllerProcessDisplay(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def setUp(self):
        self.effect_cache = EffectCache(os.path.dirname(__file__) + "/test_effects",
                                        "tests.test_effects.", Canvas(self.TEST_CANVAS_SIZE))

    def test_display_default_options_default_log(self, effect_parade_mock):
        expected = "display(parade=CYCLE, duration=10 secs, repeat=1, brightness=8, invert=False, effects=ALL)"
        with LogCapture(level=cl.logging.INFO) as log_out:
            controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
            controller.process("display")
        log_out.check(("root", cl.logging.getLevelName(cl.logging.INFO), expected))
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()

    def test_display_default_options_warning_log(self, effect_parade_mock):
        with LogCapture(level=cl.logging.WARNING) as log_out:
            controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
            controller.process("display")
        log_out.check()
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()

    def test_display_default_options_debug_log(self, effect_parade_mock):
        expected = "display(parade=CYCLE, duration=10 secs, repeat=1, brightness=8, invert=False, effects=ALL)"
        with LogCapture(level=cl.logging.DEBUG) as log_out:
            controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
            controller.process("display")
        log_out.check(("root", cl.logging.getLevelName(cl.logging.INFO), expected))
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()

    def test_display_all_options_verbose_log(self, effect_parade_mock):
        expected = "display(parade=RANDOM, duration=180 secs, repeat=240, brightness=3, " \
                   "invert=True, effects=['Dummy1Effect', 'Dummy2Effect'])"
        with LogCapture(level=cl.VERBOSE) as log_out:
            controller = EffectController("RANDOM", 180, 240, 3, True,
                                          ['Dummy1Effect', 'Dummy2Effect'], self.effect_cache)
            controller.process("display")
        log_out.check(("root", cl.logging.getLevelName(cl.logging.INFO), expected))
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()


@mock.patch('ledshimdemo.effect_controller.AbstractEffectParade')
class TestEffectControllerProcessLead(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def setUp(self):
        self.effect_cache = EffectCache(os.path.dirname(__file__) + "/test_effects",
                                        "tests.test_effects.", Canvas(self.TEST_CANVAS_SIZE))

    def test_lead_default_options_default_log(self, effect_parade_mock):
        expected = "lead(parade=CYCLE, duration=10 secs, repeat=1, brightness=8, invert=False, effects=ALL)"
        with LogCapture(level=cl.logging.INFO) as log_out:
            controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
            controller.process("lead")
        log_out.check(("root", cl.logging.getLevelName(cl.logging.INFO), expected))
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()

    def test_lead_default_options_warning_log(self, effect_parade_mock):
        with LogCapture(level=cl.logging.WARNING) as log_out:
            controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
            controller.process("lead")
        log_out.check()
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()

    def test_lead_default_options_debug_log(self, effect_parade_mock):
        expected = "lead(parade=CYCLE, duration=10 secs, repeat=1, brightness=8, invert=False, effects=ALL)"
        with LogCapture(level=cl.logging.DEBUG) as log_out:
            controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
            controller.process("lead")
        log_out.check(("root", cl.logging.getLevelName(cl.logging.INFO), expected))
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()

    def test_lead_all_options_verbose_log(self, effect_parade_mock):
        expected = "lead(parade=RANDOM, duration=180 secs, repeat=240, brightness=3, " \
                   "invert=True, effects=['Dummy1Effect', 'Dummy2Effect'])"
        with LogCapture(level=cl.VERBOSE) as log_out:
            controller = EffectController("RANDOM", 180, 240, 3, True,
                                          ['Dummy1Effect', 'Dummy2Effect'], self.effect_cache)
            controller.process("lead")
        log_out.check(("root", cl.logging.getLevelName(cl.logging.INFO), expected))
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()


@mock.patch('ledshimdemo.effect_controller.AbstractEffectParade')
class TestEffectControllerProcessFollow(TestCase):

    TEST_CANVAS_SIZE = 3  # type: int

    def setUp(self):
        self.effect_cache = EffectCache(os.path.dirname(__file__) + "/test_effects",
                                        "tests.test_effects.", Canvas(self.TEST_CANVAS_SIZE))

    def test_follow_valid_ip_address(self, effect_parade_mock):
        expected = "follow(parade=CYCLE, duration=10 secs, repeat=1, brightness=8, invert=False, effects=ALL)"
        with LogCapture(level=cl.logging.INFO) as log_out:
            controller = EffectController("CYCLE", 10, 1, 8, False, [], self.effect_cache)
            controller.process("follow")
        log_out.check(("root", cl.logging.getLevelName(cl.logging.INFO), expected))
        effect_parade_mock.select_effect_parade.assert_called_once()
        effect_parade_mock.select_effect_parade.return_value.render.assert_called_once()
