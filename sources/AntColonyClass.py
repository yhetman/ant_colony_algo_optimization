#!/urs/bin/python
# /* ************************************************************************** */
# /*                                                                            */
# /*                                                                            */
# /*   AntColonyClass.py	                                                      */
# /*                                                                            */
# /*   By: yhetman <hetmanyuliia@gmail.com>                                     */
# /*                                                                            */
# /*   Created: 2021/03/01 12:10:03 by yhetman                                  */
# /*   Updated: 2021/03/03 13:52:09 by yhetman                                  */
# /*                                                                            */
# /* ************************************************************************** */
import random as rn
import numpy as np
from numpy.random import choice as np_choice

class AntColonyClass():
    def __init__(self, distances, n_ants, n_elite_ants, n_iterations, decay, alpha=1, beta=1):
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_elite_ants = n_elite_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.generate_all_paths()
            self.spread_pheromone(all_paths, self.n_elite_ants, shortest_path=shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone = self.pheromone * self.decay            
        return all_time_shortest_path


    def spread_pheromone(self, all_paths, n_elite_ants, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_elite_ants]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]


    def get_path_distances(self, path):
        total_distance = 0
        for edge in path:
            total_distance += self.distances[edge]
        return total_distance


    def generate_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.generate_path(0)
            all_paths.append((path, self.get_path_distances(path)))
        return all_paths


    def generate_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.make_a_choice(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start))  
        return path


    def make_a_choice(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0
        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)
        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move


