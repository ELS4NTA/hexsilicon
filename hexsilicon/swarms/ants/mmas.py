from hexsilicon.swarms.ants.antbehavior import AntBehavior


# Max-Min Ant System (MMAS) algorithm
class MMAS(AntBehavior):

    def __init__(self, swarm=None):
        super().__init__(swarm)
        self.hyperparams = self.hyperparams | {
            'pheromone_0': (1, 0, 1),
            'rho': (0.01, 0.0, 0.2),
            'alpha': (1, 0, 10),
            'beta': (1, 0, 10),
        }

    def move_swarm(self, swarm):
        pass

    def move_swarm(self, swarm):
        # por cada hormiga
        # preguntar el punto inicial al problema por restricicones... (eso lo hace el problema)
        # validar restricciones para construir camino, si puedo seguir, agregar nodo al camino

        # agrego la soluciona a la hormiga
        # evaluo solo los caminos que cumplen con las restricciones, los que no cumplen se les asigna un valor alto o bajo

        # se le pregunta al problema que optimizacion se hace min o max luego actualizo la mejor solucion
        pass

    def update_swarm(self, swarm):
        graph = swarm.problem.get_representation()
        # only the best is updated
        new_ph = 0
        ph_max = 1
        ph_min = 0
        net = None
        i = None
        if new_ph > ph_max:
            net[i[0]][i[1]]['pheromone'] = ph_max
        elif new_ph < ph_min:
            net[i[0]][i[1]]['pheromone'] = ph_min
        else:
            net[i[0]][i[1]]['pheromone'] = new_ph

        for edge in graph.edges(data=True):
            edge[2]['pheromone'] *= (1 - self.hyperparams['rho'][0])
            edge[2]['pheromone'] += self.hyperparams['q'][0]

    def get_hyperparams(self):
        return self.hyperparams

    def get_hyperparams_description(self):
        return {
            'n_iterations': 'N\u00famero de iteraciones',
            'n_agents': 'N\u00famero de hormigas',
            'pheromone_0': 'Feromona inicial',
            'rho': 'Tasa de evaporación de feromonas',
            'q': 'Cantidad de feromonas depositadas por la hormiga',
            'alpha': 'Peso de la feromona',
            'beta': 'Peso de la distancia'
        }

    @staticmethod
    def get_description():
        return {
            "name": "MMAS",
            "description": "El algoritmo Max-Min Ant System es una mejora del ACO que garantiza la convergencia del algoritmo.",
            "class_name": "MMAS"
        }
