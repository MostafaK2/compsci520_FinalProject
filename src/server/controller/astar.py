
import osmnx as ox
from heapq import *
import warnings
warnings.filterwarnings('ignore')

G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')
api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
G = ox.elevation.add_node_elevations(G, api_key, precision=3)
G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)
# G_proj = ox.project_graph(G)
print(G.nodes[1839271812])

def compute_elevation(G, src, dest):
    if src == dest:
        return 0
    
    return G.nodes[src]['elevation'] - G.nodes[dest]['elevation']

def astar(G, src, dest, min_elev = None):
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
                        if min_elev is None:
                            y1 = G.nodes[dest]['y']
                            x1 = G.nodes[dest]['x']
                            y2 = G.nodes[neighbor]['y']
                            x2 = G.nodes[neighbor]['x']
                            h = ox.distance.euclidean_dist_vec(y1, x1, y2, x2)
                        elif min_elev:
                            h = compute_elevation(G, neighbor, dest)
                        else:
                            h = compute_elevation(G, neighbor, dest)

                    open_list[neighbor] = new_cost, h
                    heappush(queue, (new_cost + h, neighbor, new_cost, node))

path, path_len = astar(G, 1839271812, 668727077, True)
print(path, path_len)
print(ox.distance.shortest_path(G, 1839271812, 668727077, weight='length'))

                        




