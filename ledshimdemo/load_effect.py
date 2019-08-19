from importlib import import_module
import pkgutil
from typing import List

from .abstract_effect import AbstractEffect


def load_effects(effects_path, effects_package, *args, **kwargs) -> List[AbstractEffect]:
    effects = []
    for (_, effect_module, _) in pkgutil.iter_modules([effects_path]):
        effects.append(load_effect(effects_package + effect_module, None, *args, **kwargs))
    return effects


def load_effect(effect_module, effect_class: str, *args, **kwargs) -> AbstractEffect:
    try:
        effect_module = import_module(effect_module)
        if effect_class is None:
            module_classes = list(filter(lambda x: x != 'AbstractEffect' and x.endswith('Effect'), dir(effect_module)))
            if module_classes:
                effect_class = module_classes[0]
        effect_class = getattr(effect_module, effect_class)
        instance = effect_class(*args, **kwargs)
    except (AttributeError, ImportError):
        raise ImportError('{} is not part of the effect collection!'.format(effect_module))
    else:
        if not issubclass(effect_class, AbstractEffect):
            raise TypeError("{} is not a valid effect class!".format(effect_class))
    return instance
