from abc import ABC, abstractmethod


class Restriction(ABC):

    @abstractmethod
    def is_valid(self):
        pass