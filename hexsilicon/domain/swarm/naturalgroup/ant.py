from hexsilicon.domain.problem.problem import Problem
from hexsilicon.domain.problem.solution import Solution
from hexsilicon.domain.swarm.agent import Agent
from hexsilicon.domain.swarm.behavior import Behavior
from hexsilicon.domain.swarm.swarm import Swarm
from abc import abstractmethod
import numpy as np
import networkx as nx


class AntGroup(Swarm, Behavior):

    def __init__(self, problem: Problem):
        super().__init__(problem)
        self.population = None
        self.hyperparams = {
            'rho': (0.01, 0.0, 0.2),
            'q': (1, 0, 10),
            'n_ants': (7, 1, 100),
            'pheromone_0': (1, -7, 50),
            'n_iterations': (20, 1, 1000)
        }

    def generate_initial_swarm(self):
        self.population = np.array([Agent() for _ in range(self.hyperparams['n_ants'][0])])

    def metaheuristic(self):
        data_frame = self.problem.domain.space
        # Inicializar feromonas
        data_frame['pheromone'] = self.hyperparams['pheromone_0'][0]
        print(data_frame)
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
        for i in range(self.hyperparams['n_iterations'][0]):
            paths = []
            evals = {}

            # Por cada hormiga
            for ant in self.population:
                current_point = self.problem.domain.restriction.get_restriction()['initial_point']
                path = np.array([current_point])
                path = self.movement_swarm(path, current_point)
                ant.solution = Solution(self.problem.domain, path)
                evals[i] = self.problem.call_function(ant.solution)
                paths.append(path)

            # Actualizar el mejor camino
            if min(list(evals.values())) < best_path_eval:
                best_path = paths[np.argmin(list(evals.values()))]
                self.problem.solution = Solution(self.problem.domain, best_path)
                best_path_eval = min(evals)
                print('Best path:', best_path, 'with cost:', best_path_eval)

            # Actualizar feromonas
            self.update_swarm()

            for observer in self.observers:
                if observer.__class__.__name__ == 'History':
                    observer.update(evals)
        return best_path

    @abstractmethod
    def update_swarm(self):
        pass

    @abstractmethod
    def movement_swarm(self, path, current_point):
        pass
