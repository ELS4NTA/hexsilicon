from abc import ABC, abstractmethod


class Domain(ABC):

    @abstractmethod
    def get_domain(self):
        pass
