import osmnx as ox
import csv

# wrtie graph for the place
def save_graph(place, filename):
    G = ox.graph_from_place(place, network_type="drive")
    api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
    G = ox.elevation.add_node_elevations_google(G, api_key, precision=3)
    G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)
    ox.save_graphml(G, filename)
    with open("../data/allgraphs.csv", "a") as myfile:
        writer_object = csv.writer(myfile)
        writer_object.writerow([filename])
        myfile.close()

def check_graph_present(filename):
    print(filename)
    with open("../data/allgraphs.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if(row == [filename]):
                return True
    return False