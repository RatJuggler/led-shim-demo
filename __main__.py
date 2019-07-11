#!/usr/bin/env python3

# Application to display a series of effects on a Pimoroni led-shim.

from canvas import Canvas
from anu_random import ANURandom
from binary_clock import BinaryClock
from gradient_graph import GradientGraph
from rainbow import Rainbow
from solid_colours import SolidColours
from time import sleep
import random
#import ledshim

NUM_PIXELS = 28
EFFECT_TIME = 10    # Seconds

#ledshim.set_clear_on_exit()

canvas = Canvas(NUM_PIXELS)
effect0 = ANURandom(canvas)
effect1 = GradientGraph(canvas)
effect2 = SolidColours(canvas)
effect3 = BinaryClock(canvas)
effect4 = Rainbow(canvas)


def choose_effect():
    choose = random.random()
    if choose < 0.10:
        return effect0
    elif choose < 0.30:
        return effect1
    elif choose < 0.50:
        return effect2
    elif choose < 0.70:
        return effect3
    else:
        return effect4


try:
    show_time = 0
    while True:
        if show_time <= 0:
            effect = choose_effect()
            show_time = EFFECT_TIME / effect.get_speed()
            effect.print_name()
        effect.compose()
        effect.print_compose()
        #canvas.print_canvas()
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
