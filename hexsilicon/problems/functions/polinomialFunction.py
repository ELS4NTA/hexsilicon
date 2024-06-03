from hexsilicon.problems.functions.function import Function


class PolinomialFunction(Function):
    
    def __init__(self):
        pass
    
    def evaluate(self, solution, representation):
        return sum((x-1)**2 for x in solution)   
        
        