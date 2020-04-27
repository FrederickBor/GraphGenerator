#!/usr/bin/python3

from random import randint
import os
import sys
import getopt

class ErrorExistingEdge(Exception):
    """Custom exception class"""
    pass

class Graph(object):
    """This class helps to create a graph file with a 
    specific size and number of edges per node."""
    
    def __init__(self, size, edges):
        """Constructor of the class.

        Parameters:
        size (int): Number of nodes of the graph.
        edges (int): Number of edges per node.

        Returns:
        Graph: Graph with the size and edges specified.
        """
        self.__nodes = []
        self.__size = size
        self.__edges = edges

        self.__generateNodes()
        self.__generateEdges()
        self.__generateGraphFile()

    def __generateNodes(self):
        i = 0
        while i < self.__size:
            self.__nodes.append(Graph.Node(i))
            i += 1

    def __generateEdges(self):
        for node in self.__nodes:
            while node.getNumberEdges() < self.__edges:
                nodekey = randint(0,self.__size-1)
                try:
                    node.addEdge(nodekey)
                except ErrorExistingEdge:
                    pass

    def getNodes(self):
        return self.__nodes
    
    def getSize(self):
        return self.__size
    
    def getNumEdges(self):
        return self.__edges

    def __generateGraphFile(self):
        filename = "graph{}_{}.in".format(self.__size, self.__edges)
        
        if not os.path.isdir("graphs"):
            os.mkdir("graphs")

        with open("graphs/"+filename, "w") as file:
            file.write(self.__str__())
        

    def __str__(self):
        str = "bidirectional=false\nsource;destination;cost\n"
        for node in self.__nodes:
            str += node.__str__()
        return str

    class Node(object):
        
        def __init__(self, key):
            self.__key = key
            self.__edges = {}

        def getKey(self):
            return self.__key

        def addEdge(self, nodeKey):
            if nodeKey in self.__edges.keys():
                raise ErrorExistingEdge
        
            self.__edges[nodeKey] = randint(1,50)

        def getEdges(self):
            return self.__edges
        
        def getNumberEdges(self):
            return len(self.__edges)

        def __str__(self):
            str = ""
            for edge, value in self.__edges.items():                
                str += "{SRC};{DST};{COST}\n".format(SRC = self.__key, DST = edge,COST = value)
            return str


if __name__ == "__main__":
    size = 0
    edges = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hs:e:",["size=","edges="])
    except getopt.GetoptError:
        print('GraphGenerator.py -s <size> -e <edges>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('GraphGenerator.py -s <size> -e <edges>')
            sys.exit()
        elif opt in ("-s", "--size"):
            size = int(arg)
        elif opt in ("-e", "--edges"):
            edges = int(arg)

    if size != 0 and edges != 0:
        g = Graph(size, edges)