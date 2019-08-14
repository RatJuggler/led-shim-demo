# led-shim-demo

[![Coverage Status](https://coveralls.io/repos/github/RatJuggler/led-shim-demo/badge.svg?branch=develop)](https://coveralls.io/github/RatJuggler/led-shim-demo?branch=develop)
[![PyPi Package](https://img.shields.io/pypi/v/ledshimdemo.svg)](https://pypi.python.org/pypi/ledshimdemo)
[![Python Versions](https://img.shields.io/pypi/pyversions/ledshimdemo.svg)](https://pypi.python.org/pypi/ledshimdemo)

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

**Note**: This project is completely over-engineered for what it actually does because it's being used as a learning exercise.

# Installing

Install on Raspbian from PyPi using:
```
pip3 install led-shim-demo
```
Or update using:
```
pip3 install --update led-shim-demo
```

# Running

```
$ ledshimdemo --help

Usage: ledshimdemo [OPTIONS]

  Show various effects on a Pimoroni LED shim.

Options:
  --version                       Show the version and exit.
  -d, --effect_display [CYCLE|RANDOM]
                                  How the effects are displayed.  [default:
                                  CYCLE]
  -u, --effect_duration INTEGER RANGE
                                  How long to display each effect for, in
                                  seconds (1-180).  [default: 10]
  -r, --effect_run INTEGER RANGE  How many times to run effects before
                                  stopping (1-240).  [default: 24]
  -b, --brightness INTEGER RANGE  How bright the effects will be (1-10).
                                  [default: 8]
  -i, --invert                    Change the display orientation.
  -l, --loglevel [DEBUG|INFO|WARNING]
                                  Show additional logging information.
                                  [default: WARNING]
  --help                          Show this message and exit.
```

# Troubleshooting

If anything is going to cause a problem trying to run `ledshimdemo` it will be NumPy which is used by a couple of the 
demos. The NumPy package is included in most builds of Raspbian, but installed with `apt-get`, this then causes problems
if anything tries to install a different version with `pip3`. For this reason `ledshimdemo` is set to use the Raspbian
default version (see setup.py) to try and avoid installing a different version with `pip3`. However, if you do get a 
runtime error indicating a corrupted NumPy you could first try uninstalling any `pip3` versions of it to see if that
helps.
```
pip3 uninstall numpy
```

