from hexsilicon.swarms.behavior import Behavior


class AntBehavior(Behavior):

    def __init__(self, swarm=None):
        self.hyperparams = {
            'n_iterations': {
                "name": "Iteraciones",
                "value": 20,
                "range": (1, 1000),
                "description": "Cantidad de iteraciones en el enjambre"
            }
        }
        self.swarm = swarm

    def move_swarm(self, swarm):
        pass

    def update_swarm(self, swarm):
        pass

    @staticmethod
    def get_description():
        pass

    def get_hyperparams(self):
        return self.hyperparams

    def get_hyperparams_description(self):
        pass
