#!/usr/bin/env python3

# Application to display a series of effects on a Pimoroni led-shim.

import click
from random import randint
from time import sleep

#import ledshim

from canvas import Canvas
from effects import Candle, BinaryClock, CheerLights, GradientGraph, Rainbow, RandomBlink, SolidColours

NUM_PIXELS = 28     # Number of LEDs on the shim.

#ledshim.set_clear_on_exit()

canvas = Canvas(NUM_PIXELS)
effects = [Candle(canvas),
           GradientGraph(canvas),
           SolidColours(canvas),
           BinaryClock(canvas),
           Rainbow(canvas),
           CheerLights(canvas),
           RandomBlink(canvas)]
effect_no = -1


def random_effect():
    choose = randint(0, len(effects))
    return effects[choose]


def cycle_effects():
    global effect_no
    effect_no = (effect_no + 1) % len(effects)
    return effects[effect_no]


@click.command(help="Show various effects on a Pimoroni LED shim.")
@click.version_option(prog_name="ledshimeffects", version="0.0.1")
@click.option('-s', '--show_effects', type=click.Choice(["CYCLE", "RANDOM"]), default="CYCLE", help="How the effects are displayed.", show_default=True)
@click.option('-t', '--effect_time', type=int, default=10, help="How long to display each effect for, in seconds.", show_default=True)
@click.option('-i', '--invert', is_flag=True, help="Change the display orientation.")
@click.option('-d', '--debug', is_flag=True, help="Show additional debug information.")
def display_effects(show_effects, effect_time, invert, debug):
    try:
        show_time = 0
        effect = effects[0]
        while True:
            if show_time <= 0:
                if show_effects == "CYCLE":
                    effect = cycle_effects()
                if show_effects == "RANDOM":
                    effect = random_effect()
                show_time = effect_time / effect.get_speed()
                print(str(effect))
            effect.compose()
            if effect.is_debug():
                print(repr(effect))
                print(repr(canvas))
            for i in range(canvas.get_size()):
                pixel = canvas.get_pixel(i)
                position = (canvas.get_size() - 1 - i) if invert else i
#                ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
#            ledshim.show()
            show_time -= 1
            sleep(effect.get_speed())
    except KeyboardInterrupt:
        pass
#        ledshim.clear()
#        ledshim.show()


if __name__ == '__main__':
    display_effects()
