import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from hexsilicon.presentation.dashboard import Dashboard
from hexsilicon.presentation.control import Control
from hexsilicon.presentation.evironment import Environment


class Execution(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        #self.place_widgets()
        self.pack(expand=YES, fill=BOTH)

    def create_widgets(self):
        # Buttons to see problem, natual or stop execution
        # self.buttons_frame = ttk.Labelframe(self, text="Ejecución")
        # self.see_problem_button = ttk.Button(self.buttons_frame, text="Ver Problema", command=self.see_problem)
        #self.start_execution_button = ttk.Button(self.buttons_frame, text="Ver Natural", command=self.see_natural)
        #self.stop_execution_button = ttk.Button(self.buttons_frame, text="Detener Ejecución", command=self.stop_execution)

        # Simulation environment
        #self.simulation_environment_frame = ttk.Labelframe(self, text="Entorno de Simulación")
        #self.simulation_environment = ttk.Label(self.simulation_environment_frame, text="Entorno de Simulación")

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
        self.buttons_frame.place(x=padding,y=padding,width=window_width*0.66+padding, height=window_height*0.1)
        self.see_problem_button.grid(row=0, column=0, padx=10)
        self.start_execution_button.grid(row=0, column=1, padx=10)
        self.stop_execution_button.grid(row=0, column=2, padx=10)

        # Simulation environment
        self.simulation_environment_frame.place(x=padding,y=padding+window_height*0.1,width=window_width*0.66+padding, height=window_height*0.5)
        self.simulation_environment.grid(row=0, column=0)

    def see_problem(self):
        pass

    def see_natural(self):
        pass

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

