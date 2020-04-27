import unittest
from GraphGenerator import Graph

class Tests(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(10,4)

    def test_checkNodesLength(self):
        self.assertEqual(len(self.graph.getNodes()), self.graph.getSize())

    def test_checkNodesEdgesCount(self):
        nodes = self.graph.getNodes()
        for node in nodes:
            self.assertEqual(node.getNumberEdges(),4)

    def tearDown(self):
        del(self.graph)

if __name__ == "__main__":
    unittest.main()