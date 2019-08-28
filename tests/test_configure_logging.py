from unittest import TestCase
from testfixtures import LogCapture

import ledshimdemo.configure_logging as cl


class TestConfigureLogging(TestCase):

    TEST_MESSAGE = "This is a test..."

    @staticmethod
    def get_log_name(log_level):
        return cl.logging.getLevelName(log_level)

    def test_invalid_log_level(self):
        with self.assertRaises(ValueError):
            cl.configure_logging("INVALID")

    def test_debug_log_level(self):
        with LogCapture() as log_out:
            cl.configure_logging(cl.logging.DEBUG)
            cl.logging.debug(self.TEST_MESSAGE)
        log_out.check(("root", self.get_log_name(cl.logging.DEBUG), self.TEST_MESSAGE),)

    def test_verbose_log_level(self):
        with LogCapture() as log_out:
            cl.configure_logging(cl.VERBOSE)
            cl.verbose(self.TEST_MESSAGE)
        log_out.check(("root", self.get_log_name(cl.VERBOSE), self.TEST_MESSAGE),)

    def test_info_log_level(self):
        with LogCapture() as log_out:
            cl.configure_logging(cl.logging.INFO)
            cl.logging.info(self.TEST_MESSAGE)
        log_out.check(("root", self.get_log_name(cl.logging.INFO), self.TEST_MESSAGE),)
