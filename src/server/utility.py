import osmnx as ox

def save_graph(place, filename):
    G = ox.graph_from_place(place, network_type="drive")
    ox.save_graphml(G, filename)

if __name__ == "__main__":
    filepath = "./data/amherst.graphml"
    save_graph("Amherst, MA, USA", filepath)