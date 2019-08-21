import click
import logging
import os
from typing import List

from .canvas import Canvas
from .configure_logging import configure_logging
from .effect_factory import EffectFactory
from .pixel import Pixel
from .render import render

NUM_PIXELS = 28  # The number of LEDs on the shim.

EFFECT_FACTORY = EffectFactory(os.path.dirname(__file__) + "/effects", "ledshimdemo.effects.", Canvas(NUM_PIXELS))


def show_options(display: str, duration: int, run: int, brightness: int,
                 invert: bool, level: str, effects_selected: List[str]) -> str:
    """
    Human readable string showing the command line options to be used.
    :param display: from command line option or default
    :param duration: from command line option or default
    :param run: from command line option or default
    :param brightness: from command line option or default
    :param invert: from command line option or default
    :param level: from command line option or default
    :param effects_selected: from command line arguments or default
    :return: One line string of the command line options to be used
    """
    options = ["Active Options(",
               "effect-display={0}, ".format(display),
               "effect-duration={0}, ".format(duration),
               "effect-run={0}, ".format(run),
               "brightness={0}, ".format(brightness),
               "invert={0}, ".format(invert),
               "log-level={0}, ".format(level),
               "effects_selected={0}".format(effects_selected if effects_selected else "ALL"),
               ")"]
    return "".join(options)


def list_effects(ctx, param, value) -> None:
    """
    List the names and descriptions of the effects currently available then exit.
    :param ctx: see callbacks for click options
    :param param: see callbacks for click options
    :param value: see callbacks for click options
    :return: No meaningful return
    """
    if not value or ctx.resilient_parsing:
        return
    click.echo(EFFECT_FACTORY.create_list_effects_display())
    ctx.exit()


def validate_effects_selected(ctx, param, value) -> None:
    """
    Validate entered effect names.
    :param ctx: see callbacks for click options
    :param param: see callbacks for click options
    :param value: see callbacks for click options
    :return: Validated names otherwise a click.BadParameter exception is raised
    """
    names_in_error = EFFECT_FACTORY.validate_effect_names(value)
    if names_in_error:
        raise click.BadParameter("Unknown effect{0}: {1}"
                                 .format('s' if len(names_in_error) > 1 else "", ", ".join(names_in_error)))
    return value


@click.command(help="""
    Show various effects on a Pimoroni LED shim.\n
    To limit the effects shown use the effect-list option to list the effects available then add them to the command
    line as required. Otherwise all effects will be shown.
                    """)
@click.version_option()
@click.option('-l', '--effect-list', is_flag=True, is_eager=True, expose_value=False, callback=list_effects,
              help='List the effects available and exit.')
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
@click.argument('effects_selected', nargs=-1, callback=validate_effects_selected, required=False)
def display_effects(display: str, duration: int, run: int, brightness: int,
                    invert: bool, level: str, effects_selected: List[str]) -> None:
    """
    Show various effects on a Pimoroni LED shim.
    :param display: In a CYCLE or at RANDOM
    :param duration: How long to display each effect for
    :param run: How many times to run effects
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param level: Set a logging level; DEBUG, VERBOSE, INFO or WARNING
    :param effects_selected: User entered list of effects to use, defaults to all effects
    :return: No meaningful return
    """
    configure_logging(level)
    logging.info(show_options(display, duration, run, brightness, invert, level, effects_selected))
    Pixel.set_default_brightness(brightness / 10.0)
    if not effects_selected:
        effects_to_render = EFFECT_FACTORY.get_all_effects()
    else:
        effects_to_render = []
        for name in effects_selected:
            effects_to_render.append(EFFECT_FACTORY.get_effect(name.upper()))
    render(display, duration, run, invert, effects_to_render)


if __name__ == '__main__':
    display_effects()   # pragma: no cover
