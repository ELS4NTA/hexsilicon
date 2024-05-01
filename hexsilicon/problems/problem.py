from abc import abstractmethod


class Problem(object):

    def __init__(self, context=None):
        self.function = None
        self.searchspace = None
        self.context = context
        self.representation = None

    @abstractmethod
    def get_representation(self):
        pass

    @staticmethod
    @abstractmethod
    def get_description():
        pass

    @abstractmethod
    def get_restrictions(self):
        pass
    
    @abstractmethod
    def check_restrictions(self, solution):
        pass
    
    @abstractmethod
    def is_minimization(self):
        pass

    def call_function(self, solution) -> float:
        return self.function.evaluate(solution, self.representation)
