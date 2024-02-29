from hexsilicon.problem import solution


class Agent(object):

    def __init__(self, context: dict):
        self.context = context
        self.solution = None

    def get_solution(self):
        return self.solution
