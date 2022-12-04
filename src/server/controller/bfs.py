import osmnx as ox
from queue import Queue

# G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')

# print("Shortest Paths Using In-Built Libraries")
# print(next(ox.k_shortest_paths(G, 1839271812, 668727077, 1, weight='length')))
def perform_bfs(G, src, dest):
    parent = dict()
    visited = set()
    queue = Queue()
    queue.put(src)
    visited.add(src)
    parent[src] = None
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == dest:
            path_found = True
            print("path found")
            break
        for (curr, next, length) in G.edges(current_node, data=True):
            if next not in visited:
                queue.put(next)
                parent[next] = current_node
                visited.add(next)
            
    path = []
    if path_found:
        path.append(dest)
        while parent[dest] is not None:
            path.append(parent[dest]) 
            dest = parent[dest]
        path.reverse()
    return path
# bfs(G, 1839271812, 668727077)