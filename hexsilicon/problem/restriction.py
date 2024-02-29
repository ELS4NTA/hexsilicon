from abc import ABC, abstractmethod


class Restriction(object, ABC):

    @abstractmethod
    def __init__(self):
        pass
