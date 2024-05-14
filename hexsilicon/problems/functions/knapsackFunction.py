from hexsilicon.problems.functions.function import Function


class KnapsackFunction(Function):

    def __init__(self):
        pass

    def evaluate(self, solution, representation):
        total_profit = 0.0
        total_weight = 0.0
        w_max = representation['wmax'][0]
        
        for i in range(len(solution)):
            if solution[i] == 1:
                total_profit += representation['profit'][i]
                total_weight += representation['weight'][i]
        
        if total_weight > w_max:
            cost = 1E-5
        else:
            cost = total_profit
        return cost
