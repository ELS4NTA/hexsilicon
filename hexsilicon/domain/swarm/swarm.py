from hexsilicon.domain.problem.problem import Problem
from hexsilicon.domain.swarm.observable import Observable
from hexsilicon.presentation.history import History
from abc import abstractmethod

from hexsilicon.presentation.observer import Observer


class Swarm(Observable):

    def __init__(self, problem: Problem):
        super().__init__()
        self.hyperparams = None
        self.problem = problem

    def generate_initial_swarm(self):
        pass

    def metaheuristic(self):
        pass

    def generate_initial_solution(self):
        pass

    def update_swarm(self):
        pass

    def get_hyperparams(self):
        return self.hyperparams
