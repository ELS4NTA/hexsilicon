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

class TestBall:
    def __init__(self, canvas, points, image_path, speed_factor=0.01, image_size=(50, 50)):
        self.canvas = canvas
        self.points = points
        self.speed_factor = speed_factor
        image = Image.open(image_path)  
        image = image.resize(image_size)  
        self.image = ImageTk.PhotoImage(image)
        self.id = canvas.create_image(points[0][0], points[0][1], image=self.image)
        self.current_point_index = 0
        self.x_velocity = self.y_velocity = 0

    def move(self):
        current_coords = self.canvas.coords(self.id)
        if abs(current_coords[0] - self.points[self.current_point_index][0]) < 1 and abs(current_coords[1] - self.points[self.current_point_index][1]) < 1:
            self.current_point_index = (self.current_point_index + 1) % len(self.points)
            next_point = self.points[self.current_point_index]
            self.x_velocity = (next_point[0] - current_coords[0]) * self.speed_factor
            self.y_velocity = (next_point[1] - current_coords[1]) * self.speed_factor
        self.canvas.move(self.id, self.x_velocity, self.y_velocity)