from domain import Domain
from function import Function
from abc import ABC, abstractmethod


class Problem(object):

    def __init__(self, domain: Domain, function: Function) -> None:
        self.domain = domain
        self.function = function
        self.solution = None

    def set_domain(self, new_domain: Domain) -> None:
        self.domain = new_domain

    def get_domain(self) -> Domain:
        return self.domain

    @abstractmethod
    def solve(self):
        pass

