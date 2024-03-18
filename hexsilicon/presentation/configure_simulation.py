import tkinter as tk


class SimulationConfigure(tk.Frame):
    def __init__(self, master=None, problems=None):
        super().__init__(master)
        self.master = master
        self.problems = problems
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.simulation = tk.Label(self, text="Configuración Inicial")
        self.simulation.grid(row=0, column=0, columnspan=2)

        self.problem_label = tk.Label(self, text="Problema")
        self.problem_label.grid(row=1, column=0)

        if self.problems is not None:
            self.problem_listbox = tk.Listbox(self, selectmode=tk.SINGLE, bg=self.cget('bg'), fg='black', bd=0, highlightthickness=0, relief='flat', font=('Arial', 12))
            for problem in self.problems.get_problems():
                self.problem_listbox.insert(tk.END, problem)
        self.problem_listbox.grid(row=2, column=0, sticky='nsew')

        # Ajustar el tamaño del ListBox al tamaño de la ventana
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.algorithm = tk.Label(self, text="Algoritmo")
        self.algorithm.grid(row=1, column=1)

