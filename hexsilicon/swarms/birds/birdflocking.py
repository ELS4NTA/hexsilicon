from hexsilicon.swarms.swarm import Swarm


class BirdFlocking(Swarm):

    def __init__(self):
        pass

    def generate_swarm(self):
        pass

    def metaheuristic(self):
        pass

    def get_best_solution(self):
        pass

    @staticmethod
    def get_description():
        return {
            "name": "Bandada de Aves",
            "description": "Este algoritmo se basa en el comportamiento de las aves en bandadas.",
            "behavior": "BirdBehavior",
            "class_name": "BirdFlocking"
        }
