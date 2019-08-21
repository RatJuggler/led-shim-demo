# led-shim-demo

![GitHub](https://img.shields.io/github/license/RatJuggler/led-shim-demo)
![Over-Engineered](https://img.shields.io/badge/over--engineered-somewhat-red)
[![PyPi Package](https://img.shields.io/pypi/v/ledshimdemo.svg)](https://pypi.python.org/pypi/ledshimdemo)
[![Python Versions](https://img.shields.io/pypi/pyversions/ledshimdemo.svg)](https://pypi.python.org/pypi/ledshimdemo)

[![Travis](https://img.shields.io/travis/com/RatJuggler/led-shim-demo/master.svg?label=master%20build)](https://travis-ci.org/RatJuggler/led-shim-demo)
[![Coverage Status](https://coveralls.io/repos/github/RatJuggler/led-shim-demo/badge.svg?branch=master)](https://coveralls.io/github/RatJuggler/led-shim-demo?branch=master)
![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/RatJuggler/led-shim-demo)

[![Travis](https://img.shields.io/travis/com/RatJuggler/led-shim-demo/develop.svg?label=develop%20build)](https://travis-ci.org/RatJuggler/led-shim-demo)
[![Coverage Status](https://coveralls.io/repos/github/RatJuggler/led-shim-demo/badge.svg?branch=develop)](https://coveralls.io/github/RatJuggler/led-shim-demo?branch=develop)

An application to display a variety of effects on the Raspberry Pi [led-shim](https://shop.pimoroni.com/products/led-shim)
from Pimoroni.

The effects are based on the examples given in the base [library](https://github.com/pimoroni/led-shim) plus some 
additions from my [fork](https://github.com/RatJuggler/led-shim/tree/more-examples).

- Binary Clock - Shows hours, minutes and seconds.
- Candle - A flickering candle.
- CheerLights - Synchronize with the [CheerLights](https://cheerlights.com) "Internet of Things" project.
- Coloured Lights - Simple coloured lights like Xmas lights.
- Digital Rain - Cut price Matrix effect.
- Gradient Graph - A moving colour gradient determined by the height of a sine wave.
- Rainbow - A slowly moving rainbow effect.
- Random Blink - Some random blinking.
- Solid Colours - A basic effect which just shows a sequence of solid colours.

# Installing

Install on Raspbian using:
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

Usage: ledshimdemo [OPTIONS] [EFFECTS_SELECTED]...

  Show various effects on a Pimoroni LED shim.

  To limit the effects shown use the effect-list option to list the effects
  available then add them to the command line as required. Otherwise all
  effects will be shown.

Options:
  --version                       Show the version and exit.
  -l, --effect-list               List the effects available and exit.
  -d, --effect-display [CYCLE|RANDOM]
                                  How the effects are displayed.  [default:
                                  CYCLE]
  -u, --effect-duration INTEGER RANGE
                                  How long to display each effect for, in
                                  seconds (1-180).  [default: 10]
  -r, --effect-run INTEGER RANGE  How many times to run effects before
                                  stopping (1-240).  [default: 24]
  -b, --brightness INTEGER RANGE  How bright the effects will be (1-10).
                                  [default: 8]
  -i, --invert                    Change the display orientation.
  -o, --log-level [DEBUG|VERBOSE|INFO|WARNING]
                                  Show additional logging information.
                                  [default: WARNING]
  --help                          Show this message and exit.
```

# Troubleshooting

If anything is going to cause a problem trying to run `ledshimdemo` it will be NumPy which is used by a couple of the 
demos. The NumPy package is included in most builds of Raspbian, but installed with `apt-get`, this then causes problems
if anything tries to install a different version with `pip3`. For this reason `ledshimdemo` is set to use the Raspbian
default version (see setup.py) to try and avoid installing a different version with `pip3`. However, if you do get a 
runtime error indicating a corrupted NumPy you could first try uninstalling any local `pip3` versions of it to see if
that helps.
```
pip3 uninstall numpy
```

# Addendum

This project is somewhat over-engineered for what it actually does because it's being used as a learning exercise.

The application has a number of output logging levels built into it, including a custom VERBOSE level, to show some of
the inner workings. This is just because.

The effects are loaded dynamically using a mechanism loosely based on code from
[this](https://github.com/BNMetrics/factory_pattern_sample) Python3 factory pattern example.

The code coverage for this project is a good example of why measuring unit test coverage can be a misleading indicator
of quality. Whilst it does have plenty of unit tests those for the effects are mostly simple smoke tests which show that
the code will run. They don't actually confirm that the effects are producing the desired output.

The development work for this project was done using PyCharm on an Intel x64 machine, as the
project was designed to be run on an ARM based Raspberry Pi only a source distribution is uploaded to PyPi. However,
when installing under Raspbian it should install the ARM wheel from [PiWheels](https://www.piwheels.hostedpi.com/)
making the installation much faster. See the [PiWheels FAQ](https://www.piwheels.hostedpi.com/faq.html) for more
information.

Badges showing the build status and code coverage for both the master and develop branches are shown at the top. This is
 a simple solution to the problem of trying to make this file specific to the branch it is in.
