import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from hexsilicon.presentation.dashboard import Dashboard
from hexsilicon.presentation.control import Control
from hexsilicon.presentation.evironment import Environment
import hexsilicon.domain.swarm.algorithms.ACO as ACO
from hexsilicon.domain.problem.problem import Problem
from hexsilicon.domain.problem.restriction import Restriction
from hexsilicon.domain.problem.domain import Domain
import pandas as pd
from hexsilicon.domain.problem.problems.MinPathFunction import MinPathFunction


class Execution(ttk.Frame):

    def __init__(self, master=None, algorithm=None, problem=None):
        super().__init__(master)
        self.create_widgets()
        self.problem = problem
        self.algorithm = algorithm
        self.set_observers()
        self.pack(expand=YES, fill=BOTH)

    def create_widgets(self):
        self.control = Control(self)
        self.dashboard = Dashboard(self)
        self.environment = Environment(self)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.control.grid(column=0, row=0, sticky=NW)
        self.environment.grid(column=0, row=1, sticky=N)
        self.dashboard.grid(column=1, row=0, rowspan=2, sticky=E)

    def place_widgets(self):
        geometry = self.master.winfo_geometry()
        window_width = int(geometry.split("x")[0])
        window_height = int(geometry.split("x")[1].split("+")[0])
        padding = 10

        # Buttons to see problem, natual or stop execution
        self.buttons_frame.place(x=padding, y=padding, width=window_width*0.66+padding, height=window_height*0.1)
        self.see_problem_button.grid(row=0, column=0, padx=10)
        self.start_execution_button.grid(row=0, column=1, padx=10)
        self.stop_execution_button.grid(row=0, column=2, padx=10)

        # Simulation environment
        self.simulation_environment_frame.place(x=padding, y=padding+window_height*0.1, width=window_width*0.66+padding, height=window_height*0.5)
        self.simulation_environment.grid(row=0, column=0)

    def see_problem(self):
        pass

    def start_execution(self):
        self.instancia.generate_initial_swarm()
        self.instancia.metaheuristic()

    def stop_execution(self):
        pass

    def place_solution_results(self):
        # pedir al enjmabre su mejor solucion global
        # con la libreria nx construir el grafo
        # guardar el grafo en una variable de matplotlib
        # mostrar la variable en el grafico de tkinter-bootsrap
        pass

    def place_history_function(self):
        # pedir al enjambre su historia de la funcion
        # crear una grafica de linea con la historia de la funcion
        # guardar la grafica en una variable de matplotlib
        # mostrar la variable en el grafico de tkinter-bootsrap
        pass

    def set_observers(self):
        clase = getattr(ACO, self.algorithm)
        print(clase)
        print(type(clase))
        problem = self.example_problem()

        self.instancia = ACO.SACO(problem)
        self.dashboard.set_hyperparams(self.instancia.get_hyperparams())
        history = self.dashboard.get_history_frame()
        graphic = self.dashboard.get_graphic_frame()
        self.instancia.subscribe(history)
        self.instancia.subscribe(graphic)


    def example_problem(self):
        df = pd.DataFrame({'source': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5],
                           'target': [2, 3, 6, 3, 7, 6, 7, 5, 5, 7, 6],
                           'weight': [5, 3.1, 5.2, 4.9, 5.2, 3.2, 3, 6, 5.5, 4.8, 4.7]})
        dict_restrictions = {'initial_point': 1, 'final_point': 4}
        R = Restriction(dict_restrictions)
        D = Domain(df, R)
        return Problem(D, MinPathFunction())


