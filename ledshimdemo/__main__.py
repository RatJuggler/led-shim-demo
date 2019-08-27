import click
import logging
import os
from typing import List

from .canvas import Canvas
from .configure_logging import configure_logging
from .display_options import DISPLAY_OPTIONS, add_options
from .effect_parade import AbstractEffectParade
from .effect_cache import EffectCache
from .ipaddress_param import IPAddressParamType
from .pixel import Pixel

NUM_PIXELS = 28  # The number of LEDs on the shim.

EFFECT_CACHE = EffectCache(os.path.dirname(__file__) + "/effects", "ledshimdemo.effects.", Canvas(NUM_PIXELS))

IP_ADDRESS = IPAddressParamType()


def display_options_used(command: str, parade: str, duration: int, run: int, brightness: int,
                         invert: bool, effects_selected: List[str]) -> str:
    """
    Human readable string showing the display options to be used.
    :param command: the command using these options
    :param parade: from command line option or default
    :param duration: from command line option or default
    :param run: from command line option or default
    :param brightness: from command line option or default
    :param invert: from command line option or default
    :param effects_selected: from command line arguments or default
    :return: One line string of the display options to be used
    """
    options = ["{0}(".format(command),
               "parade={0}, ".format(parade),
               "duration={0} secs, ".format(duration),
               "repeat={0}, ".format(run),
               "brightness={0}, ".format(brightness),
               "invert={0}, ".format(invert),
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
    click.echo(EFFECT_CACHE.create_list_effects_display())
    ctx.exit()


def validate_effects_selected(ctx, param, value) -> None:
    """
    Validate entered effect names.
    :param ctx: see callbacks for click options
    :param param: see callbacks for click options
    :param value: see callbacks for click options
    :return: Validated names otherwise a click.BadParameter exception is raised
    """
    names_in_error = EFFECT_CACHE.validate_effect_names(value)
    if names_in_error:
        raise click.BadParameter("Unknown effect{0}: {1}"
                                 .format('s' if len(names_in_error) > 1 else "", ", ".join(names_in_error)))
    return value


@click.group(help="""
    Show various effects on one or more Raspberry Pi's with Pimoroni LED shim's.\n
    To limit the effects shown use the effect-list option to list the effects available then add them to the command
    line as required. Otherwise all effects will be shown.
    """)
@click.version_option()
@click.option('-e', '--effect-list', is_flag=True, is_eager=True, expose_value=False, callback=list_effects,
              help='List the effects available and exit.')
@click.option('-l', '--log-level', 'level', type=click.Choice(["DEBUG", "VERBOSE", "INFO", "WARNING"]),
              help="Show additional logging information.", default="INFO", show_default=True)
def ledshimdemo(level: str):
    """
    Show various effects on one or more Raspberry Pi's with Pimoroni LED shim's.
    :param level: Set a logging level; DEBUG, VERBOSE, INFO or WARNING
    :return: No meaningful return
    """
    configure_logging(level)


@ledshimdemo.command(help="Display the effects on a single Pi")
@add_options(DISPLAY_OPTIONS)
@click.argument('effects_selected', nargs=-1, type=click.STRING, callback=validate_effects_selected, required=False)
def display(parade: str, duration: int, run: int, brightness: int,
            invert: bool, effects_selected: List[str]) -> None:
    """
    Display various effects on a Pimoroni LED shim.
    :param parade: In a CYCLE or at RANDOM
    :param duration: How long to display each effect for
    :param run: How many times to run the effects
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param effects_selected: User entered list of effects to use, defaults to all effects
    :return: No meaningful return
    """
    logging.info(display_options_used("display", parade, duration, run, brightness, invert, effects_selected))
    Pixel.set_default_brightness(brightness / 10.0)
    if invert:
        Canvas.invert_display()
    effect_instances = EFFECT_CACHE.get_effect_instances(effects_selected)
    effects_display = AbstractEffectParade.select_effect_parade(parade, effect_instances)
    effects_display.render(duration, run, lead)


@ledshimdemo.command(help="Act as a lead for other instances to follow.")
@add_options(DISPLAY_OPTIONS)
@click.option('-o', '--port', type=click.IntRange(1024, 65535),
              help="Set the port number used for syncing.", default=5556, show_default=True)
@click.argument('ip_address', nargs=1, type=IP_ADDRESS, required=True)
@click.argument('effects_selected', nargs=-1, type=click.STRING, callback=validate_effects_selected, required=False)
def lead(parade: str, duration: int, run: int, brightness: int,
         invert: bool, port: int, ip_address: str, effects_selected: List[str]) -> None:
    """
    Display effects as normal but also publish the settings for follow subscribers.
    :param parade: In a CYCLE or at RANDOM
    :param duration: How long to display each effect for
    :param run: How many times to run the effects
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param port: Configure the port number to be used when syncing
    :param ip_address: the lead instance's ip address
    :param effects_selected: User entered list of effects to use, defaults to all effects
    :return: No meaningful return
    """
    logging.info(display_options_used("lead", parade, duration, run, brightness, invert, effects_selected))
    Pixel.set_default_brightness(brightness / 10.0)
    if invert:
        Canvas.invert_display()
    effect_instances = EFFECT_CACHE.get_effect_instances(effects_selected)
    effects_display = AbstractEffectParade.select_effect_parade(parade, effect_instances)
    effects_display.render(duration, run, lead)


@ledshimdemo.command(help="Follow a lead instance.")
@click.option('-o', '--port', type=click.IntRange(1024, 65535),
              help="Set the port number used for syncing.", default=5556, show_default=True)
@click.argument('ip_address', nargs=1, type=IP_ADDRESS, required=True)
def follow(port: int, ip_address: str) -> None:
    """
    Subscribe to lead instance for display setting then start displaying effects.
    :param port: Configure the port number to be used when syncing
    :param ip_address: the lead instance's ip address
    :return: No meaningful return
    """
    logging.info(display_options_used("follow", None, None, None, None, None, None))
    click.echo("Subscribe to lead for display setting then start displaying effects.")


if __name__ == '__main__':
    ledshimdemo()   # pragma: no cover
