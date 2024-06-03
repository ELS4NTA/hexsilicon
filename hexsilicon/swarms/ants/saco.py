import numpy as np

from hexsilicon.swarms.ants.antbehavior import AntBehavior


# Simple Ant Colony Optimization (SACO) algorithm or Ant System (AS) algorithm
class SACO(AntBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.hyperparams.update({
            "q": {
                "name": "q",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Importancia de la feromona"
            }
        })

    def update_swarm(self, swarm):
        is_minimization = swarm.problem.is_minimization()
        q = self.hyperparams['q']['value']
        rho = self.hyperparams['rho']['value']
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

        # Pheromone deposit
        delta_pheromone = np.zeros_like(swarm.pheromone_matrix)
        for ant in swarm.population:
            path = ant.get_solution()
            for i in range(len(path) - 1):
                delta_pheromone[path[i], path[i + 1]] += q / ant.get_score()
        swarm.pheromone_matrix = swarm.pheromone_matrix + delta_pheromone

    def get_pheromone_initial(self):
        return self.hyperparams["pheromone_0"]["value"]

    @staticmethod
    def get_description():
        return {
            "name": "SACO",
            "description": "Es el algoritmo más simple de la familia de las colonias de hormigas. Teniendo en cuenta "
                           "solo la feromona en los caminos",
            "class_name": "SACO",
        }
