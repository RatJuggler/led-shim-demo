# led-shim-demo

![Over-Engineered](https://img.shields.io/badge/over--engineered-definitely-red)
[![PyPi Package](https://img.shields.io/pypi/v/ledshimdemo.svg)](https://pypi.python.org/pypi/ledshimdemo)

![Test & QA](https://github.com/RatJuggler/guinea-bot/workflows/Test%20&%20QA/badge.svg)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/RatJuggler/led-shim-demo)

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

If you have more than one Pi with an led-shim you can use the lead/follow commands to share options and perform a simple
synchronised start across them. Be sure to start the follow instances before the lead.

# Installing

Install on Raspbian using:
```
pip3 install ledshimdemo
```
Or update using:
```
pip3 install -U ledshimdemo
```

# Running

```
$ ledshimdemo --help

Usage: ledshimdemo [OPTIONS] COMMAND [ARGS]...

  Show various effects on one or more Raspberry Pi's with Pimoroni LED
  shim's.

  Use the 'display' command for a single Pi. For multiple Pi's one must use
  the 'lead' command and the others the 'follow' command. Ensure you start
  the followers before starting the lead.

  To limit the effects shown use the effect-list option to list the effects
  available then add them to the command line as required. Otherwise all
  effects will be shown.

Options:
  --version                       Show the version and exit.
  -e, --effect-list               List the effects available and exit.
  -l, --log-level [DEBUG|VERBOSE|INFO|WARNING]
                                  Show additional logging information.
                                  [default: INFO]
  --help                          Show this message and exit.

Commands:
  display  Display the effects on a single Pi
  follow   Follow a lead instance.
  lead     Act as a lead for other instances to follow.

$ ledshimdemo display --help

Usage: ledshimdemo display [OPTIONS] [EFFECTS]...

  Display the effects on a single Pi

Options:
  -p, --parade [CYCLE|RANDOM]     How the effects are displayed.  [default:
                                  CYCLE]
  -d, --duration INTEGER RANGE    How long to display each effect for, in
                                  seconds (1-180).  [default: 10]
  -r, --repeat INTEGER RANGE      How many times to run the effects before
                                  stopping (1-240).  [default: 1]
  -b, --brightness INTEGER RANGE  How bright the effects will be (1-10).
                                  [default: 8]
  -i, --invert                    Change the display orientation.
  --help                          Show this message and exit.

$ ledshimdmeo follow --help

Usage: ledshimdemo follow [OPTIONS] IP_ADDRESS

  Follow a lead instance.

Options:
  -o, --port INTEGER RANGE  Set the port number used for syncing.  [default:
                            5556]
  --help                    Show this message and exit.

$ ledshimdemo lead --help

Usage: ledshimdemo lead [OPTIONS] IP_ADDRESS [EFFECTS]...

  Act as a lead for other instances to follow.

Options:
  -p, --parade [CYCLE|RANDOM]     How the effects are displayed.  [default:
                                  CYCLE]
  -d, --duration INTEGER RANGE    How long to display each effect for, in
                                  seconds (1-180).  [default: 10]
  -r, --repeat INTEGER RANGE      How many times to run the effects before
                                  stopping (1-240).  [default: 1]
  -b, --brightness INTEGER RANGE  How bright the effects will be (1-10).
                                  [default: 8]
  -i, --invert                    Change the display orientation.
  -o, --port INTEGER RANGE        Set the port number used for syncing.
                                  [default: 5556]
  --help                          Show this message and exit.
```

Sample output with the default options:

```
$ ledshimdemo display
2019-08-31 15:47:36,864 - INFO - Effect Options(parade=CYCLE, duration=10 secs, repeat=1, brightness=8, invert=False, effects=ALL)
2019-08-31 15:47:36,864 - INFO - Effect: BinaryClock - Shows hours, minutes and seconds. Update Frequency: 1 secs
2019-08-31 15:47:47,185 - INFO - Effect: Candle - A flickering candle. Update Frequency: 0.01 secs
2019-08-31 15:47:57,208 - INFO - Effect: CheerLights - Synchronize with the CheerLights "Internet of Things" project. Update Frequency: 5 secs
2019-08-31 15:48:07,745 - INFO - Effect: ColouredLights - Simple coloured lights like Xmas lights. Update Frequency: 0.5 secs
2019-08-31 15:48:17,817 - INFO - Effect: DigitalRain - Cut price Matrix effect. Update Frequency: 0.02 secs
2019-08-31 15:48:27,820 - INFO - Effect: GradientGraph - Sine wave colour gradient effect. Update Frequency: 0.01 secs
2019-08-31 15:48:37,826 - INFO - Effect: Rainbow - A slowly moving rainbow. Update Frequency: 0.01 secs
2019-08-31 15:48:47,861 - INFO - Effect: RandomBlink - Some random blinking. Update Frequency: 0.05 secs
2019-08-31 15:48:57,875 - INFO - Effect: SolidColours - A sequence of solid colours. Update Frequency: 0.5 secs
```

# Troubleshooting

If anything is going to cause a problem trying to run `ledshimdemo` it will be NumPy which is used by a couple of the 
demos. The NumPy package is included in most builds of Raspbian, but installed with `apt-get`, this then causes problems
if anything tries to install a different version with `pip3`. For this reason `ledshimdemo` doesn't install a specific 
version of NumPy hoping to pick up the latest global installed one. If you need to install NumPy try using:
```
sudo apt-get install python3-numpy
```

# Development

Development is done in the 'develop' branch and merging into 'master' will trigger a release. Tests in master should 
always pass.

# Addendum

This project is definitely over-engineered for what it actually does because it's being used as a learning exercise.

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

The synchronisation using the lead/follow commands is very basic, yes the effect options set for the lead are
distributed to the follow instances but there is only a primitive trigger to try and start the displays together and
there is no heartbeat to try to keep them in sync. If you run with more than about 10 repeat iterations you'll soon see
the displays go out of sync.    

Badges showing the build status and code coverage for both the master and develop branches are shown at the top. This is
 a simple solution to the problem of trying to make this file specific to the branch it is in.
