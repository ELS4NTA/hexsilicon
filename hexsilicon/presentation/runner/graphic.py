import matplotlib.pyplot as plt
import networkx as nx
import ttkbootstrap as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer


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
        pass
        # G = swarm.problem.get_representation()
        #
        # path = swarm.best_agent.get_solution()
        #
        # path_edges = list(zip(path, path[1:]))
        #
        # edge_colors = [
        #     "red" if edge in path_edges or tuple(
        #         reversed(edge)) in path_edges else "black"
        #     for edge in G.edges()
        # ]
        # if self.first_time:
        #     self.first_time = False
        #     self.pos = nx.spring_layout(G)
        #
        # # Limpiar el gráfico existente
        # self.ax.clear()
        #
        # # Dibujar el gráfico
        # nx.draw_networkx_nodes(G, self.pos, ax=self.ax)
        # nx.draw_networkx_edges(G, self.pos, edge_color=edge_colors, ax=self.ax)
        # nx.draw_networkx_labels(G, self.pos, ax=self.ax)
        # nx.draw_networkx_edge_labels(
        #     G, self.pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}, ax=self.ax
        # )
        #
        # # Redibujar el canvas
        # if self.will_update:
        #     self.canvas.draw()
