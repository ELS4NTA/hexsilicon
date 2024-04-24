import matplotlib.pyplot as plt
import ttkbootstrap as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer


class History(Observer, ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.show_btn = ttk.Button(
            self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

    def place_widgets(self):
        pass

    def example_function_plot(self):
        # Crear una figura y un eje
        fig = plt.figure(figsize=(6, 4), dpi=70)

        # Graficar la función y personalizar la gráfica
        ax = fig.add_subplot(111)
        x = range(-10, 11)
        y = [x_val ** 2 for x_val in x]
        ax.plot(x, y, label="y = x^2")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Función cuadrática")

        # Mostrar la gráfica en el marco sin redimensionamiento
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()

        # Configurar el Canvas para que no tenga bordes de resaltado
        self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)

    def toggle_frame(self):
        if self.canvas.get_tk_widget().winfo_ismapped():
            self.canvas.get_tk_widget().pack_forget()
            self.show_btn.config(text="Mostrar")
        else:
            self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
            self.show_btn.config(text="Ocultar")

    def update(self, swarm):
        print("Se dibuja la historia")
        history = swarm.history
        fig = plt.figure(figsize=(6, 4), dpi=70)

        # Graficar la función y personalizar la gráfica
        ax = fig.add_subplot(111)
        x = history.keys()
        y = history.values()
        ax.plot(x, y, label="y = x^2")
        ax.set_xlabel("Iteración")
        ax.set_ylabel("Costo")
        ax.set_title("Función de costo")

        # Mostrar la gráfica en el marco sin redimensionamiento
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()

        # Configurar el Canvas para que no tenga bordes de resaltado
        self.canvas.get_tk_widget().pack(expand=YES, fill=BOTH)
