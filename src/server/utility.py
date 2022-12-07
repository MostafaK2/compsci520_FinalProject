import osmnx as ox

def save_graph(place, filename):
    G = ox.graph_from_place(place, network_type="drive")
    ox.save_graphml(G, filename)
    with open("./data/allgraphs.txt", "a") as myfile:
        myfile.write("\n" + filename)


def check_graph_present(filename):
    with open("./data/allgraphs.txt") as f:
        lines = f.readlines()
        if(filename in lines):
            return True
    return False