from abc import ABC, abstractmethod


class Behavior(ABC):

    @abstractmethod
    def movement_swarm(self):
        pass
