from random import randint
import networkx as nx
from DiffusionModels import loadAmazon, loadGithub, loadArxiv
import numpy as np
import pickle


def random(graph):
    """
    Input: 
    graph: networkX graph object

    Costs each node with random integer between 1 and 9
    """
    labels = {}

    for node in graph.nodes:
        labels[node] = randint(1,9)

    return labels


def degree(graph):
    """
    Input: 
    graph: networkX graph object

    Costs each node using the degree of the node
    """
    labels = {}

    for node in graph.nodes:
        labels[node] = len([n for n in graph.neighbors(node)])
    
    return labels


def pageRank(graph):
    """
    Input: 
    graph: networkX graph object

    Uses NetworkX pagerank function to cost nodes
    """
    return nx.pagerank(graph)

def writeCosts(graph, name):
    """
    Input: 
    graph: networkX graph object
    name: string name of graph

    Writes costs to file for the defined network
    """

    with open("costs/" + name + "/random.p", "wb") as fp:
        pickle.dump(random(graph), fp, protocol=pickle.HIGHEST_PROTOCOL)

    with open("costs/" + name + "/degree.p", "wb") as fp:
        pickle.dump(degree(graph), fp, protocol=pickle.HIGHEST_PROTOCOL)

    with open("costs/" + name + "/pagerank.p", "wb") as fp:
        pickle.dump(pageRank(graph), fp, protocol=pickle.HIGHEST_PROTOCOL)


def writeAllCosts():
    """
    Writes costs for all three networks to file
    """

    networkNames = ["amazon", "github", "arxiv"]
    networks = np.array([loadAmazon, loadGithub, loadArxiv])

    for x in range(len(networks)):

        writeCosts(networks[x](), networkNames[x])


def averageCalculations():
    costs = []
    networks = ["amazon", "github", "arxiv"]
    
    for network in networks:
        with open("costs/" + network + "/pagerank.p", "rb") as fp:
            data = pickle.load(fp)
        
        dataArray = list(data.values())

        print(network, " : Mean: ", '{:.10f}'.format(np.median(dataArray)))

        costs.append(np.array(dataArray))
    
    overallArray = np.concatenate(costs)
    
    print("overall mean: ", '{:.10f}'.format(np.median(overallArray)))
    




if __name__ == "__main__":

    # writeAllCosts()
    averageCalculations()
