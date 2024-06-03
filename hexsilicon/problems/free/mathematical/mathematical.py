import random
from io import StringIO

import pandas as pd

from hexsilicon.problems.free.freeproblem import FreeProblem
from hexsilicon.problems.functions.polinomialFunction import PolinomialFunction



class Mathematical(FreeProblem):
    
    def __init__(self, context):
        super().__init__(context)
        self.function = PolinomialFunction()
        self.context = context
        self.representation = self.make_representation()
        self.binary = False
    
    def get_dimensions(self):
        return int(self.representation['n'][0])

    def generate_solution(self):
        domain_range = self.representation['range'][0]
        solution = [random.uniform(-domain_range, domain_range) for _ in range(self.get_dimensions())]
        return solution

    def clip_velocity(self, temp_velocity):
        return temp_velocity

    def is_binary(self):
        return self.binary

    def make_representation(self):
        df = pd.read_csv(StringIO(self.context), sep=';')
        df.columns = ['n', 'range', 'minimization']
        return df

    @staticmethod
    def get_description():
        return {
            "name": "Problema de Función Matemática",
            "description": "Consiste en determinar el valor mínimo de una función polinomial.",
            "algorithms": "PSO, FA",
            "class_name": "Mathematical",
            "class_visualization": "MathematicalVisualization"
        }

    def get_restrictions(self):
        pass

    def check_restrictions(self, solution):
        return True

    def is_minimization(self):
        return True if self.representation['minimization'][0] == 'yes' else False