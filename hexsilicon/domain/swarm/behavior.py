from abc import ABC, abstractmethod


class Behavior(ABC):

    @abstractmethod
    def get_hyperparams(self):
        pass

    @abstractmethod
    def get_hyperparams_description(self):
        pass

    @abstractmethod
    def move_swarm(self):
        pass

    @abstractmethod
    def update_swarm(self):
        pass
