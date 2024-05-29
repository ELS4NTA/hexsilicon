import numpy as np
from matplotlib import pyplot as plt

from hexsilicon.presentation.visualization.problemvisualization import ProblemVisualization


class KnapsackVisualization(ProblemVisualization):

    def __init__(self):
        pass

    def draw(self, swarm, ax):
        # 1. Obtener datos del problema:
        df = swarm.problem.get_representation()

        # 3. Obtener las mejores soluciones:
        func = np.argmin if swarm.problem.is_minimization() else np.argmax
        k = func([agent.get_score() for agent in swarm.population])

        # 4. Filtrar los objetos seleccionados en cada solución:
        mejor_global_indices = [i for i, val in enumerate(swarm.best_agent.get_solution()) if val == 1]
        mejor_personal_indices = [i for i, val in enumerate(swarm.population[k].get_solution()) if val == 1]

        # Obtener los datos para graficar
        mejor_global_data = df.iloc[mejor_global_indices]
        mejor_personal_data = df.iloc[mejor_personal_indices]

        # Configurar los datos para graficar la barra apilada
        beneficio_total = [mejor_global_data['profit'].sum(), mejor_personal_data['profit'].sum()]
        peso_total = [mejor_global_data['weight'].sum(), mejor_personal_data['weight'].sum()]
        labels = ['Mejor Global', 'Mejor Personal']

        # Configurar los colores de cada objeto
        num_objetos = df.shape[0]
        colores = plt.cm.viridis(np.linspace(0, 1, num_objetos))

        ax.clear()

        # Graficar la barra apilada de beneficios
        bottom = np.zeros(2)
        for i in range(num_objetos):
            beneficios = df.iloc[i]['profit'] * np.array(
                [swarm.best_agent.get_solution()[i], swarm.population[k].get_solution()[i]])
            if beneficios.any():
                ax.bar(labels, beneficios, bottom=bottom, color=[colores[i], colores[i]], label=f'Objeto {i + 1}')
                for j, beneficio in enumerate(beneficios):
                    if beneficio != 0:
                        ax.text(j, bottom[j] + beneficio / 2, f'{beneficio}', ha='center', va='center',
                                color='white')
                bottom += beneficios

        # Mostrar el peso de cada barra encima de la misma
        for i, peso in enumerate(peso_total):
            ax.text(i, beneficio_total[i], f'Peso: {peso}', ha='center', va='bottom', color='black')

        # Configurar etiquetas y título
        ax.set_xlabel('Solución')
        ax.set_ylabel('Beneficio Total')
        ax.set_title('Barra Apilada de Beneficio Total y Peso Total')
        ax.legend(title='Objetos')

        # Mostrar la leyenda de los colores de cada ítem
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels, title='Objetos', bbox_to_anchor=(1.05, 1), loc='upper left')
