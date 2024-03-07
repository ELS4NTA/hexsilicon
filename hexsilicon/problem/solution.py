from .domain import Domain


class Solution(object):

    def __init__(self, domain: Domain, respresentation) -> None:
        self.domain = domain
        self.representation = respresentation
