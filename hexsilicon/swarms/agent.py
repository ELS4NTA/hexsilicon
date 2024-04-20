class Agent(object):

    def __init__(self, name=""):
        self.solution = None
        self.name = name

    def get_score(self):
        return self.solution.get_score()

    def get_solution(self):
        return self.solution
