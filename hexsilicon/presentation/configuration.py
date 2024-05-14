from tkinter import filedialog

import ttkbootstrap as ttk


class Configuration(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master # type: ignore
        self.swarms_descriptions = self.get_descriptions("Swarm")
        self.problems_descriptions = self.get_descriptions("GraphProblem")
        self.problems_descriptions.extend(self.get_descriptions("FreeProblem"))
        self.selected_swarm = None
        self.selected_algorithm = None
        self.selected_problem = None
        self.content = None
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        # Title
        self.simulation_title = ttk.Label(self, text="Configuración Inicial", font=("Arial Bold", 20))

        # Swarm selection
        self.swarm_frame = ttk.Labelframe(self, text="Enjambre")
        self.swarm_combobox = ttk.Combobox(self.swarm_frame,
                                           values=[swarm["name"] for swarm in self.swarms_descriptions])
        self.swarm_combobox.bind("<<ComboboxSelected>>", self.update_swarm_description)

        # Description of Swarm
        self.swarm_description_frame = ttk.Labelframe(self, border=0)
        self.swarm_description = ttk.Label(self.swarm_description_frame, text="", wraplength=200, justify="center")
        self.swarm_description.config(font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Algorithm selection
        self.algorithm_frame = ttk.Labelframe(self, text="Algoritmo")
        self.algorithm_combobox = ttk.Combobox(self.algorithm_frame)
        self.algorithm_combobox.bind("<<ComboboxSelected>>", self.update_algorithm_description)

        # Description of Algorithm
        self.algorithm_description_frame = ttk.Labelframe(self, border=0)
        self.algorithm_description = ttk.Label(self.algorithm_description_frame, text="", wraplength=200,
                                               justify="center")
        self.algorithm_description.config(font=("Arial", 10), padding=(10, 10,), background="#99E4FE")

        # Problems selection
        self.problem_frame = ttk.Labelframe(self, text="Problemas")
        self.problem_combobox = ttk.Combobox(self.problem_frame)
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
        self.start_button = ttk.Button(self, text="Iniciar Simulación", command=self.start_simulation)

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
        file_path = filedialog.askopenfilename(filetypes=[("Archivos csv", "*.csv")])
        if file_path:
            file_name = file_path.split("/")[-1]
            self.file_name_label.config(text="Archivo Seleccionado: " + file_name)
            with open(file_path, "r") as file_obj:
                self.content = file_obj.read()

    def start_simulation(self):
        self.master.start_simulation(self.selected_swarm, self.selected_algorithm, self.selected_problem, self.content) # type: ignore

    def update_problem_description(self, *args):
        problem_descriptions = next((problem for problem in self.problems_descriptions if problem['name'] == self.problem_combobox.get()), None)
        description = problem_descriptions['description'] # type: ignore
        self.text_description.config(text=description)
        self.selected_problem = problem_descriptions['class_name'] # type: ignore
        self.text_description.update()
        # Show the label
        self.text_description.grid()

    def update_algorithm_description(self, *args):
        # Reset widgets
        self.problem_combobox.set("")
        self.text_description.grid_remove()
        algorithm_descriptions = next(
            (behavior for behavior in self.algoritms_descriptions if behavior['name'] == self.algorithm_combobox.get()),
            None)
        description = algorithm_descriptions['description'] # type: ignore
        self.selected_algorithm = algorithm_descriptions['class_name'] # type: ignore
        self.problem_combobox["values"] = [problem['name'] for problem in self.problems_descriptions if self.algorithm_combobox.get() in problem['algorithms'].split(', ')]
        self.algorithm_description.config(text=description)
        self.algorithm_description.update()
        # Show the label
        self.algorithm_description.grid()

    def update_swarm_description(self, *args):
        # Reset widgets
        self.algorithm_combobox.set("")
        self.problem_combobox.set("")
        self.algorithm_description.grid_remove()
        self.text_description.grid_remove()

        swarm_descriptions = next(
            (swarm for swarm in self.swarms_descriptions if swarm['name'] == self.swarm_combobox.get()), None)
        description = swarm_descriptions['description'] # type: ignore
        self.selected_swarm = swarm_descriptions['class_name'] # type: ignore
        self.algoritms_descriptions = self.master.get_descriptions(swarm_descriptions['behavior']) # type: ignore
        self.algorithm_combobox["values"] = [behavior["name"] for behavior in self.algoritms_descriptions]
        self.swarm_description.config(text=description)
        self.swarm_description.update()
        # Show the label
        self.swarm_description.grid()

    def get_descriptions(self, class_name):
        return self.master.get_descriptions(class_name) # type: ignore
