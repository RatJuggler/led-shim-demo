#!/usr/bin/env python3

# Application to display a series of effects on a Pimoroni led-shim.

from canvas import Canvas
from effects import Candle, BinaryClock, CheerLights, GradientGraph, Rainbow, RandomBlink, SolidColours
from time import sleep
import random
#import ledshim

NUM_PIXELS = 28     # Number of LEDs on the shim.
INVERT = True       # Invert the display depending on which way round the shim is to be viewed.

EFFECT_TIME = 10    # Time to show each effect, in seconds.
DEBUG = False       # Show additional output on composing.

#ledshim.set_clear_on_exit()

canvas = Canvas(NUM_PIXELS)
effects = [Candle(canvas), GradientGraph(canvas), SolidColours(canvas), BinaryClock(canvas), Rainbow(canvas), CheerLights(canvas), RandomBlink(canvas)]
effect_no = -1


def random_effect():
    choose = random.randint(0, len(effects))
    return effects[choose]


def cycle_effects():
    global effect_no
    effect_no = (effect_no + 1) % len(effects)
    return effects[effect_no]


try:
    show_time = 0
    while True:
        if show_time <= 0:
            effect = cycle_effects()
            show_time = EFFECT_TIME / effect.get_speed()
            print(str(effect))
        effect.compose()
        if effect.is_debug():
            print(repr(effect))
            print(repr(canvas))
        for i in range(canvas.get_size()):
            pixel = canvas.get_pixel(i)
            position = (canvas.get_size() - 1 - i) if INVERT else i
#            ledshim.set_pixel(position, pixel.get_r(), pixel.get_g(), pixel.get_b(), pixel.get_brightness())
#        ledshim.show()
        show_time -= 1
        sleep(effect.get_speed())
except KeyboardInterrupt:
    pass
#    ledshim.clear()
#    ledshim.show()
