from restriction import Restriction


class Domain(object):

    def __init__(self, restriction: Restriction) -> None:
        self.restriction = restriction
