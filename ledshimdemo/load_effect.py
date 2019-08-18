from importlib import import_module

from .abstract_effect import AbstractEffect


def load_effect(effect_name, *args, **kwargs):
    try:
        if '.' in effect_name:
            module_name, class_name = effect_name.rsplit('.', 1)
        else:
            module_name = effect_name
            class_name = effect_name.capitalize()
        effect_module = import_module('ledshimdemo.effects.' + module_name)
#        effect_module = import_module('.' + module_name, package='ledshimdemo.effects')
        effect_class = getattr(effect_module, class_name)
        instance = effect_class(*args, **kwargs)
    except (AttributeError, ImportError):
        raise ImportError('{} is not part of the effect collection!'.format(effect_name))
    else:
        if not issubclass(effect_class, AbstractEffect):
            raise ImportError("We currently don't have {}, but you are welcome to send in the request for it!".format(effect_class))
    return instance
