import networkx as nx

from hexsilicon.presentation.visualization.problemvisualization import ProblemVisualization


class GraphVisualization(ProblemVisualization):

    def __init__(self, fig):
        self.first_time = True
        self.pos = None
        self.ax = fig.add_subplot(111)

    def draw(self, swarm):
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
