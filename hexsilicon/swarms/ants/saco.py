from hexsilicon.swarms.ants.antbehavior import AntBehavior


# Simple Ant Colony Optimization (SACO) algorithm or Simple Ant System (AS) algorithm
class SACO(AntBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.hyperparams = {
            'pheromone_0': (1, 0, 1),
            'rho': (0.01, 0.0, 0.2),
            'alpha': (1, 0, 10),
            'beta': (1, 0, 10),
        }

    def move_swarm(self, swarm):
        pass

    def update_swarm(self, swarm):
        func = min if swarm.problem.is_minimization() else max
        swarm.best_agent = func(swarm.population, key=lambda agent: agent.get_score())
        swarm.pheromone_matrix *= (1 - self.hyperparams['rho'][0])
        swarm.pheromone_matrix += self.hyperparams['q'][0]

    def get_hyperparams(self):
        return self.hyperparams

    def get_hyperparams_description(self):
        return {
            'n_iterations': 'N\u00famero de iteraciones',
            'n_agents': 'N\u00famero de hormigas',
            'pheromone_0': 'Feromona inicial',
            'rho': 'Tasa de evaporación de feromonas',
            'q': 'Cantidad de feromonas depositadas por la hormiga',
            'alpha': 'Peso de la feromona',
            'beta': 'Peso de la distancia'
        }

    @staticmethod
    def get_description():
        return {
            "name": "SACO",
            "description": "Es el algoritmo más simple de la familia de las colonias de hormigas. Tieniendo en cuenta "
                           "solo la feromona en los caminos",
            "class_name": "SACO",
        }
