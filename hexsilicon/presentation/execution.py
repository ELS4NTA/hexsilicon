import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Execution(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.place_widgets()
        self.pack(expand=YES, fill=BOTH)

    def create_widgets(self):
        # Buttons to see problem, natual or stop execution
        self.buttons_frame = ttk.Labelframe(self, text="Ejecución")
        self.see_problem_button = ttk.Button(self.buttons_frame, text="Ver Problema", command=self.see_problem)
        self.start_execution_button = ttk.Button(self.buttons_frame, text="Ver Natural", command=self.see_natural)
        self.stop_execution_button = ttk.Button(self.buttons_frame, text="Detener Ejecución", command=self.stop_execution)

        # Simulation environment
        self.simulation_environment_frame = ttk.Labelframe(self, text="Entorno de Simulación")
        self.simulation_environment = ttk.Label(self.simulation_environment_frame, text="Entorno de Simulación")

        # Hyperparameters
        self.hyperparameters_frame = ttk.Labelframe(self, text="Hiperparámetros")
        for hyperparameter in ["Hiperparámetro 1", "Hiperparámetro 2", "Hiperparámetro 3"]:
            ttk.Label(self.hyperparameters_frame, text=hyperparameter).pack()

        # Simulation velocity
        self.simulation_velocity_frame = ttk.Labelframe(self, text="Velocidad de Simulación")
        self.simulation_velocity = ttk.Label(self.simulation_velocity_frame, text="Velocidad de Simulación")
        
        # Ghraphic funcition
        self.graphic_frame = ttk.Labelframe(self, text="Gráfica")
        self.graphic = ttk.Label(self.graphic_frame, text="Gráfica")

        # Best Global Solution
        self.best_global_solution_frame = ttk.Labelframe(self, text="Mejor Solución Global")
        self.best_global_solution = ttk.Label(self.best_global_solution_frame, text="Mejor Solución Global")

        # Best Local Solution
        self.best_local_solution_frame = ttk.Labelframe(self, text="Mejor Solución Local")
        self.best_local_solution = ttk.Label(self.best_local_solution_frame, text="Mejor Solución Local")

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

        # Hyperparameters
        self.hyperparameters_frame.place(x=(padding*2)+window_width*0.66+padding,y=padding,width=window_width*0.3, height=window_height*0.3)
        self.hyperparameters_frame.grid_propagate(0)

        # Simulation velocity
        self.simulation_velocity_frame.place(x=(padding*2)+window_width*0.66+padding,y=padding+window_height*0.3,width=window_width*0.3, height=window_height*0.3)
        self.simulation_velocity.grid(row=0, column=0)

        # Ghraphic funcition
        self.graphic_frame.place(x=padding,y=window_height*0.6+padding,width=window_width*0.33, height=window_width*0.2)
        self.graphic.grid(row=0, column=0)

        # Best Global Solution
        self.best_global_solution_frame.place(x=(padding*2)+window_width*0.33,y=window_height*0.6+padding,width=window_width*0.33, height=window_width*0.2)
        self.best_global_solution.grid(row=0, column=0)

        # Best Local Solution
        self.best_local_solution_frame.place(x=(padding*3)+window_width*0.66,y=window_height*0.6+padding,width=window_width*0.3, height=window_width*0.2)
        self.best_local_solution.grid(row=0, column=0)

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

