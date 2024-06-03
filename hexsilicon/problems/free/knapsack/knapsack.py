import random
from io import StringIO

import numpy as np
import pandas as pd

from hexsilicon.problems.free.freeproblem import FreeProblem
from hexsilicon.problems.functions.knapsackFunction import KnapsackFunction


class Knapsack(FreeProblem):

    def __init__(self, context):
        super().__init__(context)
        self.function = KnapsackFunction()
        self.context = context
        self.binary = True
        self.representation = self.make_representation()

    def check_restrictions(self, solution):
        if self.function.evaluate(solution, self.representation) == 1E-5:
            return False
        return True

    def make_representation(self):
        df = pd.read_csv(StringIO(self.context), sep=';')
        df.columns = ['profit', 'weight', 'n', 'wmax', 'minimization']
        return df

    def is_minimization(self):
        return True if self.representation['minimization'][0] == 'yes' else False  # type: ignore

    def get_dimensions(self):
        return int(self.representation['n'][0])

    def generate_solution(self):
        solution = [1] * self.get_dimensions()
        while not self.check_restrictions(solution):
            solution = [random.randint(0, 1) for _ in range(self.get_dimensions())]
        return solution

    def clip_velocity(self, temp_velocity):
        sigmoid_velocity = 1 / (1 + np.exp(-temp_velocity))
        return sigmoid_velocity

    def is_binary(self):
        return self.binary

    @staticmethod
    def get_description():
        return {
            "name": "Problema de la Mochila",
            "description": "Consiste en determinar la mejor combinación de objetos que se pueden llevar en una mochila.",
            "algorithms": "PSO, FA",
            "class_name": "Knapsack",
            "class_visualization": "KnapsackVisualization"
        }

    def get_restrictions(self):
        pass
