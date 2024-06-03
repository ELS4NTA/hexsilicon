from abc import ABC, abstractmethod


class ProblemVisualization(ABC):

    @abstractmethod
    def __init__(self, fig):
        pass

    @abstractmethod
    def draw(self, swarm):
        pass
