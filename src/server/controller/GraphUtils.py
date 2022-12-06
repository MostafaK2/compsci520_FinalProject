from controller.bfs import perform_bfs
import osmnx as ox
import networkx as nx
import numpy as np
import taxicab as tc

def getElevation(G, src, dest):
    return G.nodes[dest]['elevation'] - G.nodes[src]['elevation']

def getDistance(G, src, dest):
    return G.edges[src, dest, 0]['distance']

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

def get_shortest_path(src_point, dest_point):
    # print(src, dest)
    graph = get_graph("./data/amherst.graphml")
    src_node = get_node(graph, src_point)
    dest_node = get_node(graph, dest_point)
    details = nx.to_dict_of_dicts(graph)
    route = ox.shortest_path(graph, src_node, dest_node, weight="length")
    # print(route)
    routes = perform_bfs(graph, src_node, dest_node, 'travel_time')
    # print(routes)
    path = []
    for point in routes:
        for key in details[point].keys():
            for index in details[point][key]:
                my_dict = details[point][key][index]
                if 'geometry' in my_dict.keys():
                    my_dict['geometry'] = convert_linestring(my_dict['geometry'])
                path.append(my_dict)
    return path
