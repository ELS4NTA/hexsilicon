from hexsilicon.domain.swarm.behavior import Behavior

# Ant System (AS) algorithm
class AS(Behavior):

    def __init__(self):
        self.hyperparams = {
            'rho': (0.01, 0.0, 0.2),
            'q': (1, 0, 10),
            'n_agents': (7, 1, 100),
            'pheromone_0': (1, -7, 50),
            'n_iterations': (20, 1, 1000)
        }

    def get_hyperparams(self):
        pass

    def get_hyperparams_description(self):
        pass

    def move_swarm(self):
        pass

    def update_swarm(self):
        pass