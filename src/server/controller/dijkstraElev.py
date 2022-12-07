import osmnx as ox
import heapq
import controller.GraphUtils as gu
import warnings
warnings.filterwarnings('ignore')

def get_from_djikstra(G, start, end, percent, route, max_ele=True):
    min_distance = gu.getPathDistance(G, route)
    print("min_dis ", min_distance)
    percent += 100
    max_path_length = min_distance * (percent/100)
    possible_paths = {}
    floored_percent = (percent / 10) * 10
    iters = []
    i = 100
    while (i <= floored_percent):
        iters.append(i)
        i += 10
        # print(i)

    for epoch in epochs:
        pat_len = min_distance * epoch/100
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
                cur_cost = cost[cur] + gu.getDistance(G, cur, nxt)
                cur_ecost = cost_ele[cur]
                ecost = gu.getElevation(G, cur, nxt)
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
        path = gu.getPath(revPath, start, end)
        print(gu.getTotalElevation(G, path))
        possible_paths[gu.getTotalElevation(G, path)] = path

    # print(possible_paths.keys())

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

    return path, gu.getPathDistance(G, path), gu.getTotalElevation(G, path)





