from abc import abstractmethod

from hexsilicon.presentation.runner.observer import Observer
from hexsilicon.problems.problem import Problem
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

    @abstractmethod
    def generate_swarm(self):
        pass

    @abstractmethod
    def metaheuristic(self):
        pass

    @staticmethod
    @abstractmethod
    def get_description():
        pass

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
