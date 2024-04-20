from hexsilicon.swarms.birds.birdbehavior import BirdBehavior


class PSO(BirdBehavior):

    def get_hyperparams(self):
        pass

    def get_hyperparams_description(self):
        pass

    def move_swarm(self):
        pass

    def update_swarm(self):
        pass

    @staticmethod
    def get_description():
        return {
            "name": "PSO",
            "description": "El algoritmo de optimización por enjambre de partículas (PSO) es un método de "
                           "optimización basado en la población. Cada partícula representa una solución candidata en "
                           "el espacio de búsqueda. Las partículas se mueven a través del espacio de búsqueda "
                           "siguiendo la mejor partícula y la mejor partícula global. PSO es un algoritmo de "
                           "optimización global que no requiere derivadas y es fácil de implementar.",
            "class_name": "PSO"
        }
