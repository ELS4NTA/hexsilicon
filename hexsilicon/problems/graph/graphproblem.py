from abc import abstractmethod
from hexsilicon.problems.problem import Problem


class GraphProblem(Problem):
    def __init__(self, context=None):
        super().__init__(context)
        self.representation = self.make_representation()
        
    @abstractmethod
    def make_representation(self):
        pass
    
    @abstractmethod
    def get_random_point(self):
        pass
    
    @abstractmethod
    def get_next_nodes(self, current_node):
        pass
    
    @abstractmethod
    def get_edge_weight(self, node1, node2):
        pass
    
    def get_number_of_nodes(self):
        return len(self.representation.nodes)
    