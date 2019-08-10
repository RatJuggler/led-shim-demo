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


def show_options(show_effects: str, effect_time: int, brightness: int, invert: bool, loglevel: str):
    """
    Human readable string showing the command line options to be used.
    :param show_effects: from command line option or default
    :param effect_time: from command line option or default
    :param brightness: from command line option or default
    :param invert: from command line option or default
    :param loglevel: from command line option or default
    :return: One line string of the command line options to be used.
    """
    options = ["Active Options(",
               "show_effects={0}, ".format(show_effects),
               "effect_time={0}, ".format(effect_time),
               "brightness={0}, ".format(brightness),
               "invert={0}, ".format(invert),
               "loglevel={0}".format(loglevel),
               ")"]
    return "".join(options)


@click.command(help="Show various effects on a Pimoroni LED shim.")
@click.version_option()
@click.option('-s', '--show_effects', type=click.Choice(["CYCLE", "RANDOM"]), default="CYCLE",
              help="How the effects are displayed.", show_default=True)
@click.option('-t', '--effect_time', type=click.IntRange(1, 3600), default=10,
              help="How long to display each effect for, in seconds (1-3600).", show_default=True)
@click.option('-b', '--brightness', type=click.IntRange(1, 10), default=8,
              help="How bright the effects will be (1-10).", show_default=True)
@click.option('-i', '--invert', is_flag=True,
              help="Change the display orientation.")
@click.option('-l', '--loglevel', type=click.Choice(["NOTSET", "INFO", "DEBUG"]), default="NOTSET",
              help="Show additional logging information.")
@click.option('--test', is_flag=True, hidden=True,
              help="Hidden flag for testing options")
def display_effects(show_effects: str, effect_time: int, brightness: int, invert: bool, loglevel: str, test: bool):
    """
    Show various effects on a Pimoroni LED shim.
    :param show_effects: In a CYCLE or at RANDOM
    :param effect_time: How long to display each effect for
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param loglevel: Set a logging level; NOTSET, INFO or DEBUG
    :param test: Indicates option testing only
    :return: No meaningful return
    """
    configure_logging(loglevel)
    logging.info(show_options(show_effects, effect_time, brightness, invert, loglevel))
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
        render(show_effects, effects, effect_time, invert)


if __name__ == '__main__':
    display_effects()
