import unittest
from src.controller.dijkstra import dijkstra
from src.controller.astar import astar
from src.model.GraphMetrics import getDistance, getElevation, getTotalElevation, getPathDistance
import osmnx as ox

class test_backend(unittest.TestCase):
    G = ox.graph_from_place("Amherst", network_type="drive")
    api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
    G = ox.elevation.add_node_elevations_google(G, api_key, precision=3)
    G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)

    def test_astar(self):
        src_node = 66711889
        dest_node = 66593243
        dis = astar(self.G, src_node, dest_node)
        dis = ' '.join(map(str, dis))
        expected = ox.shortest_path(self.G, src_node, dest_node, weight="length")
        expected = ' '.join(map(str, expected))
        self.assertEqual(dis, expected)

    def test_dijkstra(self):
        src_node = 66711889
        dest_node = 66593243
        dis = dijkstra(self.G, src_node, dest_node)
        dis = ' '.join(map(str, dis))
        expected = ox.shortest_path(self.G, src_node, dest_node, weight="length")
        expected = ' '.join(map(str, expected))
        self.assertEqual(dis, expected)
    
    def test_graph_elevation_value(self):
        self.assertEqual(self.G.nodes[5637885552]['elevation'], 94.449, 'incorrect elevation')
    
    def test_graph_output_value(self):
        self.assertEqual(self.G.nodes[5637885552], {'y': 42.3850694, 'x': -72.5143306, 'elevation': 94.449, 'street_count': 3}, 'incorrect value')

    def test_get_elevation_gain(self):
        self.assertEqual(getElevation(self.G, 66719742, 66745002), 19.355000000000004, 'incorrect n')

    def test_get_distance(self):
        self.assertEqual(getDistance(self.G, 66719742, 66714920), 150.191, 'incorrect length')
    
    def test_get_path_elevation(self):
        self.assertEqual(getTotalElevation(self.G, [66719742, 66678348, 66613427]), 4.747, 'wrong path elevation', )

    def test_get_path_length(self):
        self.assertEqual(getPathDistance(self.G, [66719742, 66678348, 66613427]), 696.191, 'wrong path length', )

if __name__ == '__main__':
    unittest.main()