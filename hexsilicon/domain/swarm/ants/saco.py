import numpy as np

from hexsilicon.domain.swarm.behavior import Behavior


# Simple Ant Colony Optimization (SACO) algorithm
class SACO(Behavior):

    def __init__(self, problem):
        super().__init__(problem)
        self.hyperparams = {
            'rho': (0.01, 0.0, 0.2),
            'q': (1, 0, 10),
            'n_agents': (7, 1, 100),
            'pheromone_0': (1, -7, 50),
            'n_iterations': (20, 1, 1000)
        }

    def move_swarm(self, path, current_point):
        while self.problem.domain.restriction.get_restriction()['final_point'] != current_point:
            next_nodes = list(
                self.problem.get_representation().neighbors(current_point))
            probabilities = np.zeros(len(next_nodes))
            for i, next in enumerate(next_nodes):
                probabilities[i] = self.problem.get_representation().get_edge_data(current_point, next)[
                    'pheromone'] / self.problem.get_representation().get_edge_data(current_point, next)['weight']
            probabilities = np.divide(probabilities, np.sum(probabilities))
            next_point = np.random.choice(next_nodes, p=probabilities)
            path = np.append(path, next_point)
            current_point = next_point
        return path

    def update_swarm(self):
        graph = self.problem.get_representation()
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
