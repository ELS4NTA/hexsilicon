from abc import ABC, abstractmethod


class ProblemVisualization(ABC):
    @abstractmethod
    def draw(self, swarm, ax):
        pass
