import numpy as np

from hexsilicon.swarms.ants.antbehavior import AntBehavior


# Max-Min Ant System (MMAS) algorithm
class MMAS(AntBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.hyperparams.update({
            "tau_min": {
                "name": "Tau Min",
                "value": 0.001,
                "range": (0.0, 1.0),
                "description": "Minimum pheromone level"
            },
            "tau_max": {
                "name": "Tau Max",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Maximum pheromone level"
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
