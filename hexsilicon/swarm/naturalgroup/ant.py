from hexsilicon.problem.problem import Problem
from hexsilicon.problem.solution import Solution
from hexsilicon.swarm.agent import Agent
from hexsilicon.swarm.behavior import Behavior
from hexsilicon.swarm.swarm import Swarm
from abc import abstractmethod
import numpy as np


class AntGroup(Swarm, Behavior):

    def __init__(self, hyperparams: dict, problem: Problem):
        super().__init__(hyperparams, problem)
        self.population = None

    def generate_initial_swarm(self):
        self.population = np.array(Agent(self.generate_initial_solution()), size=self.hyperparams['population_size'])

    def metaheuristic(self):
        n_points = self.problem.domain.space["n_points"]
        pheromone = np.ones((n_points, n_points))
        best_path = None
        best_path_length = np.inf
        for iteration in range(self.hyperparams['max_iterations']):
            self.update_swarm()
            self.movement_swarm()
            for ant in self.population:
                path = ant.solution.path
                path_length = self.problem.function.evaluate(path)
                if path_length < best_path_length:
                    best_path = path
                    best_path_length = path_length
                for i in range(n_points - 1):
                    pheromone[path[i], path[i + 1]] += 1 / path_length
                pheromone[path[-1], path[0]] += 1 / path_length
            pheromone *= self.hyperparams['evaporation_rate']

    def generate_initial_solution(self):
        path = np.random.randint(0, self.problem.domain.space["n_points"], size=self.problem.domain.space["n_points"], replace=False)
        solution = Solution(self.problem.domain, path)
        return solution

    @abstractmethod
    def update_swarm(self):
        pass

    @abstractmethod
    def movement_swarm(self):
        pass


