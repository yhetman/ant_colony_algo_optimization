#!/home/yhetman/anaconda3/bin/python
# /* ************************************************************************** */
# /*                                                                            */
# /*                                                                            */
# /*   main.py                                                                  */
# /*                                                                            */
# /*   By: yhetman <hetmanyuliia@gmail.com>                                     */
# /*                                                                            */
# /*   Created: 2021/03/02 22:05:50 by yhetman                                  */
# /*   Updated: 2021/03/03 13:32:04 by yhetman                                  */
# /*                                                                            */
# /* ************************************************************************** */
from datetime import datetime
import numpy as np
import networkx as nx
from AntColonyClass import AntColonyClass
import matplotlib.pyplot as plt
import seaborn as sns
from big_matrix import generate_big_matrix

## SETTING VARIABLES

n_ants = 1            # Number of ants running per iteration
n_elite_ants = 1      # Number of best ants who deposit pheromone
n_iterations = 100     # Number of iterations
p_decay = 0.9          # Rate how much pheromone decays
alpha = 1              # exponenet on pheromone
beta = 1               # exponent on distance


## DISTANCE MATRIX -- (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.


distances = generate_big_matrix(20) # generator of bigger matrix
# distances = np.array([[np.inf, 2, 2, 5, 7, 1, 1],
#                       [2, np.inf, 4, 8, 2, 1, 9],
#                       [2, 4, np.inf, 1, 3, 3, 4],
#                       [5, 8, 1, np.inf, 2, 5, 8],
#                       [7, 2, 3, 2, np.inf, 9, 1],
#                       [1, 1, 1, 1, 1, np.inf, 22],
#                       [5, 3, 6, 8, 3, 7, np.inf]])


## GO ANTS GO

ant_colony = AntColonyClass(distances,
                        n_ants,
                        n_elite_ants,
                        n_iterations,
                        p_decay,
                        alpha = alpha,    # default=1
                        beta = beta)      # default=1


shortest_path = ant_colony.run()
nodes, length = shortest_path

print ("Optimal path: {}".format(shortest_path))

## VISUALIZING GRAPH

data2 = np.asmatrix(distances)
rows, cols = np.where(data2 < np.inf)
data = distances

plt.rcParams["figure.figsize"] = (50,50)

G = nx.Graph()

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] < np.inf:
			G.add_edge(i, j,
        weight = data[i][j],
        color = 'orange')

for i in nodes:
  G.edges[i[0],i[1]]['color'] = 'blue'

edges = G.edges()
colors = [G[u][v]['color'] for u,v in edges]
weights = nx.get_edge_attributes(G,'weight')
pos=nx.spring_layout(G)

nx.draw_networkx_edge_labels(G,
  pos,
  edge_labels = weights)
nx.draw(G, pos,
  font_size = 8,
  font_weight = "bold",
  node_size = 600,
  with_labels = True,
  edgecolors = 'yellow',
  edge_color = colors,
  node_color = 'orchid')


now = str(datetime.now())
# plt.show()
plt.savefig("../pngs/graph_pic" + now + ".png")
print("Graph was saved to pngs folder.")