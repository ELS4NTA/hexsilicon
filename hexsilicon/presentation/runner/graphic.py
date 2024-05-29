import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import ttkbootstrap as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer
from hexsilicon.problems.graph.graphproblem import GraphProblem


class Graphic(Observer, ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.will_update = True
        self.first_time = True
        self.pos = None
        self.create_widgets()

    def create_widgets(self):
        self.show_btn = ttk.Button(self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

        # Inicializar la figura y el canvas
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=70)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)

    def toggle_frame(self):
        if self.canvas.get_tk_widget().winfo_ismapped():
            self.canvas.get_tk_widget().pack_forget()
            self.will_update = False
            self.show_btn.config(text="Mostrar")
        else:
            self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
            self.will_update = True
            self.show_btn.config(text="Ocultar")

    def update(self, swarm):
        if self.will_update:
            if isinstance(swarm.problem, GraphProblem):
                self.draw_graph_problem(swarm)
            else:
                self.draw_free_problem(swarm)

    def draw_graph_problem(self, swarm):
        G = swarm.problem.get_representation()
        
        path = swarm.best_agent.get_solution()
        
        path_edges = list(zip(path, path[1:]))
        
        edge_colors = [
            "red" if edge in path_edges or tuple(
                reversed(edge)) in path_edges else "black"
            for edge in G.edges()
        ]
        if self.first_time:
            self.first_time = False
            self.pos = nx.spring_layout(G)
        
        # Limpiar el gráfico existente
        self.ax.clear()
        
        # Dibujar el gráfico
        nx.draw_networkx_nodes(G, self.pos, ax=self.ax)
        nx.draw_networkx_edges(G, self.pos, edge_color=edge_colors, ax=self.ax)
        nx.draw_networkx_labels(G, self.pos, ax=self.ax)
        nx.draw_networkx_edge_labels(
            G, self.pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}, ax=self.ax
        )
        
        # Redibujar el canvas
        if self.will_update:
            self.canvas.draw()

    def draw_free_problem(self, swarm):
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

        self.ax.clear()

        # Graficar la barra apilada de beneficios
        bottom = np.zeros(2)
        for i in range(num_objetos):
            beneficios = df.iloc[i]['profit'] * np.array([swarm.best_agent.get_solution()[i], swarm.population[k].get_solution()[i]])
            if beneficios.any():
                self.ax.bar(labels, beneficios, bottom=bottom, color=[colores[i], colores[i]], label=f'Objeto {i + 1}')
                for j, beneficio in enumerate(beneficios):
                    if beneficio != 0:
                        self.ax.text(j, bottom[j] + beneficio / 2, f'{beneficio}', ha='center', va='center', color='white')
                bottom += beneficios

        # Mostrar el peso de cada barra encima de la misma
        for i, peso in enumerate(peso_total):
            self.ax.text(i, beneficio_total[i], f'Peso: {peso}', ha='center', va='bottom', color='black')

        # Configurar etiquetas y título
        self.ax.set_xlabel('Solución')
        self.ax.set_ylabel('Beneficio Total')
        self.ax.set_title('Barra Apilada de Beneficio Total y Peso Total')
        self.ax.legend(title='Objetos')

        # Mostrar la leyenda de los colores de cada ítem
        handles, labels = self.ax.get_legend_handles_labels()
        self.ax.legend(handles, labels, title='Objetos', bbox_to_anchor=(1.05, 1), loc='upper left')

        # 7. Actualizar el gráfico:
        self.canvas.draw()
