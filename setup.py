from codecs import open
from os.path import abspath, dirname, join

from setuptools import setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='ledshimeffects',
    version='0.0.1',
    description='Show various effects on a Pimoroni LED shim.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='John Chase',
    author_email='ratteal@gmail.com',
    python_requires='>=3.5.3',
    url='https://github.com/RatJuggler/led-shim-effects',
    packages = ['ledshimeffects'],
    entry_points = {
        'console_scripts': [
            'ledshimeffects = ledshimeffects.__main__:display_effects'
        ]
    })
