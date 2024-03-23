from hexsilicon.domain.swarm.naturalgroup.ant import AntGroup
import numpy as np


# Simple Ant Colony Optimization (SACO) algorithm
class SACO(AntGroup):

    def __init__(self, hyperparams: dict, problem):
        super().__init__(hyperparams, problem)

    def movement_swarm(self, path, current_point):
        while self.problem.domain.restriction.get_restriction()['final_point'] != current_point:
            next_nodes = list(self.problem.get_representation().neighbors(current_point))
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
            edge[2]['pheromone'] *= (1 - self.hyperparams['rho'])
            edge[2]['pheromone'] += self.hyperparams['q']
