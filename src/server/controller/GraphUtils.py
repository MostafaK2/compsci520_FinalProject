from controller.bfs import perform_bfs
from controller.dijkstraElev import dijkstra_elev
from controller.dijkstra import dijkstra
from controller.astar import astar
import osmnx as ox
import networkx as nx
import numpy as np
from geopy.geocoders import Nominatim
import time

def getElevation(G, src, dest):
    return G.nodes[src]['elevation'] - G.nodes[dest]['elevation']

def getTotalElevation(G, path):
    total_elevation = 0
    for i in range(len(path) - 1):
        curr_elevation = getElevation(G, path[i], path[i + 1])
        if curr_elevation > 0:
            total_elevation += curr_elevation

    return total_elevation

def getPath(par, src, dest):
    path = []
    n = dest
    path.append(n)
    while n != src:
        n = par[n]
        path.append(n)
    return path[::-1]

def getPathDistance(G, path):
    total_length = 0
    for i in range(len(path) - 1):
        total_length += getDistance(G, path[i], path[i + 1])
    return total_length

def getDistance(G, src, dest):
    return G.edges[src, dest, 0]['length']

def get_node(G, point):
    return ox.nearest_nodes(G, float(point[0]), float(point[1]))

def get_graph(filename):
    G = ox.load_graphml(filename)
    return G

def convert_linestring(linestring):
    geom = np.array(linestring.coords)
    all_points = []
    for line in geom:
            all_points.append((line[0], line[1]))
    return all_points

def get_lat_long(G, path):
    coord = []
    for node in path:
        coord.append((G.nodes[node]['y'], G.nodes[node]['x']))
    return coord

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

def get_shortest_path_helper(src_point, dest_point, filename):
    graph = get_graph(filename)
    src_node = get_node(graph, src_point)
    dest_node = get_node(graph, dest_point)

    start_bfs_time = time.time()
    routes = perform_bfs(graph, src_node, dest_node)
    print("Bfs Time: ", time.time()-start_bfs_time)
    print("Bfs Route: ", routes)
    start_dijkstra_time = time.time()
    routes = dijkstra(graph, src_node, dest_node)
    print("Dijkstra Time: ", time.time()-start_dijkstra_time)
    print("Dijkstra Route: ", routes)
    start_astar_time = time.time()
    routes, dist = astar(graph, src_node, dest_node)
    print("Astar time: ", time.time()-start_astar_time)
    print("Astar Route: ", routes)
    start_osmnx_time = time.time()
    routes = ox.shortest_path(graph, src_node, dest_node, weight="length")
    print("Osmnx Time: ", time.time()-start_osmnx_time)
    print("Osmnx Route: ", routes)

    res = {}
    res['distance'] = str(round(getPathDistance(graph, routes), 4))
    res['elevation'] = "Not Applicable"
    path = get_lat_long(graph, routes)
    res['path'] = path

    return res

def get_details(src_point, dest_point):
    geolocator = Nominatim(user_agent="EleNa-server")
    location_src = geolocator.reverse(str(src_point[1]) + ", " + str(src_point[0]))
    location_dest = geolocator.reverse(str(dest_point[1]) + ", " + str(dest_point[0]))
    src_country = location_src.raw['address']['country']
    dest_country = location_dest.raw['address']['country']
    src_state = location_src.raw['address']['state']
    dest_state = location_dest.raw['address']['state']
    if("town" in location_src.raw['address'].keys()):
        src_city = location_src.raw['address']['town']
    else:
        src_city = location_src.raw['address']['city']
    
    if("town" in location_dest.raw['address'].keys()):
        dest_city = location_dest.raw['address']['town']
    else:
        dest_city = location_dest.raw['address']['city']

    if(src_country != dest_country or src_state != dest_state or src_city != dest_city):
        return "", "", ""
    else:
        return src_city, src_state, src_country
            

