from hexsilicon.domain.problem.problem import Problem
from abc import abstractmethod


class Swarm(object):

    def __init__(self, hyperparams: dict, problem: Problem):
        self.hyperparams = hyperparams
        self.problem = problem

    @abstractmethod
    def generate_initial_swarm(self):
        pass

    @abstractmethod
    def metaheuristic(self):
        pass

    @abstractmethod
    def generate_initial_solution(self):
        pass

    @abstractmethod
    def update_swarm(self):
        pass
