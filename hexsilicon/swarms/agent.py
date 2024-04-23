class Agent(object):

    def __init__(self, name=""):
        self.solution = None
        self.name = name

    def get_score(self):
        return self.solution.get_score()
    
    def set_score(self, score):
        self.solution.set_score(score)

    def get_solution(self):
        return self.solution.get_representation()
