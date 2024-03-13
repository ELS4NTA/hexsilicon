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
        self.population = np.array([Agent() for _ in range(self.hyperparams['n_ants'])])

    def metaheuristic(self):
        data_frame = self.problem.domain.space
        # Inicializar feromonas
        data_frame['pheromone'] = self.hyperparams['pheromone_0']
        self.problem.representation = nx.from_pandas_edgelist(
            data_frame,
            'source',
            'target',
            ['weight', 'pheromone'],
            create_using=nx.Graph)

        # Inicializar el mejor camino
        best_path = None
        best_path_eval = np.inf

        # Por cada iteración
        for _ in range(self.hyperparams['n_iterations']):
            paths = []
            evals = []

            # Por cada hormiga
            for ant in self.population:
                current_point = self.problem.domain.restriction.get_restriction()['initial_point']
                path = np.array([current_point])
                path = self.movement_swarm(path, current_point)
                ant.solution = Solution(self.problem.domain, path)
                evals.append(self.problem.call_function(ant.solution))
                paths.append(path)

            # Actualizar el mejor camino
            if min(evals) < best_path_eval:
                best_path = paths[np.argmin(evals)]
                self.problem.solution = Solution(self.problem.domain, best_path)
                best_path_eval = min(evals)
                print('Best path:', best_path, 'with cost:', best_path_eval)

            # Actualizar feromonas
            self.update_swarm()
        return best_path

    @abstractmethod
    def update_swarm(self):
        pass

    @abstractmethod
    def movement_swarm(self, path, current_point):
        pass
