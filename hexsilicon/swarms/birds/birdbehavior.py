from abc import abstractmethod

from hexsilicon.swarms.behavior import Behavior


class BirdBehavior(Behavior):

    def move_swarm(self, swarm):
        pass

    def update_swarm(self, swarm):
        pass

    @staticmethod
    @abstractmethod
    def get_description():
        pass

    def get_hyperparams(self):
        pass

    def get_hyperparams_description(self):
        pass
