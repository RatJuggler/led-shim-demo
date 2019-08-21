"""
Functions for dynamically loading effects.
"""
from importlib import import_module
import pkgutil
from typing import Dict, List

from .abstract_effect import AbstractEffect


def create_list_effects_display(effects_available: Dict[str, AbstractEffect]) -> str:
    """
    Build a display list of the effects available.
    :param effects_available: to form the list
    :return: A string showing the name and description of each effect available
    """
    effects = ["Available Effects:"]
    pad_size = len(max(effects_available.keys(), key=len))
    for name, effect in effects_available.items():
        effects.append(name.ljust(pad_size, ' ') + " - " + effect.get_description())
    return "\n".join(effects)


def validate_effect_names(effects_selected: List[str], effects_available: Dict[str, AbstractEffect]) -> List[str]:
    """
    Check that the effect names supplied are in the list of effects available.
    :param effects_selected: names from command line
    :param effects_available: found when effects loaded
    :return: List of names which don't match with anything in the available list
    """
    names_in_error = []
    for name in effects_selected:
        try:
            effects_available[name]
        except KeyError:
            names_in_error.append(name)
    return names_in_error


def load_effects(effects_path: str, effects_package: str, *args, **kwargs) -> Dict[str, AbstractEffect]:
    """
    Load all the effects from a given path/package.
    :param effects_path: path on the file system to the effects to load
    :param effects_package: the name of the associated package
    :param args: parameters for new effect instances
    :param kwargs: parameters for new effect instances
    :return: A dictionary of the effect instances loaded indexed by name
    """
    effects = {}
    for (_, effect_module, _) in pkgutil.iter_modules([effects_path]):
        effect = load_effect(effects_package + effect_module, None, *args, **kwargs)
        effects[effect.get_name()] = effect
    return effects


def load_effect(effect_module: str, effect_class: str, *args, **kwargs) -> AbstractEffect:
    """
    Load an effect class and create an instance of it.
    An effect class must be a subclass of AbstractEffect and the name must end in "Effect".
    :param effect_module: the module containing the effect class to load
    :param effect_class: the name of the effect class to load
    :param args: parameters for new effect instance
    :param kwargs: parameters for new effect instance
    :return: An instance of the effect class loaded
    """
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
