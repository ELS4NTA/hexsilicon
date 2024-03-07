from hexsilicon.swarm.naturalgroup.ant import AntGroup
import numpy as np


class ACO(AntGroup):

    def update_swarm(self, path, best_path, best_path_length, path_length, pheromone, n_points):
        if path_length < best_path_length:
                best_path = path
                best_path_length = path_length

        pheromone *= self.hyperparams['evaporation_rate']
        for i in range(n_points - 1):
            pheromone[path[i], path[i + 1]] += 1 / path_length
        pheromone[path[-1], path[0]] += 1 / path_length

    def movement_swarm(self, visited, pheromone, path_length, path, points, alpha, beta, current_point):
        while False in visited:
            unvisited = np.where(np.logical_not(visited))[0]
            probabilities = np.zeros(len(unvisited))

            for i, unvisited_point in enumerate(unvisited):
                probabilities[i] = pheromone[current_point, unvisited_point]**alpha / self.distance(points[current_point], points[unvisited_point])**beta

            probabilities /= np.sum(probabilities)

            next_point = np.random.choice(unvisited, p=probabilities)
            path.append(next_point)
            path_length += self.distance(points[current_point], points[next_point])
            visited[next_point] = True
            current_point = next_point