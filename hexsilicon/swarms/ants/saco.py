from hexsilicon.swarms.ants.antbehavior import AntBehavior


# Simple Ant Colony Optimization (SACO) algorithm or Simple Ant System (AS) algorithm
class SACO(AntBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.set_hyperparams()

    def move_swarm(self, swarm):
        pass

    def update_swarm(self, swarm):
        func = min if swarm.problem.is_minimization() else max
        swarm.best_agent = func(swarm.population, key=lambda agent: agent.get_score())
        swarm.pheromone_matrix *= (1 - self.hyperparams['rho']["value"])
        swarm.pheromone_matrix += self.hyperparams['q']["value"]

    def get_hyperparams(self):
        return self.hyperparams
        
    def set_hyperparams(self):
        self.hyperparams = self.hyperparams | {
            "pheromone_0": {
                "name": "Feromona Inicial",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Feromona inicial en cada camino"
            },
            "rho": {
                "name": "Rho",
                "value": 0.01,
                "range": (0.0, 0.2),
                "description": "Tasa de evaporación de feromonas"
            },
            "q": {
                "name": "q",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Valor de importancia de feromona"
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
            }
        }

    @staticmethod
    def get_description():
        return {
            "name": "SACO",
            "description": "Es el algoritmo más simple de la familia de las colonias de hormigas. Tieniendo en cuenta "
                           "solo la feromona en los caminos",
            "class_name": "SACO",
        }
