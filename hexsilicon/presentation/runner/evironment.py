import time

import networkx as nx
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from sklearn.decomposition import PCA
from ttkbootstrap.constants import *

from hexsilicon.presentation.runner.observer import Observer
from hexsilicon.swarms.swarm import Swarm


class Environment(Observer, ttk.Labelframe):

    def __init__(self, master=None):
        super().__init__(master)
        self.create_widgets()
        self.configure(text="Ambiente")
        self.image_ids = {}
        self.will_update = True
        self.first_time = True
        self.speed_factor = 5
        self.current_point_index = 0
        self.x_velocity = self.y_velocity = 0
        self.reducer = PCA(n_components=2)
        self.photo = None

    def create_widgets(self):

        self.show_btn = ttk.Button(self, text="Ocultar", bootstyle="primary", command=self.toggle_frame)  # type: ignore
        self.show_btn.pack()

        # Crear un canvas para la imagen
        self.canvas = ttk.Canvas(self, width=700, height=500)
        self.canvas.pack(expand=YES, fill=BOTH)

    def toggle_frame(self):
        if self.canvas.winfo_ismapped():
            self.canvas.pack_forget()
            self.will_update = False
            self.show_btn.config(text="Mostrar")
        else:
            self.canvas.pack(expand=YES, fill=BOTH)
            self.will_update = True
            self.show_btn.config(text="Ocultar")

    def update(self, swarm: Swarm):
        if not self.photo:
            image = Image.open(f"icons/{swarm.population[0].name}.png")
            image = image.resize((24, 24))
            self.photo = ImageTk.PhotoImage(image)
        if self.will_update:
            representation = swarm.to_2d()
            if not swarm.has_free_problem():
                if self.first_time:
                    self.first_time = False
                    pos = nx.spring_layout(representation)
                    self.points = self.get_points(pos)
                    for key, point in self.points.items():
                        self.canvas.create_oval(point[0], point[1], point[0] + 5, point[1] + 5, fill="red")
                        self.canvas.create_text(point[0], point[1], anchor="nw", text=str(key))
            else:
                X_2d = self.reducer.fit_transform(representation)
                pos = {i: tuple(X_2d[i]) for i in range(len(X_2d))}
                self.points = self.get_points(pos)

            # Draw the agents and do the movement
            for i, agent in enumerate(swarm.population):
                passed_points = self.get_points_solution(swarm.get_passed_points_agent(i)) if not swarm.has_free_problem() else [self.points[i]]
                if agent not in self.image_ids:
                    self.image_ids[agent] = self.canvas.create_image(passed_points[0][0], passed_points[0][1], image=self.photo)
                image_id = self.image_ids[agent]
                if len(passed_points) == 1:
                    passed_points = [self.canvas.coords(image_id)] + passed_points
                self.canvas.coords(image_id, passed_points[0][0], passed_points[0][1])
                self.move(image_id, passed_points)

    def normalize(self, value, min_value, max_value, new_min, new_max):
        return ((value - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min

    def get_points(self, pos):
        # Encontrar los valores mínimos y máximos de las posiciones
        self.min_x = min(pos.values(), key=lambda x: x[0])[0]
        self.max_x = max(pos.values(), key=lambda x: x[0])[0]
        self.min_y = min(pos.values(), key=lambda x: x[1])[1]
        self.max_y = max(pos.values(), key=lambda x: x[1])[1]

        for key in pos:
            x = self.normalize(pos[key][0], self.min_x, self.max_x, 50, self.canvas.winfo_width()-50)
            y = self.normalize(pos[key][1], self.min_y, self.max_y, 50, self.canvas.winfo_height()-50)
            pos[key] = (x, y)
        return pos

    def get_points_solution(self, solution):
        path_positions = [tuple(self.points[i]) for i in solution if i in self.points]
        return path_positions

    def move(self, image_id, points, idx=0):
        if idx < len(points):
            current_coords = self.canvas.coords(image_id)
            target_point = points[idx]
            dx = (target_point[0] - current_coords[0]) / self.speed_factor
            dy = (target_point[1] - current_coords[1]) / self.speed_factor
            for _ in range(self.speed_factor):
                self.canvas.move(image_id, dx, dy)
                self.canvas.update()
                time.sleep(0.01)
            self.move(image_id, points, idx + 1)
