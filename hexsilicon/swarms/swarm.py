from abc import abstractmethod

from hexsilicon.presentation.observer import Observer
from hexsilicon.problems.problem import Problem
from hexsilicon.swarms.observable import Observable


class Swarm(Observable):

    def __init__(self):
        self.history = {}
        self.description = ""
        self.problem = Problem()
        self.best_agent = None
        self.behavior = None
        self.population = []
        self.observers = []

    @abstractmethod
    def generate_swarm(self):
        pass

    @abstractmethod
    def metaheuristic(self):
        pass

    @abstractmethod
    def get_best_agent(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        list(map(lambda observer: observer.update(*args, **kwargs), self.observers))

    def get_history(self):
        return self.history
