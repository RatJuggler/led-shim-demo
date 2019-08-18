from ledshimdemo.abstract_effect import AbstractEffect
from importlib import import_module
import pkgutil
import os
import sys

for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
    imported_module = import_module('.' + name, package='ledshimdemo.effects')
    class_name = list(filter(lambda x: x != 'AbstractEffect' and x.endswith('Effect'), dir(imported_module)))
    if not class_name:
        continue
    effect_class = getattr(imported_module, class_name[0])
    if issubclass(effect_class, AbstractEffect):
        setattr(sys.modules[__name__], name, effect_class)
