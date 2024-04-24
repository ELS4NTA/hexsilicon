import networkx as nx
import numpy as np

from hexsilicon.problems.solution import Solution
from hexsilicon.swarms.agent import Agent
from hexsilicon.swarms.swarm import Swarm


class AntColony(Swarm):

    def __init__(self, behavior=None, problem=None):
        super().__init__(behavior, problem)
        self.pheromone_matrix = None
        self.weights_matrix = None

    def generate_swarm(self):
        graph = self.problem.get_representation()
        n_agents = self.get_hyperparams()["n_agents"]["value"]
        # No lo da en orden :(
        self.weights_matrix = nx.to_pandas_adjacency(graph).sort_index().sort_index(axis=1).values
        self.pheromone_matrix = np.zeros((len(graph.nodes), len(graph.nodes)))
        self.pheromone_matrix.fill(self.behavior.get_hyperparams()["pheromone_0"]["value"])
        self.population = [Agent("Ant") for _ in range(n_agents)]

    def metaheuristic(self):
        num_iterations = self.behavior.get_hyperparams()["n_iterations"]["value"]
        for i in range(num_iterations):
            print("iteration", i)
            self.create_solutions()
            self.behavior.update_swarm(self)
            self.history[i] = self.best_agent.get_score()
        self.notify(self)

    def create_solutions(self):
        alpha = self.behavior.get_hyperparams()["alpha"]["value"]
        beta = self.behavior.get_hyperparams()["beta"]["value"]
        rng = np.random.default_rng(seed=42)
        for ant in self.population:
            current_node = self.problem.get_random_point()
            path = [current_node]
            while self.problem.check_restrictions(path):
                next_nodes = self.problem.get_next_nodes(current_node)
                probabilities = np.zeros(len(next_nodes))
                for i, next_node in enumerate(next_nodes):
                    probabilities[i] = self.pheromone_matrix[current_node-1][next_node-1] ** alpha \
                                       * (1 / self.weights_matrix[current_node-1][next_node-1]) ** beta
                probabilities = np.divide(probabilities, np.sum(probabilities))
                next_node = rng.choice(next_nodes, p=probabilities)
                path.append(next_node)
                current_node = next_node
            ant.solution = Solution(representation=path)
            ant.set_score(self.problem.call_function(ant.solution))

    def get_best_agent(self):
        return self.best_agent.get_solution()

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
