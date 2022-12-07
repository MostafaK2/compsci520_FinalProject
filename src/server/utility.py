import osmnx as ox

def save_graph(place, filename):
    G = ox.graph_from_place(place, network_type="drive")
    api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
    G = ox.elevation.add_node_elevations(G, api_key, precision=3)
    G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)
    ox.save_graphml(G, filename)
    with open("./data/allgraphs.txt", "a") as myfile:
        myfile.write("\n" + filename)


def check_graph_present(filename):
    with open("./data/allgraphs.txt") as f:
        lines = f.readlines()
        if(filename in lines):
            return True
    return False