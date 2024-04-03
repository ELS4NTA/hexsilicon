from abc import ABC, abstractmethod
from hexsilicon.presentation.observer import Observer


class Observable(ABC):

    def __init__(self):
        self.observers = []

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        list(map(lambda observer: observer.update(*args, **kwargs), self.observers))
