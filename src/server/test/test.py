import unittest
from controller.bfs import perform_bfs
from controller.dfs import dfs
from controller.dijkstraElev import dijkstra_elev
from controller.dijkstra import dijkstra
from controller.astar import astar
import osmnx as ox

class test_backend(unittest.TestCase):
    G = ox.graph_from_place("Amherst", network_type="drive")
    api_key = 'AIzaSyBZtVsQkxLlEp63rHfRCA1vXWSEverMKSs'
    G = ox.elevation.add_node_elevations_google(G, api_key, precision=3)
    G = ox.elevation.add_edge_grades(G, add_absolute=True, precision=3)

    def test_bfs(self):
        src_node = 66711889
        dest_node = 66593243
        dis = perform_bfs(G, src_node, dest_node)
        dis = ' '.join(map(str, dis))
        expected = ox.shortest_path(G, src_node, dest_node, weight="length")
        expected = ' '.join(map(str, expected))
        self.assertEqual(dis, expected)

    def test_dfs(self):
        src_node = 66711889
        dest_node = 66593243
        dis = dfs(G, src_node, dest_node)
        dis = ' '.join(map(str, dis))
        expected = ox.shortest_path(G, src_node, dest_node, weight="length")
        expected = ' '.join(map(str, expected))
        self.assertEqual(dis, expected)

    def test_astar(self):
        src_node = 66711889
        dest_node = 66593243
        dis = astar(G, src_node, dest_node)
        dis = ' '.join(map(str, dis))
        expected = ox.shortest_path(G, src_node, dest_node, weight="length")
        expected = ' '.join(map(str, expected))
        self.assertEqual(dis, expected)

    def test_dijkstra(self):
        src_node = 66711889
        dest_node = 66593243
        dis = dijkstra(G, src_node, dest_node)
        dis = ' '.join(map(str, dis))
        expected = ox.shortest_path(G, src_node, dest_node, weight="length")
        expected = ' '.join(map(str, expected))
        self.assertEqual(dis, expected)

if __name__ == '__main__':
    unittest.main()