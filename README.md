# led-shim-demo
Display a variety of effects on the Raspberry Pi [led-shim](https://shop.pimoroni.com/products/led-shim) from Pimoroni.

The effects are based on the examples given in the base [library](https://github.com/pimoroni/led-shim) plus some 
additions from my [fork](https://github.com/RatJuggler/led-shim/tree/more-examples).

- Binary Clock - Shows hours, minutes and seconds.
- Candle - A flickering candle.
- CheerLights - Synchronize with the [CheerLights](https://cheerlights.com) "Internet of Things" project.
- Coloured Lights - Simple coloured lights like Xmas lights.
- Gradient Graph - A moving colour gradient determined by the height of a sine wave.
- Rainbow - A slowly moving rainbow effect.
- Random Blink - Some random blinking.
- Solid Colours - A basic effect which just shows a sequence of solid colours.

# Installing

Install on Raspbian from PyPi using:

```
sudo pip3 install led-shim-demo
```

# Running

```
$ ledshimdemo --help

Usage: ledshimdemo [OPTIONS]

  Show various effects on a Pimoroni LED shim.

Options:
  --version                       Show the version and exit.
  -s, --show_effects [CYCLE|RANDOM]
                                  How the effects are displayed.  [default:
                                  CYCLE]
  -t, --effect_time INTEGER RANGE
                                  How long to display each effect for, in
                                  seconds (1-3600).  [default: 10]
  -b, --brightness INTEGER RANGE  How bright the effects will be (1-10).
                                  [default: 8]
  -i, --invert                    Change the display orientation.
  -l, --log [NONE|INFO|EFFECT|DEBUG]
                                  Show additional logging information.
  --help                          Show this message and exit.
```
