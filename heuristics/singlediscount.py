import random 
import collections


def singleDegreeDiscountUniform(G, n):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    node selection using single degree discount heuristic, first proposed by chen et al

    Return: new seedSet

    """
    
    seedSet = []
    degreeDict = {}

    #Get degree of each node
    for node in G.nodes:
        degreeDict[node] = G.degree[node]


    #Sort nodes by degree and add highest one
    # while len(seedSet) < n:

    for x in range(n):

        degreeDict = dict(sorted(degreeDict.items(), key=lambda item: item[1], reverse=True))

        for k, v in degreeDict.items():

            if(k in seedSet):
                continue

            seedSet.append(k)

            for neighbour in G.neighbors(k):
                if neighbour not in seedSet:
                    degreeDict[neighbour] -= 1

            break
    return seedSet


def singleDegreeDiscountNonUniform(G, n, costs):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    node selection using single degree discount heuristic, first proposed by chen et al

    Return: new seedSet

    """
    
    seedSet = []
    degreeDict = {}
    overallCost = 0

    #Get degree of each node
    for node in G.nodes:
        degreeDict[node] = G.degree[node]


    #Sort nodes by degree and add highest one

    while True:

        oldSeedSet = seedSet.copy()

        
        # print(seedSet)

        degreeDict = dict(sorted(degreeDict.items(), key=lambda item: item[1], reverse=True))

        for k, v in degreeDict.items():

            if(k in seedSet):
                continue

            nodeCost = costs[k]

            if overallCost+nodeCost <= n:
                print(nodeCost)

                overallCost += nodeCost

                seedSet.append(k)

                for neighbour in G.neighbors(k):
                    if neighbour not in seedSet:
                        degreeDict[neighbour] -= 1

                break
        

        if overallCost == n or oldSeedSet == seedSet:
            return seedSet




if __name__ == '__main__':
    import pickle

    with open("costs/" + "github" + "/pagerank.p", "rb") as fp:
        data = pickle.load(fp)
    
    with open(r"pickles/github.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    undirected = githubGraph.to_undirected()

    S = singleDegreeDiscountNonUniform(undirected, 0.004, data)

    print(S)