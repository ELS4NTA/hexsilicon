import pandas as pd
import networkx as nx

from hexsilicon.problems.functions.roadcost import RoadCostFunction
from hexsilicon.problems.problem import Problem


class MinPath(Problem):

    def __init__(self, context):
        super().__init__()
        self.function = RoadCostFunction()
        self.context = context
        self.representation = self.make_representation()

    def get_next_nodes(self, current_node):
        return list(self.representation.neighbors(current_node))

    def check_restrictions(self, solution):
        if solution[0] == self.df['initial'][0] and solution[-1] == self.df['final'][0]:
            return True
        return False
        
    def make_representation(self):
        self.df = pd.read_csv(self.context, sep=";")
        df_formatted = pd.DataFrame({
            'source': self.df['source'],
            'target': self.df['target'],
            'weight': self.df['weight'].astype(float)
        })
        return nx.from_pandas_edgelist(df_formatted, 'source', 'target', ['weight'])
    
    def get_random_point(self):
        return self.df['initial'][0]    
        
    def get_representation(self):
        return self.representation

    def is_minimization(self):
        return True if self.df['minimization'][0] == 'yes' else False

    @staticmethod
    def get_description():
        return {
            "name": "Camino Mínimo",
            "description": "Consiste en determinar la distancia más corta que hay entre dos nodos de un grafo.",
            "algorithms": "SACO, MMAS",
            "class_name": "MinPath"
        }

    def get_restrictions(self):
        pass
