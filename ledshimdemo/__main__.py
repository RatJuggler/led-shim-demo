import click
import logging

from .canvas import Canvas
from .effects import BinaryClockEffect, CandleEffect, CheerLightsEffect, ColouredLightsEffect, DigitalRainEffect, GradientGraphEffect, RainbowEffect, RandomBlinkEffect, SolidColoursEffect
from .pixel import Pixel
from .render import render

NUM_PIXELS = 28  # The number of LEDs on the shim.

CANVAS = Canvas(NUM_PIXELS)
EFFECTS = [BinaryClockEffect(CANVAS),
           CandleEffect(CANVAS),
           CheerLightsEffect(CANVAS),
           ColouredLightsEffect(CANVAS),
           DigitalRainEffect(CANVAS),
           GradientGraphEffect(CANVAS),
           RainbowEffect(CANVAS),
           RandomBlinkEffect(CANVAS),
           SolidColoursEffect(CANVAS)]


def configure_logging(loglevel: str) -> None:
    """
    Configure basic logging to the console.
    :param loglevel: from the command line or default
    :return: No meaningful return
    """
    numeric_level = logging.getLevelName(loglevel.upper())
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')
    if numeric_level < logging.WARNING:
        logging.log(numeric_level, "Logging level enabled!")


def show_options(display: str, duration: int, run: int, brightness: int, invert: bool, level: str) -> str:
    """
    Human readable string showing the command line options to be used.
    :param display: from command line option or default
    :param duration: from command line option or default
    :param run: from command line option or default
    :param brightness: from command line option or default
    :param invert: from command line option or default
    :param level: from command line option or default
    :return: One line string of the command line options to be used.
    """
    options = ["Active Options(",
               "effect-display={0}, ".format(display),
               "effect-duration={0}, ".format(duration),
               "effect-run={0}, ".format(run),
               "brightness={0}, ".format(brightness),
               "invert={0}, ".format(invert),
               "log-level={0}".format(level),
               ")"]
    return "".join(options)


def list_effects(ctx, param, value):
    """
    List the effects currently available.
    :param ctx: see callbacks for the click options
    :param param: see callbacks for the click options
    :param value: see callbacks for the click options
    :return: A string listing all the effect names and descriptions.
    """
    if not value or ctx.resilient_parsing:
        return
    effects = ["Available Effects:"]
    for effect in EFFECTS:
        effects.append(effect.get_name() + " - " + effect.get_description())
    click.echo("\n".join(effects))
    ctx.exit()


@click.command(help="Show various effects on a Pimoroni LED shim.")
@click.version_option()
@click.option('-l', '--effect-list', is_flag=True, is_eager=True, expose_value=False, callback=list_effects,
              help='List the effects available.')
@click.option('-d', '--effect-display', 'display', type=click.Choice(["CYCLE", "RANDOM"]),
              help="How the effects are displayed.", default="CYCLE", show_default=True)
@click.option('-u', '--effect-duration', 'duration', type=click.IntRange(1, 180),
              help="How long to display each effect for, in seconds (1-180).", default=10, show_default=True)
@click.option('-r', '--effect-run', 'run', type=click.IntRange(1, 240),
              help="How many times to run effects before stopping (1-240).", default=24, show_default=True)
@click.option('-b', '--brightness', type=click.IntRange(1, 10),
              help="How bright the effects will be (1-10).", default=8, show_default=True)
@click.option('-i', '--invert', is_flag=True,
              help="Change the display orientation.")
@click.option('-o', '--log-level', 'level', type=click.Choice(["DEBUG", "VERBOSE", "INFO", "WARNING"]),
              help="Show additional logging information.", default="WARNING", show_default=True)
def display_effects(display: str, duration: int, run: int, brightness: int, invert: bool, level: str) -> None:
    """
    Show various effects on a Pimoroni LED shim.
    :param display: In a CYCLE or at RANDOM
    :param duration: How long to display each effect for
    :param run: How many times to run effects
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param level: Set a logging level; DEBUG, VERBOSE, INFO or WARNING
    :return: No meaningful return
    """
    configure_logging(level)
    logging.info(show_options(display, duration, run, brightness, invert, level))
    Pixel.set_default_brightness(brightness / 10.0)
    render(display, duration, run, invert, EFFECTS)


if __name__ == '__main__':
    display_effects()   # pragma: no cover
