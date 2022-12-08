import osmnx as ox
from queue import Queue

class Node(object):
    def __init__(self, node, weight, path):
        self.node = node
        self.weight = weight
        self.path = path

# print("Shortest Paths Using In-Built Libraries")
# print(next(ox.k_shortest_paths(G, 1839271812, 668727077, 1, weight='length')))
def perform_bfs(G, src, dest):
    parent = dict()
    visited = set()
    queue = Queue()
    srcObject = Node(src, 0, str(src))
    queue.put(srcObject)
    visited.add(src)
    parent[src] = None
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node.node == dest:
            path_found = True
            # print("path found")
            # print("length", current_node.weight)
            break
        for curr, next, length in G.edges(current_node.node, data=True):
            if next not in visited:
                neighborObject = Node(next, length['length'] + current_node.weight, current_node.path + " " + str(next))
                queue.put(neighborObject)
                parent[next] = curr
                visited.add(next)
           
    path = []
    if path_found:
        path.append(dest)
        while parent[dest] is not None:
            path.append(parent[dest])
            dest = parent[dest]
        path.reverse()
    return path

