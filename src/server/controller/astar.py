
import osmnx as ox
from heapq import *

G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')

def astar(G, src, dest):
    queue = [(0, src, 0, None)]
    visited = {}
    open_list = {}
    while queue:
        _, node, dist, parent = heappop(queue)
        if node == dest:
            path = [node]
            node = parent
            while node:
                path.append(node)
                node = visited[node]
            path.reverse()
            return path, dist

        elif not node in visited:
            visited[node] = parent

            for neighbor, dic in G[node].items():
                if not neighbor in visited:
                    new_cost = dist + dic[0]['length']
                    if neighbor in open_list:
                       old_cost, h = open_list[neighbor] 
                       if old_cost <= new_cost:
                            continue
                    else:
                        y1 = G.nodes[dest]['y']
                        x1 = G.nodes[dest]['x']
                        y2 = G.nodes[node]['y']
                        x2 = G.nodes[node]['x']
                        h = ox.distance.euclidean_dist_vec(y1, x1, y2, x2)
                    open_list[neighbor] = new_cost, h
                    heappush(queue, (new_cost + h, neighbor, new_cost, node))

path, path_len = astar(G, 1839271812, 668727077)
print(path, path_len)
print(ox.distance.shortest_path(G, 1839271812, 668727077, weight='length'))

                        




