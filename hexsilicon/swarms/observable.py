from abc import ABC, abstractmethod
from hexsilicon.presentation.runner.observer import Observer


class Observable(ABC):
    """
    Abstract base class for observables.

    Observables are objects that can be observed by one or more observers.
    Subclasses of `Observable` must implement the `subscribe`, `unsubscribe`,
    and `notify` methods.
    """

    @abstractmethod
    def subscribe(self, observer: Observer):
        """
        Subscribe an observer to this observable.

        Args:
            observer (Observer): The observer to subscribe.
        """

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        """
        Unsubscribe an observer from this observable.

        Args:
            observer (Observer): The observer to unsubscribe.
        """

    @abstractmethod
    def notify(self, swarm):
        """
        Notify all subscribed observers about a change in the observable.

        Args:
            swarm: The swarm object to notify the observers about.
        """
