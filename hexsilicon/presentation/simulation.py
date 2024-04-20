import ttkbootstrap as ttk

from hexsilicon.presentation import configure_simulation
from hexsilicon.presentation.execution import Execution


class Simulation(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Configuración de la Simulación")
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * 0.6)
        window_height = int(screen_height * 0.6)
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.resizable(False, False)

    def create_widgets(self):
        self.simulation = configure_simulation.SimulationConfigure(
            master=self, swarms_algorithm=self.get_swarm_algorithm(), algorithms_problems=self.get_algorithm_problem(),
            description=self.get_description())

    def start_simulation(self, swarm, algorithm, problem, context):
        for widget in self.winfo_children():
            widget.destroy()
        self.title("Ejecución de la Simulación")
        self.execution = Execution(master=self, swarm=swarm, algorithm=algorithm, problem=problem, context=context)

    def get_swarm_algorithm(self):
        return {
            "Colonia de Hormigas": ["SACO", "MAXMIN"],
            "Bandada de aves": ["PSO", "APSO"]
        }

    def get_algorithm_problem(self):
        return {
            "SACO": ["TSP", "MIN"],
            "MAXMIN": ["TSP", "QAP"],
            "PSO": ["TSP", "QAP"],
            "APSO": ["TSP", "QAP"]
        }

    def get_description(self):
        return {
            "Colonia de Hormigas": "La metaheurística ACO se inspira en la observación del comportamiento de colonias "
                                   "de hormigas reales, cómo encontrar los caminos más cortos entre el nidos y la "
                                   "comida.",
            "Bandada de aves": "Algoritmo de bandada de pájaros",
            "SACO": "Algoritmo mas simple de colonia de hormigas",
            "MAXMIN": "Algoritmo de colonia de hormigas con feromonas MAX-MIN",
            "PSO": "Optimización por enjambre de partículas",
            "APSO": "Optimización por enjambre de partículas adaptativo",
            "TSP": "Problema del vendedor viajero",
            "MIN": "Problema de encontrar el camino más corto",
            "QAP": "Problema de asignación cuadrática"
        }

    def get_name_class(self):
        return {
            "Colonia de Hormigas": "AntColony",
            "Bandada de aves": "PSO",
            "SACO": "SACO",
            "MAXMIN": "ACO",
            "PSO": "PSO",
            "APSO": "PSO",
            "TSP": "TSP",
            "MIN": "MIN",
            "QAP": "QAP"
        }
