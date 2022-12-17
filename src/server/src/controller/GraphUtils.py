from controller.dijkstraElev import dijkstra_elev
from controller.dijkstra import dijkstra
from controller.astar import astar
import osmnx as ox
from model.GraphMetrics import get_graph, get_node, get_lat_long, getPathDistance
import time

# get shortest path with preferred elevation
def get_shortest_path(src_point, dest_point, percent, flag, filename):
    graph = get_graph(filename)
    src_node = get_node(graph, src_point)
    dest_node = get_node(graph, dest_point)
    min_dis = get_shortest_path_helper(src_point, dest_point, filename)
    if flag == 1:
        max_elevation = True
    else:
        max_elevation = False
    res = dijkstra_elev(graph, src_node, dest_node, percent, min_dis['distance'], max_elevation)
    res['path'] = get_lat_long(graph, res['path'])
    return res

# get shortest path without any elevation
def get_shortest_path_helper(src_point, dest_point, filename):
    graph = get_graph(filename)
    src_node = get_node(graph, src_point)
    dest_node = get_node(graph, dest_point)

    start_dijkstra_time = time.time()
    routes = dijkstra(graph, src_node, dest_node)
    print("Dijkstra Time: ", time.time()-start_dijkstra_time)
    # print("Dijkstra Route: ", routes)
    start_astar_time = time.time()
    routes = astar(graph, src_node, dest_node)
    print("Astar time: ", time.time()-start_astar_time)
    # print("Astar Route: ", routes)
    start_osmnx_time = time.time()
    routes = ox.shortest_path(graph, src_node, dest_node, weight="length")
    print("Osmnx Time: ", time.time()-start_osmnx_time)
    # print("Osmnx Route: ", routes)

    res = {}
    res['distance'] = str(round(getPathDistance(graph, routes), 4))
    res['elevation'] = "Not Applicable"
    path = get_lat_long(graph, routes)
    res['path'] = path

    return res
