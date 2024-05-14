from io import StringIO

import pandas as pd
import numpy as np

from hexsilicon.problems.free.freeproblem import FreeProblem
from hexsilicon.problems.functions.knapsackFunction import KnapsackFunction


class Knapsack(FreeProblem):

    def __init__(self, context):
        super().__init__(context)
        self.function = KnapsackFunction()
        self.context = context
        self.representation = self.make_representation()

    def check_restrictions(self, solution):
        if self.function.evaluate(solution, self.representation) != 1E-5:
            return False
        return True

    def make_representation(self):
        df = pd.read_csv(StringIO(self.context), sep=';')
        df.columns = ['profit', 'weight', 'n', 'wmax', 'minimization']
        print(df)
        return df

    def is_minimization(self):
        return True if self.representation['minimization'][0] == 'yes' else False  # type: ignore
    
    def get_dimensions(self):
        return int(self.representation['n'][0])

    def generate_solution(self):
        return [0] * self.get_dimensions()

    def clip_velocity(self, temp_velocity):
        return np.round(temp_velocity).astype(int)

    @staticmethod
    def get_description():
        return {
            "name": "Problema de la Mochila",
            "description": "Consiste en determinar la mejor combinación de objetos que se pueden llevar en una mochila.",
            "algorithms": "PSO",
            "class_name": "Knapsack"
        }

    def get_restrictions(self):
        pass
