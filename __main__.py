#!/usr/bin/env python3

# Application to display a series of effects on a Pimoroni led-shim.

from canvas import Canvas
from effects import Candle, BinaryClock, CheerLights, GradientGraph, Rainbow, RandomBlink, SolidColours
from time import sleep
import random
#import ledshim

NUM_PIXELS = 28
EFFECT_TIME = 10    # Time to show each effect, in seconds.
DEBUG = False       # Show additional output on composing.

#ledshim.set_clear_on_exit()

canvas = Canvas(NUM_PIXELS)
effect0 = Candle(canvas, DEBUG)
effect1 = GradientGraph(canvas, DEBUG)
effect2 = SolidColours(canvas, DEBUG)
effect3 = BinaryClock(canvas, DEBUG)
effect4 = Rainbow(canvas, DEBUG)
effect5 = CheerLights(canvas, DEBUG)
effect6 = RandomBlink(canvas, DEBUG)
effect_no = -1


def random_effect():
    choose = random.random()
    if choose < 0.10:
        return effect0
    elif choose < 0.20:
        return effect1
    elif choose < 0.30:
        return effect2
    elif choose < 0.40:
        return effect3
    elif choose < 0.50:
        return effect4
    elif choose < 0.60:
        return effect5
    else:
        return effect6


def cycle_effects():
    global effect_no
    effect_no += 1
    if effect_no == 0:
        return effect0
    elif effect_no == 1:
        return effect1
    elif effect_no == 2:
        return effect2
    elif effect_no == 3:
        return effect3
    elif effect_no == 4:
        return effect4
    elif effect_no == 5:
        return effect5
    else:
        effect_no = -1
        return effect6


try:
    show_time = 0
    while True:
        if show_time <= 0:
            effect = cycle_effects()
            show_time = EFFECT_TIME / effect.get_speed()
            effect.print_name()
        effect.compose()
        if effect.is_debug():
            effect.print_debug()
            canvas.print_canvas()
        for i in range(canvas.get_size()):
            pixel = canvas.get_pixel(i)
#            ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
#        ledshim.show()
        show_time -= 1
        sleep(effect.get_speed())
except KeyboardInterrupt:
    pass
#    ledshim.clear()
#    ledshim.show()
