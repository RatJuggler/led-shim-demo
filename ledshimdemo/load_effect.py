from importlib import import_module
import os
import pkgutil

from .abstract_effect import AbstractEffect


def load_effects(*args, **kwargs):
    effects = []
    for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__) + "/effects"]):
        effects.append(load_effect(name, *args, **kwargs))
    return effects


def load_effect(effect_name, *args, **kwargs):
    try:
        if '.' in effect_name:
            module_name, class_name = effect_name.rsplit('.', 1)
        else:
            module_name = effect_name
            class_name = None
#        effect_module = import_module('.' + module_name, package='ledshimdemo.effects')
        effect_module = import_module('ledshimdemo.effects.' + module_name)
        if class_name is None:
            module_classes = list(filter(lambda x: x != 'AbstractEffect' and x.endswith('Effect'), dir(effect_module)))
            class_name = module_classes[0]
        effect_class = getattr(effect_module, class_name)
        instance = effect_class(*args, **kwargs)
    except (AttributeError, ImportError):
        raise ImportError('{} is not part of the effect collection!'.format(effect_name))
    else:
        if not issubclass(effect_class, AbstractEffect):
            raise ImportError("We currently don't have {}, but you are welcome to send in the request for it!".format(effect_class))
    return instance
