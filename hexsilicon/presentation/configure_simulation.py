import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog
import pandas as pd

from hexsilicon.domain.problem.problem import Problem
from hexsilicon.domain.problem.problems.MinPathFunction import MinPathFunction
from hexsilicon.domain.problem.restriction import Restriction
from hexsilicon.domain.problem.domain import Domain


class SimulationConfigure(ttk.Frame):
    def __init__(self, master=None, swarms=None, algorithms=None, problems=None):
        super().__init__(master)
        self.master = master
        self.swarms = swarms
        self.algorithms = algorithms
        self.problems = problems
        self.create_widgets()
        self.place_widgets()
        self.pack()

    def create_widgets(self):
        # Title
        self.simulation_title = ttk.Label(self, text="Configuración Inicial", font=("Arial Bold", 20))

        # Swarm selection
        self.swarm_frame = ttk.Labelframe(self, text="Enjambre")
        if self.swarms is not None:
            self.swarm_combobox = ttk.Combobox(
                self.swarm_frame, values=self.swarms.get_swarms())
            self.swarm_combobox.bind("<<ComboboxSelected>>", self.update_swarm_description)

        # Description of Swarm
        self.swarm_description_frame = ttk.Labelframe(self, border=0)
        self.swarm_description = ttk.Label(self.swarm_description_frame, text="", wraplength=200, justify="center")
        self.swarm_description.config(font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Algorithm selection
        self.algorithm_frame = ttk.Labelframe(self, text="Algoritmo")
        if self.algorithms is not None:
            self.algorithm_combobox = ttk.Combobox(
                self.algorithm_frame, values=self.algorithms.get_algorithms())
            self.algorithm_combobox.bind("<<ComboboxSelected>>", self.update_algorithm_description)

        # Description of Algorithm
        self.algorithm_description_frame = ttk.Labelframe(self, border=0)
        self.algorithm_description = ttk.Label(self.algorithm_description_frame, text="", wraplength=200, justify="center")
        self.algorithm_description.config(font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Problems selection
        self.problem_frame = ttk.Labelframe(self, text="Problemas")
        if self.problems is not None:
            self.problem_combobox = ttk.Combobox(
                self.problem_frame, values=self.problems.get_problems())
            self.problem_combobox.bind("<<ComboboxSelected>>", self.update_problem_description)

        # Description of Problem
        self.problem_description_frame = ttk.Labelframe(self, border=0)
        self.text_description = ttk.Label(self.problem_description_frame, text="", wraplength=200, justify="center")
        self.text_description.config(font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Select file
        self.file_frame = ttk.Labelframe(self, text="Específicaciones del Problema")
        self.file_button = ttk.Button(self.file_frame, text="Seleccionar", command=self.open_file)
        self.file_name_label = ttk.Label(self.file_frame, text="", justify="center")

        # Start button
        self.start_button = ttk.Button(
            self, text="Iniciar Simulación", command=self.start_simulation)

    def place_widgets(self):
        # Title
        self.simulation_title.grid(row=0, column=0, columnspan=3, pady=10)

        # Swarm selection
        self.swarm_frame.grid(row=1, column=0, padx=10)
        self.swarm_combobox.grid(row=0, column=0, padx=20, pady=20)

        # Algorithm selection
        self.algorithm_frame.grid(row=1, column=1, padx=10)
        self.algorithm_combobox.grid(row=0, column=0, padx=20, pady=20)

        # Description of Swarm
        self.swarm_description_frame.grid(row=2, column=0, pady=10)
        self.swarm_description.grid(row=0, column=0, pady=10)
        # hide the label
        self.swarm_description.grid_remove()

        # Description of Algorithm
        self.algorithm_description_frame.grid(row=2, column=1, pady=10)
        self.algorithm_description.grid(row=0, column=0, pady=10)
        # hide the label
        self.algorithm_description.grid_remove()

        # Problems selection
        self.problem_frame.grid(row=1, column=2, padx=10)
        self.problem_combobox.grid(row=0, column=0, padx=20, pady=20)

        # Description of Problem
        self.problem_description_frame.grid(row=2, column=2, pady=10)
        self.text_description.grid(row=0, column=0, pady=10)
        # hide the label
        self.text_description.grid_remove()

        # Select file problem
        self.file_frame.grid(row=3, column=2, padx=10)
        self.file_button.grid(row=0, column=0, padx=5, pady=5)
        self.file_name_label.grid(row=1, column=0, padx=5, pady=5)

        # Start button
        self.start_button.grid(row=4, column=0, columnspan=3, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            file_name = file_path.split("/")[-1]
            self.file_name_label.config(text="Archivo Seleccionado: " + file_name)
            with open(file_path, "r") as file_obj:
                content = file_obj.read()
                self.get_problem_data(content)

    def get_problem_data(self, content):
        self.source = list(map(int, content.split("\n")[0].split(",")))
        self.target = list(map(int, content.split("\n")[1].split(",")))
        self.weights = list(map(float, content.split("\n")[2].split(",")))
        self.pto_ini = int(content.split("\n")[3])
        self.pto_fin = int(content.split("\n")[4])
        self.objetive = content.split("\n")[5]

    def create_problem(self):
        # Create Restriction
        self.restriction = Restriction({'initial_point': self.pto_ini, 'final_point': self.pto_fin})
        # Create dataframe
        self.data_frame = pd.DataFrame(
            {
                'source': self.source,
                'target': self.target,
                'weight': self.weights
            }
        )
        # Create the domain
        self.domain = Domain(self.data_frame, self.restriction)
        # Create function objective
        # Create the problem
        self.problem = Problem(self.domain, MinPathFunction())

    def get_problem(self):
        return self.problem

    def start_simulation(self):
        self.create_problem()
        self.master.start_simulation()


    def update_problem_description(self, event):
        selected_problem = self.problem_combobox.get()
        description = self.problems.get_problem_description(selected_problem)
        self.text_description.config(text=description)
        self.text_description.update()
        # Show the label
        self.text_description.grid()

    def update_algorithm_description(self, event):
        selected_algorithm = self.algorithm_combobox.get()
        description = self.algorithms.get_algorithm_description(selected_algorithm)
        self.algorithm_description.config(text=description)
        self.algorithm_description.update()
        # Show the label
        self.algorithm_description.grid()

    def update_swarm_description(self, event):
        selected_swarm = self.swarm_combobox.get()
        description = self.swarms.get_swarm_description(selected_swarm)
        self.swarm_description.config(text=description)
        self.swarm_description.update()
        # Show the label
        self.swarm_description.grid()

