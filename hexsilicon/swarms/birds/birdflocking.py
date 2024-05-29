from hexsilicon.problems.solution import Solution
from hexsilicon.swarms.agent import Agent
from hexsilicon.swarms.swarm import Swarm

import numpy as np


class BirdFlocking(Swarm):

    def __init__(self, behavior=None, problem=None):
        super().__init__(behavior, problem)
        self.velocities = None
        self.pbest = []
        self.pcost = []
        self.history_pos = []

    def generate_swarm(self):
        rng = np.random.default_rng(seed=42)
        n_agents = self.get_hyperparams()["n_agents"]["value"]
        dimensions = self.problem.get_dimensions()
        max_velocity = self.get_hyperparams()["v_max"]["value"]
        min_velocity = self.get_hyperparams()["v_min"]["value"]
        self.velocities = rng.uniform(low=min_velocity, high=max_velocity, size=(n_agents, dimensions))

        for _ in range(n_agents):
            bird = Agent("Bird")
            bird.solution = Solution(representation=self.problem.generate_solution())
            score = self.problem.call_function(bird.solution)
            bird.set_score(score)
            self.pbest.append(bird.solution.get_representation())
            self.history_pos.append(bird.solution.get_representation())
            self.pcost.append(score)
            self.population.append(bird)

        func = np.argmin if self.problem.is_minimization() else np.argmax
        self.best_agent = Agent("BestBird")
        self.best_agent.solution = Solution(representation=self.pbest[func(self.pcost)])
        self.best_agent.set_score(self.pcost[func(self.pcost)])

    def metaheuristic(self):
        num_iterations = self.behavior.get_hyperparams()["n_iterations"]["value"]
        for i in range(num_iterations):
            self.behavior.move_swarm(self)
            self.behavior.update_swarm(self)
            self.history[i] = self.best_agent.get_score()
            self.notify(self)

    def get_passed_points_agent(self, idx):
        return self.history_pos[idx] + self.population[idx].solution.get_representation()

    def to_2d(self):
        return [agent.solution.get_representation() for agent in self.population]

    @staticmethod
    def get_description():
        return {
            "name": "Bandada de Aves",
            "description": "Este algoritmo se basa en el comportamiento de las aves en bandadas.",
            "behavior": "ParticleBehavior",
            "class_name": "BirdFlocking"
        }
