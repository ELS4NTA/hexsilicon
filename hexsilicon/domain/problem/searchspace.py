from abc import ABC


class SearchSpace(object):

    def __init__(self):
        self.domain = None
        self.restrictions = None
        self.solutions = []

    def get_domain(self):
        return self.domain

    def get_restrictions(self):
        return self.restrictions
