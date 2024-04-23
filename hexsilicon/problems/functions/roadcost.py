from hexsilicon.problems.functions.function import Function


class RoadCostFunction(Function):
    
    def __init__(self):
        pass

    def evaluate(self, solution, representation):
        cost = 0.0
        for i in range(len(solution.representation) - 1):
            cost += representation.get_edge_data(solution.representation[i], solution.representation[i + 1])['weight']
        return cost