from abc import ABC, abstractmethod
from random import randint
from typing import List


class AbstractEffectDisplay(ABC):

    # Supported display options:
    # Cycle - go through the selected effects in order.
    # Random - out of the selected effects pick one at random each time.
    CYCLE_DISPLAY = "CYCLE"
    RANDOM_DISPLAY = "RANDOM"

    def __init__(self, effect_count: int):
        self.effect_count = effect_count
        self.next_effect = -1

    @classmethod
    def get_display_options(cls) -> List[str]:
        """
        Create a list of all the display options.
        :return: A list of all the display option.
        """
        return [cls.CYCLE_DISPLAY, cls.RANDOM_DISPLAY]

    @classmethod
    def get_default_option(cls) -> str:
        """
        The default display option.
        :return: The display option to use as a default.
        """
        return cls.CYCLE_DISPLAY

    @classmethod
    def select_effect_display(cls, display_option: str, effect_count: int) -> 'AbstractEffectDisplay':
        """
        Determine the function to use for the selected display option.
        :param display_option: In a CYCLE or at RANDOM
        :return: A function defining how the selected display option should work.
        """
        assert display_option in (cls.CYCLE_DISPLAY, cls.RANDOM_DISPLAY), \
            "Effect display must be {0} or {1}!".format(cls.CYCLE_DISPLAY, cls.RANDOM_DISPLAY)
        if display_option == cls.CYCLE_DISPLAY:
            return CycleEffects(effect_count)
        if display_option == cls.RANDOM_DISPLAY:
            return RandomEffects(effect_count)

    @abstractmethod
    def get_next_effect(self) -> int:
        """
        Determine the next index to use.
        :return: The next index value to use
        """
        pass


class CycleEffects(AbstractEffectDisplay):

    def get_next_effect(self) -> int:
        """
        Determine the next index to the effects selected in a cycle.
        :return: The next index value to use
        """
        self.next_effect = (self.next_effect + 1) % self.effect_count
        return self.next_effect


class RandomEffects(AbstractEffectDisplay):

    def get_next_effect(self) -> int:
        """
        Determine the next index to the effects selected as a random number.
        :return: The next index value to use
        """
        return randint(0, self.effect_count - 1)
