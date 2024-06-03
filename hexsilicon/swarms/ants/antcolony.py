import numpy as np

from hexsilicon.swarms.agent import Agent
from hexsilicon.swarms.swarm import Swarm


class AntColony(Swarm):

    def __init__(self, behavior, problem):
        super().__init__(behavior, problem)
        self.pheromone_matrix = np.zeros((0, 0))
        self.path_history = {}

    def generate_swarm(self):
        n_agents = self.get_hyperparams()["n_agents"]["value"]
        self.best_agent = Agent("QueenAnt")
        self.population = [Agent("Ant") for _ in range(n_agents)]

    def get_edge_pheromone(self, current_node, next_node):
        max_node_index = max(current_node, next_node)
        # Expand the pheromone matrix if needed
        if max_node_index >= self.pheromone_matrix.shape[0]:
            new_shape = (max_node_index + 1, max_node_index + 1)
            self.pheromone_matrix = np.pad(self.pheromone_matrix,
                                           ((0, new_shape[0] - self.pheromone_matrix.shape[0]),
                                            (0, new_shape[1] - self.pheromone_matrix.shape[1])),
                                           mode='constant')
        # Check if the pheromone level is 0 (uninitialized)
        if self.pheromone_matrix[current_node, next_node] == 0:
            pheromone_0 = self.behavior.get_pheromone_initial()
            self.pheromone_matrix[current_node, next_node] = pheromone_0
        return self.pheromone_matrix[current_node, next_node]

    def get_passed_points_agent(self, idx):
        return self.population[idx].get_solution()

    def to_2d(self):
        return self.problem.get_representation()

    @staticmethod
    def get_description():
        return {
            "name": "Colonia de Hormigas",
            "description": "La metaheurística ACO se inspira en la observación del comportamiento de colonias de "
                           "hormigas reales, que presentaban una característica interesante: cómo encontrar los "
                           "caminos más cortos entre el nido y la comida.",
            "behavior": "AntBehavior",
            "class_name": "AntColony"
        }
