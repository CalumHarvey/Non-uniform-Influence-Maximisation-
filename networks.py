"""
File containing code for network structure and a way to read in network data from snap.stanford

"""

import networkx as nx
import pandas as pd
import pickle


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
    """
    Takes a network file and outputs a graph object of the network.
    """

    G = nx.Graph()


    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        edge = line.split()
        G.add_nodes_from([edge[0], edge[1]])
        G.add_edge(edge[0], edge[1])

    print((G.number_of_nodes()), " nodes")
    print(G.number_of_edges(), " edges")

    return G

def readAmazonData():

    with open("networks/Amazon0302.txt") as f:
        amazonGraph = nx.read_edgelist(f)
    
    pickle.dump(amazonGraph, open( "pickles/amazon.pickle", "wb" ))


def readGithubData():

    with open("networks/musae_git_edges.csv") as f:
        next(f, None)
        githubGraph = nx.parse_edgelist(f, delimiter=',', nodetype=int)

    pickle.dump(githubGraph, open( "pickles/github.pickle", "wb" ))


def readArxivData():
    with open("networks/CA-CondMat.txt") as f:
        ArxivGraph = nx.read_edgelist(f)
    
    pickle.dump(ArxivGraph, open( "pickles/arxiv.pickle", "wb" ))



if __name__ == "__main__":
    # readAmazonData()
    # readGithubData()
    readArxivData()
