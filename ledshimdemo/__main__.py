import click
import logging
from random import randint
from time import sleep

import ledshim

from .canvas import Canvas
from .effects import BinaryClock, Candle, CheerLights, ColouredLights, GradientGraph, Rainbow, RandomBlink, SolidColours
from .pixel import Pixel

NUM_PIXELS = 28     # The number of LEDs on the shim.

ledshim.set_clear_on_exit()


def show_options(show_effects: str, effect_time: int, brightness: int, invert: bool, log: str):
    options = ["Active Options(",
               "show_effects={0}, ".format(show_effects),
               "effect_time={0}, ".format(effect_time),
               "brightness={0}, ".format(brightness),
               "invert={0}, ".format(invert),
               "log={0}".format(log),
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
@click.option('-l', '--log', type=click.Choice(["NONE", "INFO", "EFFECT", "DEBUG"]), default="NONE",
              help="Show additional logging information.")
def display_effects(show_effects: str, effect_time: int, brightness: int, invert: bool, log: str):
    """
    Show various effects on a Pimoroni LED shim.
    :param show_effects: In a CYCLE or at RANDOM
    :param effect_time: How long to display each effect for
    :param brightness: How bright the effects will be
    :param invert: Depending on which way round the Pi is
    :param log: Set a logging level; NONE, INFO, EFFECT or DEBUG
    :return: No meaningful return
    """
    print(show_options(show_effects, effect_time, brightness, invert, log))
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
    show_time = 0
    effect_no = len(effects) - 1
    effect = effects[effect_no]
    try:
        while True:
            if show_time <= 0:
                if show_effects == "CYCLE":
                    effect_no = (effect_no + 1) % len(effects)
                if show_effects == "RANDOM":
                    effect_no = randint(0, len(effects))
                effect = effects[effect_no]
                show_time = effect_time / effect.get_speed()
                logging.info(str(effect))
            effect.compose()
            logging.info(repr(effect))
            logging.debug(repr(canvas))
            for i in range(canvas.get_size()):
                pixel = canvas.get_pixel(i)
                position = (canvas.get_size() - 1 - i) if invert else i
                ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
            ledshim.show()
            show_time -= 1
            sleep(effect.get_speed())
    except KeyboardInterrupt:
        ledshim.clear()
        ledshim.show()


if __name__ == '__main__':
    display_effects()
