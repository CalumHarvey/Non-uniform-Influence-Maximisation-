import random 
import collections

def randomSeedsetUniform(G, n):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    randomly select nodes into the seedSet 

    Return: new seedSet

    """

    seedset = random.sample(list(G.nodes), n)

    return seedset


def randomSeedsetNonUniform(G, n, costs):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    randomly select nodes into the seedSet 

    Return: new seedSet

    """
    overallCost = 0
    seedset = []

    while True:

        node = random.sample(G.nodes(), 1)

        nodeCost = costs[node[0]]

        if overallCost+nodeCost > n:
            return seedset

        overallCost += nodeCost
        seedset.append(node[0])


if __name__ == '__main__':
    import pickle

    with open("costs/" + "arxiv" + "/random.p", "rb") as fp:
        data = pickle.load(fp)
    
    with open(r"pickles/arxiv.pickle", "rb") as input_file:
        arxivGraph = pickle.load(input_file)
    
    undirected = arxivGraph.to_undirected()

    S = randomSeedsetUniform(undirected, 50)

    print(S)