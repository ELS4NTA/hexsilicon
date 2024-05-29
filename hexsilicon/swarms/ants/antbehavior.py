from abc import abstractmethod
from hexsilicon.swarms.behavior import Behavior


class AntBehavior(Behavior):

    def __init__(self, swarm=None):
        self.hyperparams = {
            'n_iterations': {
                "name": "Iterations",
                "value": 50,
                "range": (1, 1000),
                "description": "Number of iterations in the swarm"
            },
        }
        self.swarm = swarm
        self.set_hyperparams()

    def set_hyperparams(self):
        self.hyperparams.update({
            "pheromone_0": {
                "name": "Initial Pheromone",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Initial pheromone on each path"
            },
            "rho": {
                "name": "Rho",
                "value": 0.01,
                "range": (0.0, 0.2),
                "description": "Pheromone evaporation rate"
            },
            "alpha": {
                "name": "Alpha",
                "value": 1.0,
                "range": (0.0, 10.0),
                "description": "Valor de importancia de feromona"
            },
            "beta": {
                "name": "Beta",
                "value": 1.0,
                "range": (0.0, 10.0),
                "description": "Valor de importancia de heuristica del problema"
            },
        })

    @abstractmethod
    def move_swarm(self, swarm):
        pass

    @abstractmethod
    def update_swarm(self, swarm):
        pass

    @abstractmethod
    def get_pheromone_initial(self):
        pass

    def get_hyperparams(self):
        return self.hyperparams

    @staticmethod
    @abstractmethod
    def get_description():
        pass
