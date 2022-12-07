import osmnx as ox
import heapq
import GraphUtils as gu
from dijkstra import dijkstra
import warnings
warnings.filterwarnings('ignore')

G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')
api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
G = ox.elevation.add_node_elevations(G, api_key, precision=3)
G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)

def dijkstra(G, start, target, percent_dis, max_elevation = True):
    pq = []
    min_dis = dijkstra(G, start, target)
    heappush(pq, (0, start))
    epochs = []
    possible_paths = {}
    epochs = [ 1 + i/100 for i in range(0, percent_dis+1, 10)]
    for epoch in epochs:
        max_dis = min_dis * epoch
        path = {}
        cost_dis = {}
        cost_elev = {}
        path[start] = None
        cost_dis[start] = 0
        cost_elev[start] = 0
        while len(pq)!=0:
            (curr_dis, curr_node) = heappop(pq)
            if(curr_node == target):
                if cost_dis[curr_node] <= max_dis:
                    break
                    # return (cost_dis[curr_node], cost_elev[curr_node], path)
            for u, next, data in G.edges(curr_node, data=True):
                new_dis = cost_dis[curr_node] + gu.getDistance(G, curr_node, next)
                elev = gu.getElevation(curr_node, next)
                if elev > 0:
                    new_elev = elev + cost_elev[curr_node]
                if next not in cost_dis or  new_dis < cost_dis[next]:
                    cost_dis[next] = new_dis
                    cost_elev[next] = new_elev
                    if(max_elevation):
                        new_elev = -new_elev
                    heapush(pq, (new_elev, next))
                    path[next] = curr_node
        path = gu.getPath(path, start, target)
        possible_paths[gu.getTotalElevation(G, path)] = path
    
    if max_elevation:
        path = candidate_paths[max(candidate_paths.keys())]
    else:
        path = candidate_paths[min(candidate_paths.keys())]

    return path

src = gu.get_node(G, (-72.5279153, 42.3497246))
dest = gu.get_node(G, (-72.51976, 42.374569))
print(dijkstra(G, src, dest, 0, True))





