from hexsilicon.problem.solution import Solution


class Agent(object):

    def __init__(self, initial_solution: Solution):
        self.solution = initial_solution
