from hexsilicon.swarms.ants.antbehavior import AntBehavior
import numpy as np


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

    def move_swarm(self, swarm):
        problem = swarm.problem
        rng = np.random.default_rng()
        alpha = self.hyperparams["alpha"]["value"]
        beta = self.hyperparams["beta"]["value"]
        while True:
            current_node = problem.get_random_point()
            path = [current_node]
            is_good_path = True
            while problem.check_restrictions(path) and is_good_path:
                next_nodes = problem.get_next_nodes(current_node)
                next_nodes = [node for node in next_nodes if node not in path]
                if not next_nodes:
                    is_good_path = False
                    break
                probabilities = np.zeros(len(next_nodes))
                for i, next_node in enumerate(next_nodes):
                    pheromone = swarm.get_edge_pheromone(current_node, next_node)
                    weight = problem.get_edge_weight(current_node, next_node)
                    probabilities[i] = (pheromone ** alpha) * ((1 / weight) ** beta)
                probabilities /= probabilities.sum()
                next_node = rng.choice(next_nodes, p=probabilities)
                path.append(next_node)
                current_node = next_node
            if is_good_path:
                return path

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
