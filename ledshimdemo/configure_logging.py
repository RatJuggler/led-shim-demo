"""
Add a custom VERBOSE logging level between DEBUG and INFO.
"""
import logging

VERBOSE = "VERBOSE"
LOGGING_LEVEL_VERBOSE = 15


def verbose(msg, *args, **kwargs) -> None:
    if logging.getLogger().isEnabledFor(LOGGING_LEVEL_VERBOSE):
        logging.log(LOGGING_LEVEL_VERBOSE, msg)


logging.addLevelName(LOGGING_LEVEL_VERBOSE, VERBOSE)
logging.verbose = verbose
logging.Logger.verbose = verbose


def configure_logging(loglevel: str) -> None:
    """
    Configure basic logging to the console.
    :param loglevel: level name from the command line or default
    :return: No meaningful return
    """
    numeric_level = logging.getLevelName(loglevel)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')
    if numeric_level < logging.WARNING:
        logging.log(numeric_level, "Logging level enabled!")
