import osmnx as ox
import sys

G = ox.graph_from_place('Sutherland Shire Council', network_type='drive')
def dfs(G, src, dest, visited):
    if src == dest:
        return 0
    visited.append(src)
    min_dis = float('inf')
    for src, nxt, dic in G.edges(1839271812, data=True):
        if not nxt in visited:
            dis = dfs(G, nxt, dest, visited)
            print(dis)
            if dis < float('inf'):
                min_dis = min(min_dis, dis + dic[length])

    if src in visited: visited.remove(src)
    return min_dis


path_len = dfs(G, 1839271812, 668727077,[])
print(path_len)
