def getElevation(G, src, dest):
    return G.nodes[dest]['elevation'] - G.nodes[src]['elevation']

def getDistance(G, src, dest):
    return G.edges[src, dest, 0]['distance']
