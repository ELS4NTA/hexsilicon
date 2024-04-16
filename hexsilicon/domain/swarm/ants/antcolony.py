import networkx as nx
import numpy as np

from hexsilicon.domain.problem.problem import Problem
from hexsilicon.domain.problem.solution import Solution
from hexsilicon.domain.swarm.agent import Agent
from hexsilicon.domain.swarm.swarm import Swarm


class AntColony(Swarm):

    def __init__(self):
        super().__init__()

    def generate_swarm(self):
        graph = self.problem.get_representation()
        n_agents = self.behavior.get_hyperparams["n_agents"][0]
        pheromone_0 = self.behavior.get_hyperparams["pheromone_0"][0]
        for edge in graph.edges(data=True):
            edge[2]['pheromone'] = pheromone_0
        self.population = [Agent("Ant") for _ in range(n_agents)]

    def mataheuristic(self):
        self.generate_swarm()
        num_iterations = self.behavior.get_hyperparams["n_iterations"][0]
        for i in range(num_iterations):
            self.behavior.move_swarm(self)
            self.behavior.update_swarm(self)
            self.history[i] = self.best_agent.get_score()
            self.notify(self)

    def get_best_solution(self):
        return self.best_agent.get_solution()

    def get_description(self):
        return """La metaheurística ACO se inspira en la observación 
                  del comportamiento de colonias de hormigas reales, 
                  que presentaban una característica interesante: 
                  cómo encontrar los caminos más cortos entre el nido
                  y la comida."""
