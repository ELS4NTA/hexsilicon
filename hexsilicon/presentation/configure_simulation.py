from tkinter import filedialog

import ttkbootstrap as ttk


class SimulationConfigure(ttk.Frame):
    def __init__(self, master=None, swarms_algorithm=None, algorithms_problems=None, description=None):
        super().__init__(master)
        self.master = master
        self.swarms_algorithms = swarms_algorithm
        self.algorithms_problems = algorithms_problems
        self.description = description
        self.create_widgets()
        self.place_widgets()
        self.pack()

    def create_widgets(self):
        # Title
        self.simulation_title = ttk.Label(
            self, text="Configuración Inicial", font=("Arial Bold", 20))

        # Swarm selection
        self.swarm_frame = ttk.Labelframe(self, text="Enjambre")
        if self.swarms_algorithms is not None:
            self.swarm_combobox = ttk.Combobox(
                self.swarm_frame, values=list(self.swarms_algorithms.keys()))
            self.swarm_combobox.bind(
                "<<ComboboxSelected>>", self.update_swarm_description)

        # Description of Swarm
        self.swarm_description_frame = ttk.Labelframe(self, border=0)
        self.swarm_description = ttk.Label(
            self.swarm_description_frame, text="", wraplength=200, justify="center")
        self.swarm_description.config(
            font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Algorithm selection
        self.algorithm_frame = ttk.Labelframe(self, text="Algoritmo")
        if self.algorithms_problems is not None:
            self.algorithm_combobox = ttk.Combobox(
                self.algorithm_frame)
            self.algorithm_combobox.bind(
                "<<ComboboxSelected>>", self.update_algorithm_description)

        # Description of Algorithm
        self.algorithm_description_frame = ttk.Labelframe(self, border=0)
        self.algorithm_description = ttk.Label(
            self.algorithm_description_frame, text="", wraplength=200, justify="center")
        self.algorithm_description.config(
            font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Problems selection
        self.problem_frame = ttk.Labelframe(self, text="Problemas")
        if self.algorithms_problems is not None:
            self.problem_combobox = ttk.Combobox(
                self.problem_frame)
            self.problem_combobox.bind(
                "<<ComboboxSelected>>", self.update_problem_description)

        # Description of Problem
        self.problem_description_frame = ttk.Labelframe(self, border=0)
        self.text_description = ttk.Label(
            self.problem_description_frame, text="", wraplength=200, justify="center")
        self.text_description.config(
            font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Select file
        self.file_frame = ttk.Labelframe(
            self, text="Específicaciones del Problema")
        self.file_button = ttk.Button(
            self.file_frame, text="Seleccionar", command=self.open_file)
        self.file_name_label = ttk.Label(
            self.file_frame, text="", justify="center")

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
        self.swarm_description_frame.grid(row=2, column=0, pady=10, padx=10)
        self.swarm_description.grid(row=0, column=0, pady=10)
        # hide the label
        self.swarm_description.grid_remove()

        # Description of Algorithm
        self.algorithm_description_frame.grid(row=2, column=1, pady=10, padx=10)
        self.algorithm_description.grid(row=0, column=0, pady=10)
        # hide the label
        self.algorithm_description.grid_remove()

        # Problems selection
        self.problem_frame.grid(row=1, column=2, padx=10)
        self.problem_combobox.grid(row=0, column=0, padx=20, pady=20)

        # Description of Problem
        self.problem_description_frame.grid(row=2, column=2, pady=10, padx=10)
        self.text_description.grid(row=0, column=0, pady=10)
        # hide the label
        self.text_description.grid_remove()

        # Select file problems
        self.file_frame.grid(row=3, column=2, padx=10)
        self.file_button.grid(row=0, column=0, padx=5, pady=5)
        self.file_name_label.grid(row=1, column=0, padx=5, pady=5)

        # Start button
        self.start_button.grid(row=4, column=0, columnspan=3, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Archivos csv", "*.csv")])
        if file_path:
            file_name = file_path.split("/")[-1]
            self.file_name_label.config(
                text="Archivo Seleccionado: " + file_name)
            with open(file_path, "r") as file_obj:
                self.content = file_obj.read()

    def start_simulation(self):
        self.master.start_simulation(self.swarm_combobox.get(), self.algorithm_combobox.get(),
                                     self.problem_combobox.get(), self.content)

    def update_problem_description(self, *args):
        description = self.description[self.problem_combobox.get()]
        self.text_description.config(text=description)
        self.text_description.update()
        # Show the label
        self.text_description.grid()

    def update_algorithm_description(self, *args):
        self.problem_combobox.set("")
        self.text_description.grid_remove()
        self.problem_combobox["values"] = self.algorithms_problems[self.algorithm_combobox.get()]
        description = self.description[self.algorithm_combobox.get()]
        self.algorithm_description.config(text=description)
        self.algorithm_description.update()
        # Show the label
        self.algorithm_description.grid()

    def update_swarm_description(self, *args):
        self.algorithm_combobox.set("")
        self.problem_combobox.set("")
        self.algorithm_description.grid_remove()
        self.text_description.grid_remove()
        self.algorithm_combobox["values"] = self.swarms_algorithms[self.swarm_combobox.get()]
        description = self.description[self.swarm_combobox.get()]
        self.swarm_description.config(text=description)
        self.swarm_description.update()
        # Show the label
        self.swarm_description.grid()
