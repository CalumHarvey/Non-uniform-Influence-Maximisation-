from random import randint
import networkx as nx


def random(graph):
    labels = {}

    for node in graph.nodes:
        labels[node] = randint(0,10)

    return labels


def degree(graph):
    labels = {}

    for node in graph.nodes:
        labels[node] = len([n for n in graph.neighbors(node)])
    
    return labels


def pageRank(graph):
    return nx.pagerank(graph)