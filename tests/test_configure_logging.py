from unittest import TestCase
from testfixtures import LogCapture

import ledshimdemo.configure_logging as my_logging


class TestMain(TestCase):

    def test_invalid_log_level(self):
        with self.assertRaises(ValueError):
            my_logging.configure_logging("INVALID")

    def test_verbose_log_level(self):
        test_message = "Test message..."
        with LogCapture() as log_out:
            my_logging.configure_logging(my_logging.VERBOSE)
            my_logging.verbose(test_message)
        log_out.check(("root", my_logging.VERBOSE, "Logging level enabled!"),
                      ("root", my_logging.VERBOSE, test_message),)
