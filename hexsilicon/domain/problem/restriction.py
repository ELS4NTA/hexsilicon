from abc import ABC, abstractmethod


class Restriction(ABC):

    def __init__(self, restriction: dict):
        self.restriction = restriction

    def get_restriction(self):
        return self.restriction
