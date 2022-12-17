import osmnx as ox

# get elevation gain between nodes
def getElevation(G, src, dest):
    return G.nodes[src]['elevation'] - G.nodes[dest]['elevation']

# get elevation gain of a path
def getTotalElevation(G, path):
    total_elevation = 0
    for i in range(len(path) - 1):
        curr_elevation = getElevation(G, path[i], path[i + 1])
        if curr_elevation > 0:
            total_elevation += curr_elevation

    return total_elevation

# get path between start and end nodes
def getPath(par, src, dest):
    path = []
    n = dest
    path.append(n)
    while n != src:
        n = par[n]
        path.append(n)
    return path[::-1]

# get total distance for a route
def getPathDistance(G, path):
    total_length = 0
    for i in range(len(path) - 1):
        total_length += getDistance(G, path[i], path[i + 1])
    return total_length

# get distance between two nodes
def getDistance(G, src, dest):
    return G.edges[src, dest, 0]['length']

# get nearest nodes for a node
def get_node(G, point):
    return ox.nearest_nodes(G, float(point[0]), float(point[1]))

# load graph
def get_graph(filename):
    G = ox.load_graphml(filename)
    return G


def convert_linestring(linestring):
    geom = np.array(linestring.coords)
    all_points = []
    for line in geom:
        all_points.append((line[0], line[1]))
    return all_points

# get latitude, longitude for a node
def get_lat_long(G, path):
    coord = []
    for node in path:
        coord.append((G.nodes[node]['y'], G.nodes[node]['x']))
    return coord