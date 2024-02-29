from abc import ABC, abstractmethod


class Swarm(ABC):

    def __init__(self):
        self.hyperparams = {}

    @abstractmethod
    def generate_initial_swarm(self):
        pass

    @abstractmethod
    def movement_swarm(self):
        pass

    @abstractmethod
    def update_swarm(self):
        pass
