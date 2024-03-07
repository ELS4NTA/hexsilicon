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
        alpha = self.hyperparams['alpha']
        beta = self.hyperparams['beta']
        pheromone = np.ones((n_points, n_points))
        points = np.random.rand(n_points, self.problem.domain.space["n_dimensions"])
        best_path = None
        best_path_length = np.inf
        for _ in range(self.hyperparams['max_iterations']):
            paths = []
            path_lengths = []
            for _ in range(self.population):
                visited = np.zeros(n_points, dtype=bool)
                current_point = np.random.randint(n_points)
                visited[current_point] = True
                path = np.array([current_point])
                path_length = 0
                self.movement_swarm(visited, pheromone, path_length, path, points, alpha, beta, current_point)

                paths.append(path)
                path_lengths.append(path_length)

            self.update_swarm(path, best_path, best_path_length, pheromone)

    def generate_initial_solution(self):
        path = np.random.randint(0, self.problem.domain.space["n_points"], size=self.problem.domain.space["n_points"], replace=False)
        solution = Solution(self.problem.domain, path)
        return solution
    
    def distance(self, point1, point2):
        return np.sqrt(np.sum((point1 - point2)**2))

    @abstractmethod
    def update_swarm(self, paths, path_lengths, pheromone):
        pass

    @abstractmethod
    def movement_swarm(self, visited, pheromone, path, path_length, points, alpha, beta, current_point):
        pass
