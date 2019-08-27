from importlib import import_module
import pkgutil
from typing import Dict, List

from .abstract_effect import AbstractEffect
from .canvas import Canvas


class EffectCache:
    """
    Class to store and control access to the available effects.
    """

    @staticmethod
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
            if not effect_class:
                module_classes = \
                    list(filter(lambda x: x != 'AbstractEffect' and x.endswith('Effect'), dir(effect_module)))
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

    @staticmethod
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
            effect = EffectCache.load_effect(effects_package + effect_module, "", *args, **kwargs)
            effects[effect.get_name().upper()] = effect
        return effects

    def __init__(self, effects_path: str, effects_package: str, canvas: Canvas) -> None:
        """
        Initialise the effect cache.
        :param effects_path: path on the file system to the effects to load
        :param effects_package: the name of the associated package
        :param canvas: to be used by all effects
        """
        self.effects_available = self.load_effects(effects_path, effects_package, canvas)

    def get_all_effects(self) -> List[AbstractEffect]:
        """
        Get a list of instances of all the effects.
        :return: A list of all the available instances sorted by name
        """
        return list(sorted(self.effects_available.values(), key=lambda e: e.get_name()))

    def get_effect(self, effect_name) -> AbstractEffect:
        """
        Get the instance of the named effect.
        :param effect_name: name of the instance required, will be converted to uppercase
        :return: An effect instance, will raise a KeyError if not found
        """
        return self.effects_available[effect_name.upper()]

    def create_list_effects_display(self) -> str:
        """
        Build a display list of the effects available.
        :return: A string showing the name and description of each effect available sorted by name
        """
        effects = ["Available Effects:"]
        pad_size = len(max(self.effects_available.keys(), key=len))
        for effect in self.get_all_effects():
            effects.append(effect.get_display_list_entry(pad_size))
        return "\n".join(effects)

    def validate_effect_names(self, effects: List[str]) -> List[str]:
        """
        Check that the effect names supplied are in the list of effects available.
        :param effects: names from command line
        :return: List of names which don't match with anything in the available list
        """
        names_in_error = []
        for name in effects:
            try:
                self.get_effect(name)
            except KeyError:
                names_in_error.append(name)
        return names_in_error

    def get_effect_instances(self, effects: List[str]) -> List[AbstractEffect]:
        """
        Get instances of the effects selected.
        :param effects: List of the effect names to use
        :return: List of effect display instances
        """
        instances = []
        if not effects:
            instances = self.get_all_effects()
        else:
            for effect in effects:
                instances.append(self.get_effect(effect))
        return instances
