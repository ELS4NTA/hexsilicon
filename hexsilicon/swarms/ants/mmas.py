import numpy as np
from hexsilicon.swarms.ants.antbehavior import AntBehavior


# Max-Min Ant System (MMAS) algorithm
class MMAS(AntBehavior):
    """
    The MMAS (Max-Min Ant System) class represents an implementation of the ACO (Ant Colony Optimization) algorithm
    with the Max-Min Ant System enhancement. It guarantees the convergence of the algorithm.

    Attributes:
        swarm (Swarm): The swarm associated with the behavior.
    """

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.hyperparams.update({
            "tau_min": {
                "name": "Tau Min",
                "value": 0.001,
                "range": (0.0, 1.0),
                "description": "Nivel mínimo de feromona"
            },
            "tau_max": {
                "name": "Tau Max",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Nivel máximo de feromona"
            }
        })

    def update_swarm(self, swarm):
        rho = self.hyperparams['rho']['value']
        tau_min = self.hyperparams["tau_min"]["value"]
        tau_max = self.hyperparams["tau_max"]["value"]
        is_minimization = swarm.problem.is_minimization()
        func = min if is_minimization else max
        best_ant = func(swarm.population, key=lambda agent: agent.get_score())
        if swarm.best_agent.solution is None:
            swarm.best_agent.solution = best_ant.solution
        update_best = best_ant.get_score() < swarm.best_agent.get_score() if is_minimization else best_ant.get_score() > swarm.best_agent.get_score()

        # Update global best if the current best ant is better
        if update_best:
            swarm.best_agent.solution = best_ant.solution

        # Pheromone evaporation
        swarm.pheromone_matrix *= (1 - rho)

        # Update pheromone levels on the global best ant's path
        best_gobal_path = swarm.best_agent.get_solution()
        for i in range(len(best_gobal_path) - 1):
            new_pheromone = 1 / swarm.best_agent.get_score()
            swarm.pheromone_matrix[best_gobal_path[i], best_gobal_path[i + 1]] = np.clip(new_pheromone, tau_min, tau_max)

    def get_pheromone_initial(self):
        return self.hyperparams["tau_max"]["value"]

    @staticmethod
    def get_description():
        return {
            "name": "MMAS",
            "description": "El algoritmo Max-Min Ant System es una mejora del ACO que garantiza la convergencia del algoritmo.",
            "class_name": "MMAS"
        }
