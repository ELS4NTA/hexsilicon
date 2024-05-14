import networkx as nx
import numpy as np

from hexsilicon.problems.solution import Solution
from hexsilicon.swarms.agent import Agent
from hexsilicon.swarms.swarm import Swarm


class AntColony(Swarm):

    def __init__(self, behavior=None, problem=None):
        super().__init__(behavior, problem)
        self.pheromone_matrix = None
        self.path_history = {}

    def generate_swarm(self):
        n_agents = self.get_hyperparams()["n_agents"]["value"]
        self.pheromone_matrix = np.empty((0, 0))
        self.population = [Agent("Ant") for _ in range(n_agents)]

    def metaheuristic(self):
        num_iterations = self.behavior.get_hyperparams()["n_iterations"]["value"]
        for i in range(num_iterations):
            self.create_solutions()
            self.behavior.update_swarm(self)
            self.history[i] = self.best_agent.get_score()
            self.path_history[i] = self.best_agent.get_solution()
            self.notify(self)

    def create_solutions(self):
        alpha = self.behavior.get_hyperparams()["alpha"]["value"]
        beta = self.behavior.get_hyperparams()["beta"]["value"]
        rng = np.random.default_rng(seed=42)
        for ant in self.population:
            haveSolution = False
            while not haveSolution:
                current_node = self.problem.get_random_point()
                path = [current_node]
                isGoodPath = True
                while self.problem.check_restrictions(path) and isGoodPath:
                    next_nodes = self.problem.get_next_nodes(current_node)
                    next_nodes = [node for node in next_nodes if node not in path]
                    if len(next_nodes) != 0:
                        probabilities = np.zeros(len(next_nodes))
                        for i, next_node in enumerate(next_nodes):
                            pheromone = self.get_edge_pheromone(current_node, next_node)
                            weight = self.problem.get_edge_weight(current_node, next_node)
                            probabilities[i] = (pheromone ** alpha) * ((1 / weight) ** beta)
                        probabilities = np.divide(probabilities, np.sum(probabilities))
                        next_node = rng.choice(next_nodes, p=probabilities)
                        path.append(next_node)
                        current_node = next_node
                    else:
                        isGoodPath = False
                if isGoodPath:
                    ant.solution = Solution(representation=path)
                    ant.set_score(self.problem.call_function(ant.solution))
                    haveSolution = True

    def get_edge_pheromone(self, current_node, next_node):
        max_node_index = max(current_node, next_node)
        required_shape = (max_node_index + 1, max_node_index + 1)
        if self.pheromone_matrix.shape[0] < required_shape[0]:
            # Create a new, larger matrix with zeros
            new_matrix = np.zeros(required_shape)
            # Copy existing values from the old matrix to the new one
            new_matrix[:self.pheromone_matrix.shape[0], :self.pheromone_matrix.shape[1]] = self.pheromone_matrix
            # Set the pheromone_matrix reference to the new, extended matrix
            self.pheromone_matrix = new_matrix

        # Access and potentially initialize the pheromone value
        pheromone_value = self.pheromone_matrix[current_node, next_node]
        if pheromone_value == 0:
            pheromone_0 = self.behavior.get_hyperparams()["pheromone_0"]["value"]
            self.pheromone_matrix[current_node, next_node] = pheromone_0
            pheromone_value = pheromone_0
        return pheromone_value

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