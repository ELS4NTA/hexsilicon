from io import StringIO

import networkx as nx
import pandas as pd

from hexsilicon.problems.functions.roadcost import RoadCostFunction
from hexsilicon.problems.graph.graphproblem import GraphProblem


class MinPath(GraphProblem):

    def __init__(self, context):
        super().__init__(context)
        self.function = RoadCostFunction()
        self.context = context
        self.representation = self.make_representation()

    def get_edge_weight(self, node1, node2):
        return self.representation[node1][node2]['weight']

    def get_next_nodes(self, current_node):
        return list(self.representation.neighbors(current_node))

    def check_restrictions(self, solution):
        if solution[0] == self.df['initial'][0] and solution[-1] == self.df['final'][0]:
            return False
        return True

    def make_representation(self):
        self.df = pd.read_csv(StringIO(self.context), sep=';')
        self.df.columns = ['source', 'target', 'weight', 'initial', 'final', 'minimization']
        df_formatted = pd.DataFrame({
            'source': self.df['source'],
            'target': self.df['target'],
            'weight': self.df['weight'].astype(float)
        })
        return nx.from_pandas_edgelist(df_formatted, 'source', 'target', ['weight'])

    def get_random_point(self):
        return self.df['initial'][0].astype(int)

    def is_minimization(self):
        return True if self.df['minimization'][0] == 'yes' else False

    @staticmethod
    def get_description():
        return {
            "name": "Camino Mínimo",
            "description": "Consiste en determinar la distancia más corta que hay entre dos nodos de un grafo.",
            "algorithms": "SACO, MMAS",
            "class_name": "MinPath",
            "class_visualization": "GraphVisualization"
        }

    def get_restrictions(self):
        pass
