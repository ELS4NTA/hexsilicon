from abc import ABC, abstractmethod

from hexsilicon.presentation.runner.observer import Observer


class Observable(ABC):

    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, *args, **kwargs):
        pass
