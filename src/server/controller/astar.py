
import osmnx as ox
from heapq import *
import warnings
warnings.filterwarnings('ignore')

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
    return [], 0.0

                        




