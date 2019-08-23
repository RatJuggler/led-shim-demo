from importlib import import_module
import logging
import pkgutil
from random import randint
from typing import Dict, List

from .abstract_effect import AbstractEffect
from .canvas import Canvas


class EffectFactory:
    """
    Class to store and control access to the available effects and those selected for rendering.
    """

    # Supported display options:
    # Cycle - go through the selected effects in order.
    # Random - out of the selected effects pick one at random each time.
    CYCLE_DISPLAY = "CYCLE"
    RANDOM_DISPLAY = "RANDOM"

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
            if effect_class is None:
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
            effect = EffectFactory.load_effect(effects_package + effect_module, None, *args, **kwargs)
            effects[effect.get_name().upper()] = effect
        return effects

    def __init__(self, effects_path: str, effects_package: str, canvas: Canvas) -> None:
        """
        Initialise the effect factory.
        :param effects_path: path on the file system to the effects to load
        :param effects_package: the name of the associated package
        :param canvas: to be used by all effects
        """
        self.effects_available = self.load_effects(effects_path, effects_package, canvas)
        self.effects_selected = []
        self.effect_display = None
        self.next_effect = -1

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

    def validate_effect_names(self, effects_selected: List[str]) -> List[str]:
        """
        Check that the effect names supplied are in the list of effects available.
        :param effects_selected: names from command line
        :return: List of names which don't match with anything in the available list
        """
        names_in_error = []
        for name in effects_selected:
            try:
                self.get_effect(name)
            except KeyError:
                names_in_error.append(name)
        return names_in_error

    def set_effects_to_display(self, effect_display: str, effects_selected: List[str]) -> None:
        """
        Set the effect display and the list of effects to be used.
        :param effect_display: In a CYCLE or at RANDOM
        :param effects_selected: List of the effect names to use
        :return: No meaningful return
        """
        assert effect_display in (self.CYCLE_DISPLAY, self.RANDOM_DISPLAY),\
            "Effect display must be {0} or {1}!".format(self.CYCLE_DISPLAY, self.RANDOM_DISPLAY)
        self.effect_display = effect_display
        if effects_selected:
            self.effects_selected = effects_selected
        else:
            self.effects_selected = []
            for effect in self.get_all_effects():
                self.effects_selected.append(effect.get_name())

    def get_count_effects_selected(self) -> int:
        """
        The number of effects to display.
        :return: The number of effects selected.
        """
        return len(self.effects_selected)

    def get_next_effect(self) -> AbstractEffect:
        """
        Pick the next effect to display.
        :return: The next effect to show
        """
        if self.effect_display is None or not self.effects_selected:
            raise ValueError("No effects selected!")
        if self.effect_display == self.CYCLE_DISPLAY:
            self.next_effect = (self.next_effect + 1) % len(self.effects_selected)
        if self.effect_display == self.RANDOM_DISPLAY:
            self.next_effect = randint(0, len(self.effects_selected) - 1)
        effect = self.get_effect(self.effects_selected[self.next_effect])
        logging.info(str(effect))
        return effect
