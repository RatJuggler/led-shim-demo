"""
Add a custom VERBOSE logging level.
"""
import logging

LOGGING_LEVEL_VERBOSE = 15


def verbose(msg, *args, **kwargs):
    if logging.getLogger().isEnabledFor(LOGGING_LEVEL_VERBOSE):
        logging.log(LOGGING_LEVEL_VERBOSE, msg)


logging.addLevelName(LOGGING_LEVEL_VERBOSE, "VERBOSE")
logging.verbose = verbose
logging.Logger.verbose = verbose
