#!/usr/bin/env python3

# Application to display a series of effects on a Pimoroni led-shim.

from canvas import Canvas
from effects import ANURandom, BinaryClock, CheerLights, GradientGraph, Rainbow, SolidColours
from time import sleep
import random
#import ledshim

NUM_PIXELS = 28
EFFECT_TIME = 10    # Time to show each effect, in seconds.
DEBUG = True        # Show additional output on composing.

#ledshim.set_clear_on_exit()

canvas = Canvas(NUM_PIXELS)
effect0 = ANURandom(canvas, DEBUG)
effect1 = GradientGraph(canvas, DEBUG)
effect2 = SolidColours(canvas, DEBUG)
effect3 = BinaryClock(canvas, DEBUG)
effect4 = Rainbow(canvas, DEBUG)
effect5 = CheerLights(canvas, DEBUG)


def choose_effect():
    choose = random.random()
    if choose < 0.10:
        return effect0
    elif choose < 0.25:
        return effect1
    elif choose < 0.40:
        return effect2
    elif choose < 0.55:
        return effect3
    elif choose < 0.70:
        return effect4
    else:
        return effect5


try:
    show_time = 0
    while True:
        if show_time <= 0:
            effect = choose_effect()
            show_time = EFFECT_TIME / effect.get_speed()
            effect.print_name()
        effect.compose()
        if effect.is_debug():
            effect.print_debug()
        for i in range(canvas.get_size()):
            pixel = canvas.get_pixel(i)
#            ledshim.set_pixel(i, pixel[0], pixel[1], pixel[2], pixel[3])
#        ledshim.show()
        show_time -= 1
        sleep(effect.get_speed())
except KeyboardInterrupt:
    pass
#    ledshim.clear()
#    ledshim.show()
