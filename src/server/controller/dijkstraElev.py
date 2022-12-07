import osmnx as ox
import heapq
import GraphUtils as gu
from dijkstra import dijkstra
import warnings
warnings.filterwarnings('ignore')

# G = ox.graph_from_place('Amherst', network_type='drive')
# api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
# G = ox.elevation.add_node_elevations_google(G, api_key, precision=3)
# G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)

# def dijkstra_elev(G, start, target, percent_dis, max_elevation = True):
#     min_dis = gu.getPathDistance(G, ox.shortest_path(G, start, target, weight="length"))
#     # _, min_dis = dijkstra(G, start, target)
#     print("min_dis ", min_dis)
#     epochs = []
#     possible_paths = {}
#     epochs = [ 1 + i/100 for i in range(0, percent_dis+1, 10)]
#     for epoch in epochs:
#         print('epoch ', epoch)
#         max_dis = min_dis * epoch
#         pq = []
#         heapq.heappush(pq, (0, start))
#         path = {}
#         cost_dis = {}
#         cost_elev = {}
#         path[start] = None
#         cost_dis[start] = 0
#         cost_elev[start] = 0
#         while len(pq)!=0:
#             (curr_dis, curr_node) = heapq.heappop(pq)
#             if(curr_node == target):
#                 if cost_dis[curr_node] <= max_dis:
#                     break
#                     # return (cost_dis[curr_node], cost_elev[curr_node], path)
#             for u, next, data in G.edges(curr_node, data=True):
#                 new_dis = cost_dis[curr_node] + gu.getDistance(G, curr_node, next)
#                 elev = gu.getElevation(G, curr_node, next)
#                 if elev > 0:
#                     # print(curr_node, cost_elev[curr_node])
#                     new_elev = elev + cost_elev[curr_node]
#                 if next not in cost_dis or  new_dis < cost_dis[next]:
#                     cost_dis[next] = new_dis
#                     cost_elev[next] = new_elev
#                     if(max_elevation):
#                         new_elev = -new_elev
#                     heapq.heappush(pq, (new_elev, next))
#                     path[next] = curr_node
#         path = gu.getPath(path, start, target)
#         possible_paths[gu.getTotalElevation(G, path)] = path
    
#     if max_elevation:
#         res_path = possible_paths[max(possible_paths.keys())]
#         res_elev = max(possible_paths.keys())
#     else:
#         res_path = possible_paths[min(possible_paths.keys())]
#         res_elev = min(possible_paths.keys())

#     return res_path, res_elev, gu.getPathDistance(G, res_path)

def dijkstra_elev(G, start, end, percent, min_dis, max_ele=True):
    # min_distance = gu.getPathDistance(G, route)
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

    res = {}
    res['path'] = path
    res['elevation'] = str(gu.getTotalElevation(G, path))
    res['distance'] = str(gu.getPathDistance(G, path))
    return res

# src = gu.get_node(G, (-72.5279153, 42.3497246))
# dest = gu.get_node(G, (-72.51976, 42.374569))
# # print(dijkstra_elev(G, src, dest, 20, True))
# print(get_from_djikstra(G, src, dest, 20, True))





