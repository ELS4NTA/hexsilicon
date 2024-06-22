import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer


class Representation(Observer, ttk.Frame):

    def __init__(self, master=None, gauge=None):
        super().__init__(master)
        self.master = master
        self.gauge = gauge
        self.will_update = True
        self.create_widgets()

    def create_widgets(self):
        self.show_btn = ttk.Button(self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

        self.frame = ttk.Frame(self)
        self.frame.pack(expand=YES, fill=BOTH)

        self.text = ttk.Text(self.frame, height=10)
        self.text.pack(side=LEFT, fill=BOTH, expand=YES)

        self.scrollbar = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.text.yview, bootstyle="primary-round")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text['yscrollcommand'] = self.scrollbar.set

    def toggle_frame(self):
        if self.frame.winfo_ismapped():
            self.frame.pack_forget()
            self.will_update = False
            self.show_btn.config(text="Mostrar")
        else:
            self.frame.pack(expand=YES, fill=BOTH)
            self.will_update = True
            self.show_btn.config(text="Ocultar")

    def update(self, swarm):
        solution = swarm.best_agent.get_solution()
        iteration = list(swarm.history.keys())[-1]
        self.gauge.configure(value=iteration+1)
        cost = swarm.best_agent.get_score()
        if self.will_update:
            self.text.insert(float(iteration + 1),
                             f"Iteración {iteration} la mejor solución fue: {solution} con el costo {cost}\n")
