from abc import abstractmethod

from hexsilicon.swarms.behavior import Behavior


class FireflyBehavior(Behavior):
    """
    Represents the behavior of fireflies in a swarm.
    """

    def __init__(self, swarm=None):
        self.hyperparams = {
            'n_iterations': {
                "name": "Iteraciones",
                "value": 100,
                "range": (100, 1000),
                "description": "Cantidad de iteraciones en el enjambre"
            }
        }
        self.swarm = swarm
        self.set_hyperparams()

    def set_hyperparams(self):
        self.hyperparams.update({
            "alpha": {
                "name": "Alpha",
                "value": 0.5,
                "range": (0.1, 1.0),
                "description": "Influencia del brillo de la luciérnaga"
            },
            "beta": {
                "name": "Beta",
                "value": 0.2,
                "range": (0.2, 1.0),
                "description": "Influencia de la distancia entre luciérnagas"
            },
            "gamma": {
                "name": "Gamma",
                "value": 0.1,
                "range": (0.1, 1.0),
                "description": "Influencia de la intensidad de la luz"
            },
            "theta": {
                "name": "Theta",
                "value": 0.9,
                "range": (0.1, 1.0),
                "description": "Decaimiento de la influencia de la luz alpha."
            },
        })

    @abstractmethod
    def move_swarm(self, swarm):
        pass

    @abstractmethod
    def update_swarm(self, swarm):
        pass

    def get_hyperparams(self):
        return self.hyperparams

    @staticmethod
    @abstractmethod
    def get_description():
        pass
