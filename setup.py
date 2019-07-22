from setuptools import setup

setup(
    name = 'ledshimeffects',
    version = '0.0.1',
    packages = ['ledshimeffects'],
    entry_points = {
        'console_scripts': [
            'ledshimeffects = ledshimeffects.__main__:display_effects'
        ]
    })
