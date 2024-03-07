from hexsilicon.swarm.naturalgroup import ant
from hexsilicon.problem import problem


class Hexsilicon(object):

    def __init__(self):
        self.example_problem()
        ant_swarm = ant.Ant()
        ant_swarm.generate_initial_swarm()

    def example_problem(self):
        ej_problem = problem.Problem()



if __name__ == "__main__":
    hexsilicon = Hexsilicon()
