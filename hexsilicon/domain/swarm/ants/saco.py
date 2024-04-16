import numpy as np

from hexsilicon.domain.problem.solution import Solution
from hexsilicon.domain.swarm.behavior import Behavior


# Simple Ant Colony Optimization (SACO) algorithm or Ant System (AS) algorithm
class SACO(Behavior):

    def __init__(self):
        self.hyperparams = {
            'rho': (0.01, 0.0, 0.2),
            'q': (1, 0, 10),
            'n_agents': (7, 1, 100),
            'pheromone_0': (1, -7, 50),
            'n_iterations': (20, 1, 1000)
        }

    def move_swarm(self, swarm):
        graph = swarm.problem.get_representation()
        restrictions = swarm.problem.get_restriction()
        start_node = restrictions['initial_point']
        end_node = restrictions['final_point']
        rng = np.random.default_rng(seed=42)
        best_score = np.inf
        for ant in swarm.population:
            current_node = start_node
            path = [current_node]
            while current_node != end_node:
                next_nodes = list(graph.neighbors(current_node))
                probabilities = np.zeros(len(next_nodes))
                for i, next_node in enumerate(next_nodes):
                    probabilities[i] = graph.get_edge_data(current_node, next_node)['pheromone'] \
                                    / graph.get_edge_data(current_node, next_node)['weight']
                probabilities = np.divide(probabilities, np.sum(probabilities))
                next_node = rng.choice(next_nodes, p=probabilities)
                path.append(next_node)
                current_node = next_node
            ant.solution = Solution(representation=path)
            score = self.problem.call_function(ant.solution)
            if score < best_score:
                best_score = score
                swarm.best_agent = ant

    def update_swarm(self, swarm):
        graph = swarm.problem.get_representation()
        for edge in graph.edges(data=True):
            edge[2]['pheromone'] *= (1 - self.hyperparams['rho'][0])
            edge[2]['pheromone'] += self.hyperparams['q'][0]

    def get_hyperparams(self):
        return self.hyperparams

    def get_hyperparams_description(self):
        return {
            'rho': 'Tasa de evaporación de feromonas',
            'q': 'Cantidad de feromonas depositadas por la hormiga',
            'n_agents': 'N\u00famero de hormigas',
            'pheromone_0': 'Feromona inicial',
            'n_iterations': 'N\u00famero de iteraciones'
        }
