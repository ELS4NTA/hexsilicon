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
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.show_btn = ttk.Button(
            self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

    def place_widgets(self):
        pass

    def toggle_frame(self):
        if self.canvas.get_tk_widget().winfo_ismapped():
            self.canvas.get_tk_widget().pack_forget()
            self.show_btn.config(text="Mostrar")
        else:
            self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
            self.show_btn.config(text="Ocultar")

    def update(self, swarm):
        print("Se dibuja el grafo :>")
        G = swarm.problem.get_representation()

        path = swarm.best_agent.get_solution()

        path_edges = list(zip(path, path[1:]))

        edge_colors = [
            "red" if edge in path_edges or tuple(
                reversed(edge)) in path_edges else "black"
            for edge in G.edges()
        ]

        pos = nx.spring_layout(G)

        fig = plt.figure(figsize=(6, 4), dpi=70)
        ax = fig.add_subplot(111)
        nx.draw_networkx_nodes(G, pos, ax=ax)
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, ax=ax)
        nx.draw_networkx_labels(G, pos, ax=ax)
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
        )

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
