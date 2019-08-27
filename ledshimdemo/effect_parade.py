from abc import ABC, abstractmethod
import logging
from random import randint
from time import time
from typing import List

import ledshim

from .abstract_effect import AbstractEffect


class AbstractEffectParade(ABC):

    # Supported parade options:
    # Cycle - go through the selected effects in order.
    # Random - out of the selected effects pick one at random each time.
    CYCLE_PARADE = "CYCLE"
    RANDOM_PARADE = "RANDOM"

    def __init__(self, effects_selected: List[AbstractEffect]):
        self.effects_selected = effects_selected
        self.next_effect = -1

    @classmethod
    def get_parade_options(cls) -> List[str]:
        """
        Create a list of all the display options.
        :return: A list of all the display option.
        """
        return [cls.CYCLE_PARADE, cls.RANDOM_PARADE]

    @classmethod
    def get_default_option(cls) -> str:
        """
        The default display option.
        :return: The display option to use as a default.
        """
        return cls.CYCLE_PARADE

    @classmethod
    def select_effect_parade(cls, parade_option: str, effects_selected: List[AbstractEffect]) -> \
            'AbstractEffectParade':
        """
        Determine the function to use for the selected parade option.
        :param parade_option: In a CYCLE or at RANDOM
        :param effects_selected: List of the effect names to use
        :return: A function defining how the selected display option should work.
        """
        assert parade_option in (cls.get_parade_options()), \
            "Effect parade option must be one of {0}!".format(cls.get_parade_options())
        if parade_option == cls.CYCLE_PARADE:
            return CycleEffects(effects_selected)
        if parade_option == cls.RANDOM_PARADE:
            return RandomEffects(effects_selected)

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
        next_effect = self.get_next_effect_index()
        effect = self.effects_selected[next_effect]
        logging.info(str(effect))
        return effect

    def render(self, duration: int, repeat: int, lead: bool) -> None:
        """
        Render the effects selected,
        :param duration: How long to display each effect for
        :param repeat: How many times to run effects
        :param lead: Act as a lead for other instances to follow
        :return: No meaningful return
        """
        ledshim.set_clear_on_exit()
        try:
            for i in range(repeat):
                for j in range(self.get_count_effects_selected()):
                    effect = self.get_next_effect()
                    start_effect = time()
                    while (time() - start_effect) < duration:
                        effect.render()
        except KeyboardInterrupt:
            logging.info("Execution interrupted!")
        finally:
            ledshim.clear()
            ledshim.show()

    @abstractmethod
    def get_next_effect_index(self) -> int:
        """
        Determine the next index to use.
        :return: The next index value to use
        """
        pass   # pragma: no cover


class CycleEffects(AbstractEffectParade):

    def __init__(self, effects_selected: List[AbstractEffect]) -> None:
        super(CycleEffects, self).__init__(effects_selected)

    def get_next_effect_index(self) -> int:
        """
        Determine the next index to the effects selected in a cycle.
        :return: The next index value to use
        """
        self.next_effect = (self.next_effect + 1) % self.get_count_effects_selected()
        return self.next_effect


class RandomEffects(AbstractEffectParade):

    def __init__(self, effects_selected: List[AbstractEffect]) -> None:
        super(RandomEffects, self).__init__(effects_selected)

    def get_next_effect_index(self) -> int:
        """
        Determine the next index to the effects selected as a random number.
        :return: The next index value to use
        """
        return randint(0, self.get_count_effects_selected() - 1)
