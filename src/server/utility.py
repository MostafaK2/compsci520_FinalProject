import osmnx as ox
import csv

def save_graph(place, filename):
    G = ox.graph_from_place(place, network_type="drive")
    ox.save_graphml(G, filename)
    with open("./data/allgraphs.csv", "a") as myfile:
        writer_object = csv.writer(myfile)
        writer_object.writerow([filename])
        myfile.close()



def check_graph_present(filename):
    print(filename)
    with open("./data/allgraphs.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if(row == [filename]):
                return True
    return False