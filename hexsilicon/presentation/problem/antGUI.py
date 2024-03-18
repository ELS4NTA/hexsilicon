import tkinter as tk

# This class is a GUI for the problem selection 
class ProblemSelection(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass