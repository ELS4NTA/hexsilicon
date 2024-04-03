import ttkbootstrap as ttk


class SimulationConfigure(ttk.Frame):
    def __init__(self, master=None, problems=None):
        super().__init__(master)
        self.master = master
        self.problems = problems
        self.create_widgets()
        self.place_widgets()
        self.pack()

    def create_widgets(self):
        # Title
        self.simulation_title = ttk.Label(self, text="Configuración Inicial", font=("Arial Bold", 20))

        # Problems selection
        self.problem_frame = ttk.Labelframe(self, text="Problemas")
        # add to label frame problem combo box
        if self.problems is not None:
            self.problem_combobox = ttk.Combobox(
                self.problem_frame, values=self.problems.get_problems())

        # Algorithm selection
        self.algorithm_frame = ttk.Labelframe(self, text="Algoritmo")
        self.algorithm = ttk.Combobox(self.algorithm_frame, values=[
                                      "SACO", "Algoritmo 2", "Algoritmo 3"])

        # Start button
        self.start_button = ttk.Button(
            self, text="Iniciar Simulación", command=lambda: self.master.start_simulation(self.algorithm.get(), self.problem_combobox.get()))

    def place_widgets(self):
        # Title
        self.simulation_title.grid(row=0, column=0, columnspan=2, pady=10)

        # Problems selection
        self.problem_frame.grid(row=1, column=0, padx=10)
        self.problem_combobox.grid(row=0, column=0, padx=20, pady=20)

        # Algorithm selection
        self.algorithm_frame.grid(row=1, column=1, padx=10)
        self.algorithm.grid(row=0, column=0, padx=20, pady=20)

        # Start button
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)
