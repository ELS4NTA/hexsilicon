import numpy as np

from hexsilicon.problems.solution import Solution
from hexsilicon.swarms.agent import Agent
from hexsilicon.swarms.swarm import Swarm


class Fireflies(Swarm):

    def __init__(self, behavior=None, problem=None):
        super().__init__(behavior, problem)
        self.history_pos = []

    def generate_swarm(self):
        n_agents = self.get_hyperparams()["n_agents"]["value"]
        for _ in range(n_agents):
            firefly = Agent("Firefly")
            firefly.solution = Solution(representation=np.array(self.problem.generate_solution()))
            firefly.set_score(self.problem.call_function(firefly.solution))
            self.history_pos.append(firefly.solution.get_representation())
            self.population.append(firefly)
        func = np.argmin if self.problem.is_minimization() else np.argmax
        self.best_agent = Agent("BestFirefly")
        self.best_agent.solution = Solution(representation=self.population[func(self.history_pos)].solution.get_representation())
        self.best_agent.set_score(self.problem.call_function(self.best_agent.solution))


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
            "name": "Nube de luciernagas",
            "description": "Grupo numeroso de insectos que, al emitir destellos de luz sincronizados, crean un espectáculo luminoso en la oscuridad.",
            "behavior": "FireflyBehavior",
            "class_name": "Fireflies"
        }