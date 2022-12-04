from controller.bfs import perform_bfs
import osmnx as ox
import networkx as nx
import numpy as np

def getElevation(G, src, dest):
    return G.nodes[dest]['elevation'] - G.nodes[src]['elevation']

def getDistance(G, src, dest):
    return G.edges[src, dest, 0]['distance']

def get_node(G, point):
    return ox.nearest_nodes(G, float(point[0]), float(point[1]))

def get_shortest_path(src_point, dest_point):
    # print(src, dest)
    G = ox.graph_from_point((float(src_point[0]), float(src_point[1])), dist=1000, network_type="drive")
    H = ox.graph_from_point((float(dest_point[0]), float(dest_point[1])), dist=1000, network_type="drive")
    graph = nx.compose(G, H)
    src_node = get_node(G, src_point)
    dest_node = get_node(G, dest_point)
    details = nx.to_dict_of_dicts(graph)
    # print(details)
    routes = nx.shortest_path(graph, src_node, dest_node, 'travel_time')
    # for point in routes:
    #     for key in details[point].keys():
    #         for index in details[point][key]:
    #             print(details[point][key][index]['geometry'])
    # print(details)
    # # route_map = ox.plot_route_folium(G, route)
    # # route_map.save('test.html')
    # path = perform_bfs(graph, int(src), int(dest))
    path = []
    for point in routes:
        for key in details[point].keys():
            for index in details[point][key]:
                my_dict = details[point][key][index]
                geom = np.array(my_dict['geometry'].coords)
                # print(geom)
                all_points = []
                for line in geom:
                    all_points.append((line[0], line[1]))
                # details[point][key][index]['geometry'] = np.array(geom)
                my_dict['geometry'] = all_points
                path.append(my_dict)
    return path
    
