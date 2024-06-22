from matplotlib import pyplot as plt
from hexsilicon.presentation.visualization.problemvisualization import ProblemVisualization

import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class MathematicalVisualization(ProblemVisualization):

    def __init__(self, fig):
        self.ax = fig.add_subplot(111, projection='3d')

    def draw(self, swarm):
        df = swarm.problem.get_representation()
        lower = df['lb'][0]
        upper = df['ub'][0]
        x = np.arange(lower, upper, 0.2)
        y = np.arange(lower, upper, 0.2)

        X, Y = np.meshgrid(x, y)
        Z = (X-1)**2 + (Y-1)**2

        # plot the best point
        solution = swarm.best_agent.get_solution()
        z_solution = (solution[0]-1)**2 + (solution[1]-1)**2

        self.ax.clear()
        self.ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.3)
        self.ax.scatter(solution[0], solution[1], z_solution, color='red')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('Función Matemática')
        self.ax.set_zlim(0, 10)
        self.ax.set_xlim(lower, upper)
        self.ax.set_ylim(lower, upper)



        
