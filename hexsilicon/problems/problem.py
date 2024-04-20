from abc import abstractmethod


class Problem(object):

    def __init__(self):
        self.function = None
        self.searchspace = None

    @abstractmethod
    def get_representation(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_restrictions(self):
        pass

    def call_function(self, solution) -> float:
        return self.function.evaluate(solution, self.representation)
