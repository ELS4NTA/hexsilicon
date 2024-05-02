import matplotlib.pyplot as plt
import ttkbootstrap as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer


class History(Observer, ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.canvas = None
        self.will_update = True
        self.create_widgets()

    def create_widgets(self):
        self.show_btn = ttk.Button(self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

        # Inicializar la figura y los ejes
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=70)
        self.ax.set_xlabel("Iteración")
        self.ax.set_ylabel("Costo")
        self.ax.set_title("Función de costo")

        # Crear un objeto Line2D vacío
        self.line, = self.ax.plot([], [], label="y = x^2")

        # Mostrar la gráfica en el marco sin redimensionamiento
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)

    def toggle_frame(self):
        if self.canvas is not None:
            if self.canvas.get_tk_widget().winfo_ismapped():
                self.canvas.get_tk_widget().pack_forget()
                self.will_update = False
                self.show_btn.config(text="Mostrar")
            else:
                self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
                self.will_update = True
                self.show_btn.config(text="Ocultar")

    def update(self, swarm):
        history = swarm.history

        # Actualizar los datos del objeto Line2D
        x = list(history.keys())
        y = list(history.values())
        self.line.set_data(x, y)

        # Ajustar los límites de los ejes para acomodar los nuevos datos
        if len(set(x)) > 1:
            self.ax.set_xlim(min(x), max(x))
        else:
            self.ax.set_xlim(min(x) - 1, max(x) + 1)

        if len(set(y)) > 1:
            self.ax.set_ylim(min(y), max(y))
        else:
            self.ax.set_ylim(min(y) - 1, max(y) + 1)

        # Redibujar el canvas
        if self.will_update:
            self.canvas.draw()
