import configure_simulation
import ttkbootstrap as ttk
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
            master=self, swarms=Swarms(), algorithms=Swarms(), problems=Problems())

    def start_simulation(self):
        self.problem = self.simulation.get_problem()
        self.algorithm = "SACO"
        print(self.problem.get_domain())
        for widget in self.winfo_children():
            widget.destroy()
        self.title("Ejecución de la Simulación")
        self.execution = Execution(
            master=self, algorithm=self.algorithm, problem=self.problem)

# De donde salen los problemas?


class Problems:
    def get_problems(self):
        return ["Problema 1", "Problema 2", "Problema 3"]

    def get_problem_description(self, problem):
        return ("The Traveling Salesman Problem (TSP) is the challenge of finding the shortest path or shortest route "
                "for a salesperson to take, given a starting point, a number of cities (nodes), and optionally an "
                "ending point")


class Swarms:
    def get_swarms(self):
        return ["Enjambre 1", "Enjambre 2", "Enjambre 3"]

    def get_algorithms(self):
        return ["SACO", "Algoritmo 2", "Algoritmo 3"]

    def get_algorithm_description(self, algorithm):
        return "Algoritmo de enjambre de partículas"

    def get_swarm_description(self, swarm):
        return "Enjambre de partículas"

