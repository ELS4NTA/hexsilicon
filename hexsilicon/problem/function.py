from .solution import Solution
from abc import ABC, abstractmethod


class Function(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, solution, representation):
        pass
