import tkinter as tk

class Hyperparameters(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hyperparameters = tk.Label(self, text="Hiperparámetros")
        self.hyperparameters.pack(side="top")

