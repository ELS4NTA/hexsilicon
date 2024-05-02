import networkx as nx
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer
from hexsilicon.swarms.swarm import Swarm


class Environment(Observer, ttk.Labelframe):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(text="Ambiente")
        self.image_ids = []

    def create_widgets(self):

        self.show_btn = ttk.Button(self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)
        self.show_btn.pack()

        # Crear un canvas para la imagen
        self.canvas = ttk.Canvas(self, width=500, height=500)
        self.canvas.pack(expand=YES, fill=BOTH)


    def toggle_frame(self):
        if self.canvas.winfo_ismapped():
            self.canvas.pack_forget()
            self.show_btn.config(text="Mostrar")
        else:
            self.canvas.pack(expand=YES, fill=BOTH)
            self.show_btn.config(text="Ocultar")

    def update(self, swarm: Swarm):
        print("Esta basura del ambiente...")
        # Cargar la imagen
        G = swarm.problem.get_representation()
        pos = nx.spring_layout(G)

        # Encontrar los valores mínimos y máximos de las posiciones
        self.min_x = min(pos.values(), key=lambda x: x[0])[0]
        self.max_x = max(pos.values(), key=lambda x: x[0])[0]
        self.min_y = min(pos.values(), key=lambda x: x[1])[1]
        self.max_y = max(pos.values(), key=lambda x: x[1])[1]

        image = Image.open("icons/insecto.png")
        image = image.resize((24, 24))
        photo = ImageTk.PhotoImage(image)
        print(pos)

        # Dibujar la imagen en el canvas
        for i, agent in enumerate(swarm.population):
            pased_points = agent.get_solution().copy()
            agent_position = pased_points.pop(0)
            # Normalizar las posiciones a las dimensiones del canvas
            x = self.normalize(pos[agent_position][0], self.min_x, self.max_x, 0, self.canvas.winfo_width())
            y = self.normalize(pos[agent_position][1], self.min_y, self.max_y, 0, self.canvas.winfo_height())
            image_id = self.canvas.create_image(x, y, anchor=NW, image=photo)  # Guardar el ID de la imagen
            self.image_ids.append(image_id)  # Añadir el ID a la lista
            self.animate(pos, i, pased_points)
        self.canvas.image = photo

    def animate(self, pos, i, pased_points):
        if pased_points:
            next_point = pased_points.pop(0)
            # Normalizar las posiciones a las dimensiones del canvas
            x = self.normalize(pos[next_point][0], self.min_x, self.max_x, 0, self.canvas.winfo_width())
            y = self.normalize(pos[next_point][1], self.min_y, self.max_y, 0, self.canvas.winfo_height())


            self.canvas.move(self.image_ids[i], x, y)  # Usar el ID de la imagen para moverla
        else:
            return

    def normalize(self, value, min_value, max_value, new_min, new_max):
        return ((value - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min
    
    def get_points_paint(self):
        pass