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
            overallCost += nodeCost
            seedSet.append(node[0])
        
        if overallCost == n:
            break

    return seedSet



if __name__ == '__main__':
    import pickle

    with open("costs/" + "amazon" + "/random.p", "rb") as fp:
        data = pickle.load(fp)
    
    with open(r"pickles/amazon.pickle", "rb") as input_file:
        arxivGraph = pickle.load(input_file)
    
    undirected = arxivGraph.to_undirected()

    S = degreeSeedsetNonUniform(undirected, 250, data)

    print(S)