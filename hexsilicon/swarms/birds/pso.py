import numpy as np

from hexsilicon.swarms.birds.particlebehavior import ParticleBehavior


class PSO(ParticleBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)

    def move_swarm(self, swarm):
        rng = np.random.default_rng()
        c1 = self.get_hyperparams()["c1"]["value"]
        c2 = self.get_hyperparams()["c2"]["value"]
        w = self.get_hyperparams()["w"]["value"]
        for i, agent in enumerate(swarm.population):
            r1, r2 = rng.uniform(), rng.uniform()
            # Calculate the cognitive and social components of velocity using list comprehensions
            cognitive = [c1 * r1 * (pb - x) for pb, x in zip(swarm.pbest[i], agent.get_solution())]
            social = [c2 * r2 * (gb - x) for gb, x in zip(swarm.best_agent.get_solution(), agent.get_solution())]
            temp_velocity = (w * swarm.velocities[i]) + np.array(cognitive) + np.array(social)
            updated_velocity = swarm.problem.clip_velocity(temp_velocity)  # Clip velocity
            swarm.velocities[i] = updated_velocity
            # Update position
            if swarm.problem.is_binary():
                agent.solution.representation = swarm.velocities[i]
            else:
                agent.solution.representation += swarm.velocities[i]
            agent.set_score(swarm.problem.call_function(agent.solution))

    def update_swarm(self, swarm):
        for i, agent in enumerate(swarm.population):
            is_min = swarm.problem.is_minimization()
            better = agent.get_score() < swarm.pcost[i] if is_min else agent.get_score() > swarm.pcost[i]
            if better:
                swarm.pbest[i] = agent.solution.get_representation()
                swarm.pcost[i] = agent.get_score()
                better_gb = agent.get_score() < swarm.best_agent.get_score() if is_min else agent.get_score() > swarm.best_agent.get_score()
                if better_gb:
                    swarm.best_agent.solution = agent.solution

    @staticmethod
    def get_description():
        return {
            "name": "PSO",
            "description": "El algoritmo de optimización por enjambre de partículas (PSO) es un método de "
                           "optimización basado en la población. Cada partícula representa una solución candidata en "
                           "el espacio de búsqueda. Las partículas se mueven a través del espacio de búsqueda "
                           "siguiendo la mejor partícula y la mejor partícula global. PSO es un algoritmo de "
                           "optimización global que no requiere derivadas y es fácil de implementar.",
            "class_name": "PSO"
        }
