from hexsilicon.swarms.birds.particlebehavior import ParticleBehavior
import numpy as np


class PSO(ParticleBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.set_hyperparams()

    def move_swarm(self, swarm):
        rng = np.random.default_rng(seed=42)
        c1 = self.get_hyperparams()["c1"]["value"]
        c2 = self.get_hyperparams()["c2"]["value"]
        w = self.get_hyperparams()["w"]["value"]
        for i, agent in enumerate(swarm.population):
            cognitive = [c1 * rng.uniform() * (swarm_pbest - agent_representation) for swarm_pbest, agent_representation
                         in zip(swarm.pbest[i], agent.solution.representation)]

            # cognitive = c1 * rng.uniform() * (swarm.pbest[i] - agent.solution.representation)
            # social = c2 * rng.uniform() * (swarm.best_agent.solution.representation - agent.solution.representation)
            social = [c2 * rng.uniform() * (swarm_best - agent_representation) for swarm_best, agent_representation in
                      zip(swarm.best_agent.solution.representation, agent.solution.representation)]
            temp_velocity = (w * swarm.velocities[i]) + cognitive + social
            updated_velocity = swarm.problem.clip_velocity(temp_velocity)  # Clip velocity
            swarm.velocities[i] = updated_velocity

    def update_swarm(self, swarm):
        for i, agent in enumerate(swarm.population):
            swarm.history_pos[i] = agent.solution.representation
            agent.solution.representation += swarm.velocities[i]
            agent.set_score(swarm.problem.call_function(agent.solution))
            if swarm.problem.is_minimization():
                if agent.get_score() < swarm.pcost[i]:
                    swarm.pbest[i] = agent.solution
                    swarm.pcost[i] = agent.get_score()
                    if agent.get_score() < swarm.best_agent.get_score():
                        swarm.best_agent = agent
            else:
                if agent.get_score() > swarm.pcost[i]:
                    swarm.pbest[i] = agent.solution
                    swarm.pcost[i] = agent.get_score()
                    if agent.get_score() > swarm.best_agent.get_score():
                        swarm.best_agent = agent

    def get_hyperparams(self):
        return self.hyperparams

    def set_hyperparams(self):
        self.hyperparams = self.hyperparams | {
            "v_min": {
                "name": "Velocidad Minima",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Define la velocidad mínima de las partículas"
            },
            "v_max": {
                "name": "Velocidad Maxima",
                "value": 1.0,
                "range": (0.0, 1.0),
                "description": "Define la velocidad máxima de las partículas"
            },
            "w": {
                "name": "Constante Inercia",
                "value": 1.0,
                "range": (0.0, 5.0),
                "description": "Reduce o aumenta la velocidad de la particula"
            },
            "c1": {
                "name": "Constante Individual",
                "value": 2.05,
                "range": (0.0, 5.0),
                "description": "Influencia de la mejor posición individual"
            },
            "c2": {
                "name": "Constante Social",
                "value": 2.05,
                "range": (0.0, 5.0),
                "description": "Influencia de la mejor posición global"
            },
        }

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
