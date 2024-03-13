from hexsilicon.problem.problem import Problem
from hexsilicon.problem.solution import Solution
from hexsilicon.swarm.agent import Agent
from hexsilicon.swarm.behavior import Behavior
from hexsilicon.swarm.swarm import Swarm
from abc import abstractmethod
import numpy as np
import networkx as nx


class AntGroup(Swarm, Behavior):

    def __init__(self, hyperparams: dict, problem: Problem):
        super().__init__(hyperparams, problem)
        self.population = None

    def generate_initial_swarm(self):
        self.population = np.array(Agent(), size=self.hyperparams['n_ants'])

    def metaheuristic(self):
        data_frame = self.problem.domain.space
        # Inicializar feromonas
        data_frame['pheromone'] = self.hyperparams['pheromone_0']
        self.problem.representation = nx.from_pandas_edgelist(
            data_frame,
            'source',
            'target',
            ['weight', 'pheromone'],
            create_using=nx.Graph if self.hyperparams['undirected'] else nx.DiGraph)

        # Inicializar el mejor camino
        best_path = None
        best_path_length = np.inf
        n_points = self.problem.get_representation().number_of_nodes()

        # Por cada iteración
        for _ in range(self.hyperparams['n_iterations']):
            paths = []

            # Por cada hormiga
            for _ in range(self.population):
                visited = np.zeros(n_points, dtype=bool)
                current_point = np.random.randint(n_points)
                visited[current_point] = True
                path = np.array([current_point])
                path = self.movement_swarm(visited, path, current_point)
                paths.append(path)

            # Por cada camino evaluarlo
            evals = []
            for path in paths:
                path_length = 0
                for i in range(n_points - 1):
                    path_length += self.distance(path[i], path[i + 1])
                path_length += self.distance(path[-1], path[0])
                evals.append(path_length)

            # Actualizar el mejor camino
            if min(evals) < best_path_length:
                best_path = paths[np.argmin(evals)]
                best_path_length = min(evals)

            # Actualizar feromonas
            self.update_swarm()

    def generate_initial_solution(self):
        path = np.random.randint(0, self.problem.domain.space["n_points"], size=self.problem.domain.space["n_points"], replace=False)
        solution = Solution(self.problem.domain, path)
        return solution
    
    def distance(self, point1, point2):
        return np.sqrt(np.sum((point1 - point2)**2))

    @abstractmethod
    def update_swarm(self):
        pass

    @abstractmethod
    def movement_swarm(self, visited, path, current_point):
        pass
