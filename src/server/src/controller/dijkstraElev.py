import osmnx as ox
import heapq
from model.GraphMetrics import getDistance, getElevation, getPath, getTotalElevation, getPathDistance
import warnings
warnings.filterwarnings('ignore')

# function for calculating route with minimum or maximum elevation using dijkstra within x% of shortest path
def dijkstra_elev(G, start, end, percent, min_distance, max_ele=True):
    percent += 100.0
    possible_paths = {}
    floored_percent = (percent / 10.0) * 10.0
    epochs = []
    i = 100
    while (i <= floored_percent):
        epochs.append(i)
        i += 10

    for epoch in epochs:
        pat_len = float(min_distance) * epoch/100.0
        queue = []
        heapq.heappush(queue, (0, start))
        revPath = {}
        cost = {}
        cost_ele = {}
        revPath[start] = None
        cost[start] = 0
        cost_ele[start] = 0
        while len(queue) != 0:
            (val, cur) = heapq.heappop(queue)
            if cur == end:
                if cost[cur] <= pat_len:
                    break
            for cur, nxt, data in G.edges(cur, data=True):
                cur_cost = cost[cur] + getDistance(G, cur, nxt)
                cur_ecost = cost_ele[cur]
                ecost = getElevation(G, cur, nxt)
                if ecost > 0:
                    cur_ecost = cur_ecost + ecost
                if nxt not in cost or cur_cost < cost[nxt]:
                    cost_ele[nxt] = cur_ecost
                    cost[nxt] = cur_cost
                    if max_ele:
                        priority = -cur_ecost
                    else:
                        priority = cur_ecost
                    heapq.heappush(queue, (priority, nxt))
                    revPath[nxt] = cur
        path = getPath(revPath, start, end)
        possible_paths[getTotalElevation(G, path)] = path

    min_path_len = 10 ** 6
    max_path_len = 0

    for el in possible_paths.keys():
        if el <= min_path_len:
            min_path_len = el
        if el >= max_path_len:
            max_path_len = el

    if max_ele:
        path = possible_paths[max_path_len]
    else:
        path = possible_paths[min_path_len]

    res = {}
    res['path'] = path
    res['elevation'] = str(round(getTotalElevation(G, path), 4))
    res['distance'] = str(round(getPathDistance(G, path), 4))
    return res





