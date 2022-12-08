import osmnx as ox
import sys

class Node(object):
    def __init__(self, node, weight, path):
        self.node = node
        self.weight = weight
        self.path = path
   
G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')
def dfs(G, src, dest, visited, length):
    if src == dest:
        return length
    visited.append(src)
    min_dis = float('inf')
    for src, nxt, dic in G.edges(src, data=True):
        if not nxt in visited:
            dis = dfs(G, nxt, dest, visited, dic['length'] + length)
            if dis < float('inf'):
                min_dis = min(min_dis, dis + dic['length'])
    return min_dis


path_len = dfs(G, 1839271812, 668727077,[], 0)
print(path_len)
