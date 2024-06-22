import numpy as np
from matplotlib import pyplot as plt

from hexsilicon.presentation.visualization.problemvisualization import ProblemVisualization


class KnapsackVisualization(ProblemVisualization):

    def __init__(self, fig):
        self.ax = fig.add_subplot(111)

    def draw(self, swarm):
        # 1. Get problem data:
        df = swarm.problem.get_representation()

        # 3. Get the best solutions:
        func = np.argmin if swarm.problem.is_minimization() else np.argmax
        k = func([agent.get_score() for agent in swarm.population])

        # 4. Filter the selected objects in each solution:
        global_best_indices = [i for i, val in enumerate(swarm.best_agent.get_solution()) if val == 1]
        personal_best_indices = [i for i, val in enumerate(swarm.population[k].get_solution()) if val == 1]

        # Get the data to plot
        global_best_data = df.iloc[global_best_indices]
        personal_best_data = df.iloc[personal_best_indices]

        # Set up the data to plot the stacked bar
        total_profit = [global_best_data['profit'].sum(), personal_best_data['profit'].sum()]
        total_weight = [global_best_data['weight'].sum(), personal_best_data['weight'].sum()]
        labels = ['Global Best', 'Personal Best']

        # Set up the colors of each object
        num_objects = df.shape[0]
        colors = plt.cm.viridis(np.linspace(0, 1, num_objects))

        self.ax.clear()

        # Plot the stacked bar of profits
        bottom = np.zeros(2)
        for i in range(num_objects):
            profits = df.iloc[i]['profit'] * np.array(
                [swarm.best_agent.get_solution()[i], swarm.population[k].get_solution()[i]])
            if profits.any():
                self.ax.bar(labels, profits, bottom=bottom, color=[colors[i], colors[i]], label=f'Object {i + 1}')
                for j, profit in enumerate(profits):
                    if profit != 0:
                        self.ax.text(j, bottom[j] + profit / 2, f'{profit}', ha='center', va='center',
                                color='white')
                bottom += profits

        # Show the weight of each bar on top of it
        for i, weight in enumerate(total_weight):
            self.ax.text(i, total_profit[i], f'Weight: {weight}', ha='center', va='bottom', color='black')

        # Set up labels and title
        self.ax.set_xlabel('Soluciones')
        self.ax.set_ylabel('Beneficio total')
        self.ax.set_title('Beneficio y peso total de las soluciones')
        self.ax.legend(title='Objetos')

        # Show the legend of the colors of each item
        handles, labels = self.ax.get_legend_handles_labels()
        self.ax.legend(handles, labels, title='Objetos', bbox_to_anchor=(1.05, 1), loc='upper left')
