import matplotlib.pyplot as plt
import ttkbootstrap as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer


class Graphic(Observer, ttk.Frame):

    def __init__(self, master=None, visualization=None):
        super().__init__(master)
        self.master = master
        self.problem_visualization = visualization()
        self.will_update = True
        self.first_time = True
        self.pos = None
        self.create_widgets()

    def create_widgets(self):
        self.show_btn = ttk.Button(self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

        # Inicializar la figura y el canvas
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=70)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)

    def toggle_frame(self):
        if self.canvas.get_tk_widget().winfo_ismapped():
            self.canvas.get_tk_widget().pack_forget()
            self.will_update = False
            self.show_btn.config(text="Mostrar")
        else:
            self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
            self.will_update = True
            self.show_btn.config(text="Ocultar")

    def update(self, swarm):
        if self.will_update:
            self.problem_visualization.draw(swarm, self.ax)
            self.canvas.draw()
