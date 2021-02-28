"""
File containing code for network structure and a way to read in network data from snap.stanford

"""

class Graph:
    """
    Graph object
    """

    def __init__(self):
        self.nodes = set()
        self.edges = []
    
    def addNode(self, name):
        
        self.nodes.add(name)
    
    def addEdge(self, first, second):

        self.addNode(first)
        self.addNode(second)
        
        self.edges.append((first, second))



def readFile(filename):
    graph = Graph()
    """
    Takes a network file and outputs a graph object of the network.
    """

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        edge = line.split()
        graph.addEdge(edge[0], edge[1])

    print(len(graph.nodes), " nodes")
    print(len(graph.edges), " edges")

    return graph


readFile("networks/web-Stanford.txt")

