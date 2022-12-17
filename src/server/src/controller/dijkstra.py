import osmnx as ox
import heapq

class Pair(object):
    def __init__(self, node, weight, path):
        self.node = node
        self.weight = weight
        self.path = path

    def __lt__(self, other):
        return self.weight < other.weight

# function for dijkstra algorithm
def dijkstra(G, src, dest):
    visited = set()
    new = Pair(src, 0, str(src))
    pq = []
    heapq.heappush(pq, new)
    visited = set()
    path = []
    while len(pq) != 0:
        object = heapq.heappop(pq)
        if object.node == dest:
            all_ids = object.path.split()
            path = [int(id) for id in all_ids]
            break
        if object.node in visited:
            continue
        visited.add(object.node)
        for src, next, length in G.edges(object.node, data=True):
            if next not in visited:
                newObject = Pair(next, length['length'] + object.weight, object.path + " " + str(next))
                heapq.heappush(pq, newObject)

    return path
