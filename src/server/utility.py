import osmnx as ox

def save_graph(place, filename):
    G = ox.graph_from_place(place, network_type="drive")
    api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
    G = ox.elevation.add_node_elevations(G, api_key, precision=3)
    G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)
    ox.save_graphml(G, filename)

if __name__ == "__main__":
    filepath = "./data/amherst.graphml"
    save_graph("Amherst, MA, USA", filepath)