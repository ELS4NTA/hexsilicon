from hexsilicon.problems.function import Function


class MinPathFunction(Function):

    def __init__(self):
        pass

    def evaluate(self):
        cost = 0.0
        for i in range(solution.representation.size - 1):
            cost += representation.get_edge_data(solution.representation[i], solution.representation[i + 1])['weight']
        return cost
