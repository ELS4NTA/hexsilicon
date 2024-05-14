from abc import ABC, abstractmethod


class Behavior(ABC):

    @abstractmethod
    def move_swarm(self, swarm):
        pass

    @abstractmethod
    def update_swarm(self, swarm):
        pass

    @staticmethod
    @abstractmethod
    def get_description():
        pass

    @abstractmethod
    def get_hyperparams(self):
        pass
