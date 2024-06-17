from abc import abstractmethod
from hexsilicon.presentation.runner.observer import Observer
from hexsilicon.problems.free.freeproblem import FreeProblem
from hexsilicon.swarms.observable import Observable


class Swarm(Observable):
    """
    Represents a swarm of particles.

    The Swarm class is responsible for managing a swarm of particles in a metaheuristic algorithm.
    It provides methods for generating the swarm, executing the metaheuristic algorithm, and accessing
    information about the swarm's history, best agent, and hyperparameters.

    Attributes:
        hyperparams (dict): A dictionary of hyperparameters for the swarm.
        history (dict): A dictionary that stores the history of the swarm's best agent scores.
        description (str): A description of the swarm.
        behavior (Behavior): An instance of the Behavior class that defines the behavior of the swarm.
        problem (Problem): An instance of the Problem class that represents the problem being solved by the swarm.
        best_agent (Agent): The best agent found by the swarm.
        population (list): A list of agents in the swarm.
        observers (list): A list of observers that are notified when the swarm updates.
        current_iteration (int): The current iteration of the metaheuristic algorithm.
    """

    def __init__(self, behavior=None, problem=None):
        self.hyperparams = {
            'n_agents': {
                "name": "Agentes",
                "value": 10,
                "range": (1, 100),
                "description": "Cantidad de agentes en el enjambre"
            }
        }
        self.history = {}
        self.description = ""
        self.behavior = behavior(self)
        self.problem = problem
        self.best_agent = None
        self.population = []
        self.observers = []
        self.current_iteration = 0

    @abstractmethod
    def generate_swarm(self):
        """
        Generates a swarm of particles.
        
        This method generates a swarm of particles based on the specified parameters.
        It initializes the positions and velocities of the particles and assigns them to the swarm.
        """

    def metaheuristic(self):
        """
        Executes the metaheuristic algorithm for the swarm.

        This method performs the main steps of the metaheuristic algorithm for the swarm.
        It moves the swarm, updates the swarm, records the best agent's score in the history,
        and increments the current iteration. Finally, it notifies any observers of the swarm.
        """
        self.behavior.move_swarm(self)
        self.behavior.update_swarm(self)
        self.history[self.current_iteration] = self.best_agent.get_score()
        self.current_iteration += 1
        self.notify(self)

    @staticmethod
    @abstractmethod
    def get_description():
        """
        Returns the description of the swarm.
        """

    @abstractmethod
    def get_passed_points_agent(self, idx):
        """
        Returns the passed points of the agent at the specified index.

        Parameters:
            idx (int): The index of the agent.

        Returns:
            list: A list of passed points of the agent.
        """

    @abstractmethod
    def to_2d(self):
        """
        Converts the swarm to a 2D representation.

        This method transforms the swarm's coordinates from a 3D space to a 2D space.
        It updates the swarm's internal state to reflect the new 2D coordinates.

        Returns:
            list: A list of 2D coordinates for the swarm.
        """

    def has_free_problem(self):
        """
        Checks if the swarm has a free problem.

        Returns:
            bool: True if the swarm has a free problem, False otherwise.
        """
        return isinstance(self.problem, FreeProblem)

    def get_best_agent(self):
        """
        Returns the solution of the best agent in the swarm.

        Returns:
            The solution of the best agent.
        """
        return self.best_agent.get_solution()

    def get_hyperparams(self):
        """
        Returns the hyperparameters of the swarm.

        This method combines the hyperparameters of the swarm with the hyperparameters
        of the behavior and returns the combined hyperparameters.

        Returns:
            dict: A dictionary containing the combined hyperparameters.
        """
        return self.hyperparams | self.behavior.get_hyperparams()

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, swarm):
        for observer in self.observers:
            observer.update(swarm)

    def get_history(self):
        """
        Returns the history of the swarm.

        Returns:
            list: A list containing the history of the swarm.
        """
        return self.history
