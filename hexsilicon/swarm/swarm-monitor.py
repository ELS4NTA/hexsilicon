from hexsilicon.problem.problem import Problem
from abc import abstractmethod


class Swarm(object):

    def __init__(self, hyperparams: dict, problem: Problem):
        self.hyperparams = hyperparams
        self.problem = problem
        self.behavior = None

    @abstractmethod
    def generate_initial_swarm(self):
        pass

    @abstractmethod
    def metaheuristic(self):
        pass

    @abstractmethod
    def update_swarm(self):
        pass
