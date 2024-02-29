from hexsilicon.swarm.population.ant import Ant
from hexsilicon.swarm.population.ant import ant_algorithm
from hexsilicon.swarm.agent import Agent


@ant_algorithm
class ACO(Ant):

    def __init__(self):
        super().__init__()
        self.population = self.generate_initial_swarm()

    def generate_initial_swarm(self) -> list[Agent]:
        population = []
        for _ in range(self.hyperparams.get("n_ants")):
            agent = Agent()
            population.append(agent)
        return population

    def movement_swarm(self):
        pass

    def update_swarm(self):
        pass

