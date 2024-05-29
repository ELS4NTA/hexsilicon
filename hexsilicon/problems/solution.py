class Solution(object):

    def __init__(self, representation=None):
        self.searchspace = None
        self.score = None
        self.representation = representation

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def get_representation(self):
        return self.representation
