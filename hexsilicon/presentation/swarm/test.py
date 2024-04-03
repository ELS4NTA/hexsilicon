import tkinter as tk
from tkinter import ttk

class SimulationConfigure(ttk.Frame):
    def __init__(self, master=None, enjambres=None, algoritmos=None):
        super().__init__(master)
        self.master = master
        self.enjambres = enjambres
        self.algoritmos = algoritmos
        self.create_widgets()
        self.place_widgets()
        self.pack()

    def create_widgets(self):
        # Enjambre selection
        self.enjambre_frame = ttk.Labelframe(self, text="Enjambres")
        if self.enjambres is not None:
            self.enjambre_combobox = ttk.Combobox(
                self.enjambre_frame, values=self.enjambres, state="readonly")
            self.enjambre_combobox.bind("<<ComboboxSelected>>", self.update_algorithm_combobox)

        # Algorithm selection
        self.algorithm_frame = ttk.Labelframe(self, text="Algoritmos")

        # Algorithm combobox (initially empty)
        self.algorithm_combobox = ttk.Combobox(
            self.algorithm_frame, state="readonly")

    def place_widgets(self):
        # Enjambre selection
        self.enjambre_frame.grid(row=0, column=0, padx=10, pady=10)
        self.enjambre_combobox.grid(row=0, column=0, padx=10, pady=10)

        # Algorithm selection
        self.algorithm_frame.grid(row=1, column=0, padx=10, pady=10)
        self.algorithm_combobox.grid(row=0, column=0, padx=10, pady=10)

    def update_algorithm_combobox(self, event):
        selected_enjambre = self.enjambre_combobox.get()
        if selected_enjambre and selected_enjambre in self.algoritmos:
            # Clearing previous options
            self.algorithm_combobox['values'] = ()
            # Updating with selected enjambre's algorithms
            self.algorithm_combobox['values'] = self.algoritmos[selected_enjambre]

if __name__ == "__main__":
    root = tk.Tk()

    # Example data (enjambres and algoritmos)
    enjambres = ["Enjambre 1", "Enjambre 2", "Enjambre 3"]
    algoritmos = {
        "Enjambre 1": ["Algoritmo A1", "Algoritmo A2", "Algoritmo A3"],
        "Enjambre 2": ["Algoritmo B1", "Algoritmo B2", "Algoritmo B3"],
        "Enjambre 3": ["Algoritmo C1", "Algoritmo C2", "Algoritmo C3"]
    }

    # Create and pack the SimulationConfigure widget
    simulation_configure = SimulationConfigure(root, enjambres, algoritmos)

    root.mainloop()
