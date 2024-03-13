from .domain import Domain
from .function import Function
from abc import ABC, abstractmethod
import networkx as nx


class Problem(object):

    def __init__(self, domain: Domain, function: Function) -> None:
        self.domain = domain
        self.function = function
        self.solution = None
        self.representation = None

    def get_representation(self) -> nx.DiGraph:
        return self.representation

    def set_domain(self, new_domain: Domain) -> None:
        self.domain = new_domain

    def get_domain(self) -> Domain:
        return self.domain

    def call_function(self, solution) -> float:
        return self.function.evaluate(solution, self.representation)

