from hexsilicon.swarms.behavior import Behavior


class AntBehavior(Behavior):

    def __init__(self, swarm=None):
        self.swarm = swarm
        self.hyperparams = {
            'n_iterations': (20, 1, 1000),
        }

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
