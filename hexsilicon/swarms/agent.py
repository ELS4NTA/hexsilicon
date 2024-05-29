class Agent(object):

    def __init__(self, name=""):
        self.solution = None
        self.name = name

    def get_score(self):
        return self.solution.get_score()

    def set_score(self, score):
        if self.solution is not None:
            self.solution.set_score(score)
        else:
            raise ValueError("Agent does not have a solution yet.")

    def get_solution(self):
        return self.solution.get_representation()
