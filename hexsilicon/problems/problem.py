from abc import abstractmethod


class Problem(object):

    def __init__(self, context=None):
        self.function = None
        self.searchspace = None
        self.context = context
    
    @abstractmethod
    def make_representation(self):
        pass

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
    def get_random_point(self):
        pass
    
    @abstractmethod
    def get_next_nodes(self, current_node):
        pass
    
    @abstractmethod
    def is_minimization(self):
        pass

    def call_function(self, solution) -> float:
        return self.function.evaluate(solution, self.representation)
