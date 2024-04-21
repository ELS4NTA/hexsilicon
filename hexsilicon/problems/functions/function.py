from abc import ABC, abstractmethod


class Function(ABC):

    @abstractmethod
    def evaluate(self, solution, representation):
        pass
