import threading
from abc import abstractmethod

from hexsilicon.presentation.runner.observer import Observer
from hexsilicon.problems.free.freeproblem import FreeProblem
from hexsilicon.swarms.observable import Observable


class Swarm(Observable):

    def __init__(self, behavior=None, problem=None):
        self.hyperparams = {
            'n_agents': {
                "name": "Agentes",
                "value": 10,
                "range": (1, 100),
                "description": "Cantidad de agentes en el enjambre"
            }
        }
        self.history = {}
        self.description = ""
        self.behavior = behavior(self)
        self.problem = problem
        self.best_agent = None
        self.population = []
        self.observers = []
        self.current_iteration = 0

    @abstractmethod
    def generate_swarm(self):
        pass

    def metaheuristic(self):
        self.behavior.move_swarm(self)
        self.behavior.update_swarm(self)
        self.history[self.current_iteration] = self.best_agent.get_score()
        self.current_iteration += 1
        self.notify(self)

    @staticmethod
    @abstractmethod
    def get_description():
        pass

    @abstractmethod
    def get_passed_points_agent(self, idx):
        pass

    @abstractmethod
    def to_2d(self):
        pass

    def has_free_problem(self):
        return isinstance(self.problem, FreeProblem)

    def get_best_agent(self):
        return self.best_agent.get_solution()

    def get_hyperparams(self):
        return self.hyperparams | self.behavior.get_hyperparams()

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, swarm):
        for observer in self.observers:
            observer.update(swarm)

    def get_history(self):
        return self.history
