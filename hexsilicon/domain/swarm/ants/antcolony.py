import networkx as nx
import numpy as np

from hexsilicon.domain.problem.problem import Problem
from hexsilicon.domain.problem.solution import Solution
from hexsilicon.domain.swarm.agent import Agent
from hexsilicon.domain.swarm.swarm import Swarm


class AntColony(Swarm):

    def __init__(self):
        super().__init__()

    def generate_swarm(self):
        self.population = np.array(
            [Agent("Ant") for _ in range(self.behavior.get_hyperparams["n_agents"][0])]
        )

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
                current_point = self.problem.domain.restriction.get_restriction()[
                    'initial_point']
                path = np.array([current_point])
                path = self.movement_swarm(path, current_point)
                ant.solution = Solution(self.problem.domain, path)
                evals[i] = self.problem.call_function(ant.solution)
                paths.append(path)

            # Actualizar el mejor camino
            if min(list(evals.values())) < best_path_eval:
                best_path = paths[np.argmin(list(evals.values()))]
                self.problem.solution = Solution(
                    self.problem.domain, best_path)
                best_path_eval = min(evals)
                print('Best path:', best_path, 'with cost:', best_path_eval)

            # Actualizar feromonas
            self.update_swarm()

            for observer in self.observers:
                if observer.__class__.__name__ == 'History':
                    observer.update(evals)
        return best_path

    def get_best_solution(self):
        pass

    def get_description(self):
        pass
