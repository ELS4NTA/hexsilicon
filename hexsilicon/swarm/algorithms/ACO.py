from hexsilicon.swarm.naturalgroup.ant import AntGroup
import numpy as np


# Simple Ant Colony Optimization (SACO) algorithm
class SACO(AntGroup):

    def __init__(self, hyperparams: dict, problem):
        super().__init__(hyperparams, problem)

    def movement_swarm(self, visited, path, current_point):
        while False in visited:
            unvisited = np.where(np.logical_not(visited))[0]
            next_nodes = self.problem.get_representation().neighbors(current_point)
            probabilities = np.zeros(len(next_nodes))
            for i, unvisited_point in enumerate(unvisited):
                for next in next_nodes:
                    probabilities[i] = self.problem.get_representation().get_edge_data(i, next)['pheromone']
            probabilities = np.divide(probabilities, np.sum(probabilities))
            next_point = np.random.choice(unvisited, p=probabilities)
            path.append(next_point)
            visited[next_point] = True
            current_point = next_point
        return path

    def update_swarm(self):
        graph = self.problem.get_representation()
        for edge in graph.edges():
            edge[2]['pheromone'] *= (1 - self.hyperparams['evaporation_rate']) + self.hyperparams['delta_pheromone']
