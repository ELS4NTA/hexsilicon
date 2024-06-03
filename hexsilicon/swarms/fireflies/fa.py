import numpy as np

from hexsilicon.swarms.fireflies.fireflybehavior import FireflyBehavior


# Firefly Algorithm (FA)
class FA(FireflyBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.alpha = self.hyperparams["alpha"]["value"]
        self.rng = np.random.default_rng()

    def move_swarm(self, swarm):
        self.alpha *= self.hyperparams["theta"]["value"]
        beta = self.hyperparams["beta"]["value"]
        gamma = self.hyperparams["gamma"]["value"]
        for firefly_i in swarm.population:
            for firefly_j in swarm.population:
                if firefly_i.get_score() < firefly_j.get_score():
                    # Compute the distance between the fireflies
                    r_distance = np.sum(np.square(firefly_i.get_solution() - firefly_i.get_solution()), axis=-1)
                    # Compute the attractiveness
                    attractiveness = beta * np.exp(-gamma * r_distance)
                    # Generate a random vector and compute the step
                    epsilon = self.rng.standard_normal(size=firefly_i.get_solution().shape)
                    steps = self.alpha * epsilon
                    # Move the firefly
                    temp_move = firefly_i.get_solution() + attractiveness * (firefly_j.get_solution() - firefly_i.get_solution()) + steps
                    sigmoid = swarm.problem.clip_velocity(temp_move)
                    updated_move = np.where(self.rng.uniform(size=sigmoid.shape) < sigmoid, 1, 0)
                    firefly_i.solution.representation = updated_move
                    firefly_i.set_score(swarm.problem.call_function(firefly_i.solution))

    def update_swarm(self, swarm):
        is_min = swarm.problem.is_minimization()
        func = min if is_min else max
        best_firefly = func(swarm.population, key=lambda agent: agent.get_score())
        if swarm.best_agent.solution is None:
            swarm.best_agent.solution = best_firefly.solution
        update_best = best_firefly.get_score() < swarm.best_agent.get_score() if is_min else best_firefly.get_score() > swarm.best_agent.get_score()

        # Update global best if the current best firefly is better
        if update_best:
            swarm.best_agent.solution = best_firefly.solution

    @staticmethod
    def get_description():
        return {
            "name": "FA",
            "description": "Inspira en el comportamiento de las luciérnagas y su capacidad para atraerse mutuamente mediante destellos de luz.",
            "class_name": "FA"
        }
