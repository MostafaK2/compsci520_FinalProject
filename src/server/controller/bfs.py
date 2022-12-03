import osmnx as ox
import heapq

G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')

print("Shortest Paths Using In-Built Libraries")
print(next(ox.k_shortest_paths(G, 1839271812, 668727077, 1, weight='length')))

def bfs(G, src, dest):
    parent = {}
    visited = set()
    queue = [src]
    path = ""
    while len(queue) != 0:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        path += " " + str(node)
        if node == dest:
            print("found destination")
            print(parent)
            printPath(parent, src, dest, "")
            break
        for curr, next, length in G.edges(node, data=True):
            print("curr", curr)
            print("next", next)
            print("length", length)
            if next not in visited:
                parent[curr] = next
                queue.append(next)

bfs(G, 1839271812, 668727077)
