import random 
import collections


def degreeSeedsetUniform(G, n):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    select nodes for the seedSet with the highest degree

    Return: new seedSet

    """

    seedSet = []

    sortedNodes = sorted(G.degree, key=lambda x: x[1], reverse=True)

    for x in range(n):

        seedSet.append(str(sortedNodes[x][0]))
    
    return seedSet


def degreeSeedsetNonUniform(G, n, costs):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    select nodes for the seedSet with the highest degree

    Return: new seedSet

    """

    seedSet = []
    overallCost = 0

    sortedNodes = sorted(G.degree, key=lambda x: x[1], reverse=True)

    for node in sortedNodes:

        nodeCost = costs[node[0]]

        if overallCost+nodeCost <= n:
            print(nodeCost)
            overallCost += nodeCost
            seedSet.append(node[0])
        

    return seedSet



if __name__ == '__main__':
    import pickle

    with open("costs/" + "github" + "/degree.p", "rb") as fp:
        data = pickle.load(fp)
    
    with open(r"pickles/arxiv.pickle", "rb") as input_file:
        arxivGraph = pickle.load(input_file)
    
    undirected = arxivGraph.to_undirected()

    S = degreeSeedsetUniform(undirected, 50)

    print(S)