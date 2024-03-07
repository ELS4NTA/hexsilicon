from .restriction import Restriction


class Domain(object):

    def __init__(self, space_search: dict,  restriction: Restriction) -> None:
        self.space = space_search
        self.restriction = restriction
