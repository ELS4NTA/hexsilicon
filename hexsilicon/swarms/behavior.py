from abc import ABC, abstractmethod


class Behavior(ABC):
    """
    Abstract base class for defining swarm behaviors.
    """

    @abstractmethod
    def set_hyperparams(self):
        """
        Set the hyperparameters for the behavior.
        """

    @abstractmethod
    def move_swarm(self, swarm):
        """
        Move the swarm based on the defined behavior.

        Parameters:
        - swarm: The swarm object to be moved.
        """

    @abstractmethod
    def update_swarm(self, swarm):
        """
        Update the swarm based on the defined behavior.

        Parameters:
        - swarm: The swarm object to be updated.
        """

    @abstractmethod
    def get_hyperparams(self):
        """
        Get the hyperparameters for the behavior.

        Returns:
        - The hyperparameters for the behavior.
        """

    @staticmethod
    @abstractmethod
    def get_description():
        """
        Get the description of the behavior.

        Returns:
        - The description of the behavior.
        """
