import osmnx as ox
import heapq

class Pair(object):
    def __init__(self, node, weight, visited, path):
        self.node = node
        self.weight = weight
        self.visited = visited
        self.path = path

    def __lt__(self, other):
        return self.weight < other.weight

G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')

print("Shortest Paths Using In-Built Libraries")
print(next(ox.k_shortest_paths(G, 1839271812, 668727077, 5, weight = 'length')))

def dijkstra(G, src, dest):
    visited = set()
    new = Pair(src, 0, False, str(src))
    pq = []
    heapq.heappush(pq, new)
    while len(pq) != 0:
        object = heapq.heappop(pq)
        print("path print check ",object.path)
        if object.node == dest:
        print("found destination")
        print("path", object.path)
        break
        if object.visited == True:
        continue
        object.visited = True
        for src, next, length in G.edges(object.node, data=True):
            print(length['length'])
            newObject = Pair(next, length['length'] + object.weight, False, object.path + " " + str(next))
            heapq.heappush(pq, newObject)

dijkstra(G, 1839271812, 668727077)
