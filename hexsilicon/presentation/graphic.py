import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx


class Graphic(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.show_btn = ttk.Button(self, text="Not show", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()
        self.example_problem_plot()

    def place_widgets(self):
        pass

    def example_problem_plot(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

        for u, v in G.edges():
            G[u][v]['weight'] = 1

        path = [1, 2, 3, 4, 5]  # Ruta de ejemplo

        path_edges = list(zip(path, path[1:]))

        edge_colors = [
            "red" if edge in path_edges or tuple(reversed(edge)) in path_edges else "black"
            for edge in G.edges()
        ]

        pos = nx.spring_layout(G)

        fig = plt.figure(figsize=(6, 4), dpi=70)
        ax = fig.add_subplot(111)
        nx.draw_networkx_nodes(G, pos, ax=ax)
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, ax=ax)
        nx.draw_networkx_labels(G, pos, ax=ax)

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)

    def toggle_frame(self):
        if self.canvas.get_tk_widget().winfo_ismapped():
            self.canvas.get_tk_widget().pack_forget()
            self.show_btn.config(text="Show")
        else:
            self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
            self.show_btn.config(text="Not show")