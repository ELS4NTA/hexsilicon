from abc import abstractmethod
from hexsilicon.swarms.behavior import Behavior


class ParticleBehavior(Behavior):
    """
    A base class for defining particle behavior in a swarm.

    Attributes:
        hyperparams (dict): A dictionary containing the hyperparameters for the behavior.
        swarm (Swarm): The swarm object associated with the behavior.
    """

    def __init__(self, swarm=None):
        self.hyperparams = {
            'n_iterations': {
                "name": "Iteraciones",
                "value": 50,
                "range": (1, 1000),
                "description": "Cantidad de iteraciones en el enjambre"
            }
        }
        self.swarm = swarm
        self.set_hyperparams()

    def set_hyperparams(self):
        self.hyperparams.update({
            "v_min": {
                "name": "Velocidad Minima",
                "value": 0.0,
                "range": (0.0, 1.0),
                "description": "Define la velocidad mínima de las partículas"
            },
            "v_max": {
                "name": "Velocidad Maxima",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Define la velocidad máxima de las partículas"
            },
            "w": {
                "name": "Constante Inercia",
                "value": 1.0,
                "range": (0.0, 5.0),
                "description": "Reduce o aumenta la velocidad de la particula"
            },
            "c1": {
                "name": "Constante Individual",
                "value": 2.05,
                "range": (0.0, 5.0),
                "description": "Influencia de la mejor posición individual"
            },
            "c2": {
                "name": "Constante Social",
                "value": 2.05,
                "range": (0.0, 5.0),
                "description": "Influencia de la mejor posición global"
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
