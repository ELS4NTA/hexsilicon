from abc import abstractmethod
from hexsilicon.problems.problem import Problem


class FreeProblem(Problem):

    def __init__(self, context=None):
        super().__init__(context)
        
    @abstractmethod
    def get_dimensions(self):
        pass

    @abstractmethod
    def generate_solution(self):
        pass

    @abstractmethod
    def clip_velocity(self, temp_velocity):
        pass

