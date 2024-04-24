import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer


class Environment(Observer, ttk.Labelframe):

    def __init__(self, master=None) -> ttk.Frame:
        super().__init__(master)
        self.create_widgets()
        self.configure(text="Ambiente")

    def create_widgets(self):

        self.environment_label = ttk.Label(self, text="Ambiente")
        self.environment_label.pack(side=LEFT, padx=10)

        self.show_btn = ttk.Button(
            self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

    def toggle_frame(self):
        if self.environment_label.winfo_ismapped():
            self.environment_label.pack_forget()
            self.show_btn.config(text="Mostrar")
        else:
            self.environment_label.pack(expand=YES, fill=BOTH)
            self.show_btn.config(text="Ocultar")

    def update(self, swarm):
        print("Se actualiza el ambiente... PD: no hay ambiente :(")
