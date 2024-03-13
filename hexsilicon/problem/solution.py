from .domain import Domain


class Solution(object):

    def __init__(self, domain: Domain, representation) -> None:
        self.domain = domain
        self.representation = representation
