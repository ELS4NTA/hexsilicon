from abc import abstractmethod
import numpy as np
from hexsilicon.problems.solution import Solution
from hexsilicon.swarms.behavior import Behavior


class AntBehavior(Behavior):
    """
    Represents the behavior of an ant within a swarm.

    The `AntBehavior` class defines the behavior of an ant within a swarm.
    It contains methods for moving the ant within the swarm, updating the swarm,
    and retrieving the hyperparameters and initial pheromone value for the behavior.

    Attributes:
        hyperparams (dict): A dictionary containing the hyperparameters for the ant behavior.
        swarm (Swarm): The swarm object associated with the behavior.
        rng (numpy.random.Generator): The random number generator used for making random choices.
    """

    def __init__(self, swarm=None):
        self.hyperparams = {
            'n_iterations': {
                "name": "Iterations",
                "value": 50,
                "range": (1, 1000),
                "description": "Cantidad de iteraciones en el enjambre"
            },
        }
        self.swarm = swarm
        self.set_hyperparams()
        self.rng = np.random.default_rng()

    def set_hyperparams(self):
        self.hyperparams.update({
            "pheromone_0": {
                "name": "Initial Pheromone",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Feromona inicial en las aristas"
            },
            "rho": {
                "name": "Rho",
                "value": 0.01,
                "range": (0.0, 0.2),
                "description": "Tasa de evaporacion de feromona"
            },
            "alpha": {
                "name": "Alpha",
                "value": 1.0,
                "range": (0.0, 10.0),
                "description": "Valor de importancia de feromona"
            },
            "beta": {
                "name": "Beta",
                "value": 1.0,
                "range": (0.0, 10.0),
                "description": "Valor de importancia de heuristica del problema"
            },
        })

    def move_swarm(self, swarm):
        for ant in swarm.population:
            path = self.move_ant(swarm)
            ant.solution = Solution(representation=path)
            ant.set_score(swarm.problem.call_function(ant.solution))

    def move_ant(self, swarm):
        """
        Move the ant within the swarm.

        Parameters:
        - swarm: The swarm object.

        Returns:
        - path: The path taken by the ant.

        This method moves the ant within the swarm by selecting the next node based on pheromone levels and edge weights.
        It continues moving until it reaches a node that violates the problem's restrictions or there are no more available nodes to move to.
        The method returns the path taken by the ant.
        """
        alpha = self.hyperparams["alpha"]["value"]
        beta = self.hyperparams["beta"]["value"]
        while True:
            current_node = swarm.problem.get_random_point()
            path = [current_node]
            is_good_path = True
            while swarm.problem.check_restrictions(path) and is_good_path:
                next_nodes = swarm.problem.get_next_nodes(current_node)
                next_nodes = [node for node in next_nodes if node not in path]
                if not next_nodes:
                    is_good_path = False
                    break
                probabilities = np.zeros(len(next_nodes))
                for i, next_node in enumerate(next_nodes):
                    pheromone = swarm.get_edge_pheromone(current_node, next_node)
                    weight = swarm.problem.get_edge_weight(current_node, next_node)
                    probabilities[i] = (pheromone ** alpha) * ((1 / weight) ** beta)
                probabilities /= probabilities.sum()
                next_node = self.rng.choice(next_nodes, p=probabilities)
                path.append(next_node)
                current_node = next_node
            if is_good_path:
                return path

    def get_hyperparams(self):
        return self.hyperparams

    @abstractmethod
    def update_swarm(self, swarm):
        pass

    @abstractmethod
    def get_pheromone_initial(self):
        """
        Returns the initial pheromone value for the ant behavior.

        This method retrieves the initial pheromone value that is used by the ant behavior.
        The pheromone value represents the strength or intensity of the chemical signal
        left by the ants to communicate with each other.

        Returns:
            float: The initial pheromone value for the ant behavior.
        """

    @staticmethod
    @abstractmethod
    def get_description():
        pass
