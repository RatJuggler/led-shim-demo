import click
import logging

from .canvas import Canvas
from .effects import BinaryClock, Candle, CheerLights, ColouredLights, GradientGraph, Rainbow, RandomBlink, SolidColours
from .pixel import Pixel
from .render import render

NUM_PIXELS = 28     # The number of LEDs on the shim.


def configure_logging(loglevel: str):
    """
    Configure basic logging to the console.
    :param loglevel: from the command line or default
    :return: No meaningful return
    """
    numeric_level = getattr(logging, loglevel.upper(), logging.WARNING)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')


def show_options(effect_display: str, effect_duration: int, effect_run: int,
                 brightness: int, invert: bool, loglevel: str):
    """
    Human readable string showing the command line options to be used.
    :param effect_display: from command line option or default
    :param effect_duration: from command line option or default
    :param effect_run: from command line option or default
    :param brightness: from command line option or default
    :param invert: from command line option or default
    :param loglevel: from command line option or default
    :return: One line string of the command line options to be used.
    """
    options = ["Active Options(",
               "effect_display={0}, ".format(effect_display),
               "effect_duration={0}, ".format(effect_duration),
               "effect_run={0}, ".format(effect_run),
               "brightness={0}, ".format(brightness),
               "invert={0}, ".format(invert),
               "loglevel={0}".format(loglevel),
               ")"]
    return "".join(options)


@click.command(help="Show various effects on a Pimoroni LED shim.")
@click.version_option()
@click.option('-d', '--effect_display', type=click.Choice(["CYCLE", "RANDOM"]), default="CYCLE",
              help="How the effects are displayed.", show_default=True)
@click.option('-u', '--effect_duration', type=click.IntRange(1, 180), default=10,
              help="How long to display each effect for, in seconds (1-180).", show_default=True)
@click.option('-r', '--effect_run', type=click.IntRange(1, 240), default=24,
              help="How many times to run effects before stopping (1-240).", show_default=True)
@click.option('-b', '--brightness', type=click.IntRange(1, 10), default=8,
              help="How bright the effects will be (1-10).", show_default=True)
@click.option('-i', '--invert', is_flag=True,
              help="Change the display orientation.")
@click.option('-l', '--loglevel', type=click.Choice(["DEBUG", "INFO", "WARNING"]), default="WARNING",
              help="Show additional logging information.", show_default=True)
@click.option('--test', is_flag=True, hidden=True,
              help="Hidden flag for testing options.")
def display_effects(effect_display: str, effect_duration: int, effect_run: int,
                    brightness: int, invert: bool, loglevel: str, test: bool):
    """
    Show various effects on a Pimoroni LED shim.
    :param effect_display: In a CYCLE or at RANDOM
    :param effect_duration: How long to display each effect for
    :param effect_run: How many times to run effects
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param loglevel: Set a logging level; DEBUG, INFO or WARNING
    :param test: Indicates option testing only
    :return: No meaningful return
    """
    configure_logging(loglevel)
    logging.info(show_options(effect_display, effect_duration, effect_run, brightness, invert, loglevel))
    Pixel.set_default_brightness(brightness / 10.0)
    canvas = Canvas(NUM_PIXELS)
    effects = [BinaryClock(canvas),
               Candle(canvas),
               CheerLights(canvas),
               ColouredLights(canvas),
               GradientGraph(canvas),
               Rainbow(canvas),
               RandomBlink(canvas),
               SolidColours(canvas)]
    if not test:
        render(effect_display, effect_duration, effect_run, invert, effects)


if __name__ == '__main__':
    display_effects()
