from hexsilicon.swarm.swarm import Swarm
from abc import ABC, abstractmethod


class Ant(Swarm, ABC):
    @abstractmethod
    def generate_initial_swarm(self):
        pass

    @abstractmethod
    def movement_swarm(self):
        pass

    @abstractmethod
    def update_swarm(self):
        pass


def ant_algorithm(antimpl):
    antimpl.__isAntSwarm__ = True
