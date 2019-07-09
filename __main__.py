#!/usr/bin/env python

from canvas import Canvas
from anu_random import ANURandom
from binary_clock import BinaryClock
from gradient_graph import GradientGraph
from solid_colours import SolidColours
from time import sleep
import random
import ledshim

NUM_PIXELS = 28

ledshim.set_clear_on_exit()

canvas = Canvas(NUM_PIXELS)
effect0 = ANURandom(canvas)
effect1 = GradientGraph(canvas)
effect2 = SolidColours(canvas)
effect3 = BinaryClock(canvas)


def choose_effect():
    choose = random.random()
    if choose < 0.1:
        return effect0
    elif choose < 0.40:
        return effect1
    elif choose < 0.70:
        return effect2
    else:
        return effect3


try:
    show_time = 60
    while True:
        if show_time == 60:
            show_time = 0
            effect = choose_effect()
        effect.print_name()
        effect.compose()
        effect.print_compose()
        #canvas.print_canvas()
        for i in range(canvas.get_size()):
            pixel = canvas.get_pixel(i)
            ledshim.set_pixel(i, pixel[0], pixel[1], pixel[2], pixel[3])
        ledshim.show()
        show_time += 1
        sleep(1)
except KeyboardInterrupt:
    ledshim.clear()
    ledshim.show()
