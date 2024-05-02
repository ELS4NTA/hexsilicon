import time

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
        self.first_time = True
        self.speed_factor=0.01
        self.current_point_index = 0
        self.x_velocity = self.y_velocity = 0

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
        G = swarm.problem.get_representation()
        if self.first_time:
            self.first_time = False
            self.points = self.get_points_grapho(G)        
            for point in self.points.values():
                self.canvas.create_oval(point[0], point[1], point[0] + 5, point[1] + 5, fill="red")
        
        # Cargar la imagen
        image = Image.open("icons/insecto.png")
        image = image.resize((24, 24))
        photo = ImageTk.PhotoImage(image)

        # Dibujar la imagen en el canvas
        for i, agent in enumerate(swarm.population):
            pased_points = self.get_poinst_solution(agent.get_solution())
            for point in pased_points:
                self.canvas.create_oval(point[0], point[1], point[0] + 5, point[1] + 5, fill="blue")
            current_x, current_y = pased_points.pop(0)
            image_id = self.canvas.create_image(current_x, current_y, anchor=NW, image=photo)  # Guardar el ID de la imagen
            self.image_ids.append(image_id)  # Añadir el ID a la lista
            while len(pased_points) > 0:
                next_x, next_y = pased_points.pop(0)
                self.move(image_id, current_x, current_y, next_x, next_y)
                current_x, current_y = next_x, next_y
                self.master.update()
                time.sleep(0.0001)

    def normalize(self, value, min_value, max_value, new_min, new_max):
        return ((value - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min
    
    def get_points_grapho(self, G):
        pos = nx.spring_layout(G)
        
        # Encontrar los valores mínimos y máximos de las posiciones
        self.min_x = min(pos.values(), key=lambda x: x[0])[0]
        self.max_x = max(pos.values(), key=lambda x: x[0])[0]
        self.min_y = min(pos.values(), key=lambda x: x[1])[1]
        self.max_y = max(pos.values(), key=lambda x: x[1])[1]
        
        for key in pos:
            x = self.normalize(pos[key][0], self.min_x, self.max_x, 0, self.canvas.winfo_width())
            y = self.normalize(pos[key][1], self.min_y, self.max_y, 0, self.canvas.winfo_height())
            pos[key] = (x, y)
        return pos
    
    def get_poinst_solution(self, solution):
        path_positions = [tuple(self.points[i]) for i in solution if i in self.points]
        return path_positions
    
    def move(self, image_id, current_x, current_y, next_x, next_y):
        current_coords = self.canvas.coords(image_id)
        if abs(current_coords[0] - current_x) < 1 and abs(current_coords[1] - current_y) < 1:
            self.x_velocity = (next_x - current_coords[0]) * self.speed_factor
            self.y_velocity = (next_y - current_coords[1]) * self.speed_factor
        self.canvas.move(image_id, self.x_velocity, self.y_velocity)
        
        