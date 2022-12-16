class Pair(object):
    def __init__(self, node, weight, path):
        self.node = node
        self.weight = weight
        self.path = path

    def __lt__(self, other):
        return self.weight < other.weight