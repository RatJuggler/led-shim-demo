import click
import os
from typing import List

from click import Context, Option

from .canvas import Canvas
from .configure_logging import configure_logging
from .display_options import DISPLAY_OPTIONS, add_options
from .effect_cache import EffectCache
from .effect_controller import EffectController
from .effect_publisher import EffectPublisher
from .effect_subscriber import EffectSubscriber
from .ipaddress_param import IPAddressParamType

NUM_PIXELS = 28  # The number of LEDs on the shim.

EFFECT_CACHE = EffectCache(os.path.dirname(__file__) + "/effects", "ledshimdemo.effects.", Canvas(NUM_PIXELS))

IP_ADDRESS = IPAddressParamType()


# noinspection PyUnusedLocal
def list_effects(ctx: Context, param: Option, value: str) -> None:
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


# noinspection PyUnusedLocal
def validate_effects(ctx: Context, param: Option, value: List[str]) -> List[str]:
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
    Use the 'display' command for a single Pi. For multiple Pi's one must use the 'lead' command and the others the
    'follow' command. Ensure you start the followers before starting the lead.\n
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


@ledshimdemo.command(help="Display the effects on a single Pi.")
@add_options(DISPLAY_OPTIONS)
@click.argument('effects', nargs=-1, type=click.STRING, callback=validate_effects, required=False)
def display(parade: str, duration: int, repeat: int, brightness: int, invert: bool, effects: List[str]) -> None:
    """
    Display various effects on a Pimoroni LED shim.
    :param parade: In a CYCLE or at RANDOM
    :param duration: How long to display each effect for
    :param repeat: How many times to run the effects
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param effects: User entered list of effects to use, defaults to all effects
    :return: No meaningful return
    """
    controller = EffectController(parade, duration, repeat, brightness, invert, effects)
    controller.process(EFFECT_CACHE.get_effect_instances(effects))


@ledshimdemo.command(help="Act as a lead for other instances to follow.")
@add_options(DISPLAY_OPTIONS)
@click.option('-o', '--port', type=click.IntRange(1024, 65535),
              help="Set the port number used for syncing.", default=5556, show_default=True)
@click.argument('ip_address', nargs=1, type=IP_ADDRESS, required=True)
@click.argument('effects', nargs=-1, type=click.STRING, callback=validate_effects, required=False)
def lead(parade: str, duration: int, repeat: int, brightness: int,
         invert: bool, port: int, ip_address: str, effects: List[str]) -> None:
    """
    Publish settings for follow subscribers then display effects as normal.
    :param parade: In a CYCLE or at RANDOM
    :param duration: How long to display each effect for
    :param repeat: How many times to run the effects
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param port: Configure the port number to be used when syncing
    :param ip_address: the lead instance's ip address
    :param effects: User entered list of effects to use, defaults to all effects
    :return: No meaningful return
    """
    controller = EffectController(parade, duration, repeat, brightness, invert, effects)
    publisher = EffectPublisher(ip_address, port)
    publisher.broadcast_effect_option(controller.encode_options_used())
    controller.process(EFFECT_CACHE.get_effect_instances(effects))


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
    subscriber = EffectSubscriber(ip_address, port)
    options = subscriber.get_effect_options()
    controller = EffectController.from_dict(options)
    controller.process(EFFECT_CACHE.get_effect_instances(controller.effects))


if __name__ == '__main__':
    ledshimdemo()   # pragma: no cover
