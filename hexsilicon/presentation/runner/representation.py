import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer


class Representation(Observer, ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
    
    def create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(expand=YES, fill=BOTH)

        self.text = ttk.Text(frame, height=10)
        self.text.pack(side=LEFT, fill=BOTH, expand=YES)

        self.scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=self.text.yview, bootstyle="primary-round")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text['yscrollcommand'] = self.scrollbar.set

    def update(self, swarm):
        print("Se pinta la representación por iteracion")
        path_history = swarm.path_history
        for iteration, path in path_history.items():
            position = f'{iteration+1}.0'
            self.text.insert(position, f"Iteración {iteration+1} el mejor camino fue: {path}\n")

