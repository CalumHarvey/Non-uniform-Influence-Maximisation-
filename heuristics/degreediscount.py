

def degreeDiscountUniform(G, n, p=0.01):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    node selection using degree discount heuristic, first proposed by chen et al

    Return: new seedSet
    """

    seedSet = []
    dd = dict() # degree dict
    t = dict() # adjacent vertices in seedSet
    d = dict() # degree of each vertice

    for node in G.nodes:
        d[node] = G.degree[node]
        dd[node] = G.degree[node]
        t[node] = 0
    

    for x in range(n):

        dd = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for k, v in dd.items():

            if(k in seedSet):
                continue

            seedSet.append(k)

            for neighbour in G.neighbors(k):
                if neighbour not in seedSet:
                    t[neighbour] += 1
                    dd[neighbour] = d[neighbour] - 2*t[neighbour] - (d[neighbour]-t[neighbour])*t[neighbour]*p
            break

    return seedSet


def degreeDiscountNonUniform(G, n, costs, p=0.01):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    node selection using degree discount heuristic, first proposed by chen et al

    Return: new seedSet
    """
    overallCost = 0
    seedSet = []
    dd = dict() # degree dict
    t = dict() # adjacent vertices in seedSet
    d = dict() # degree of each vertice

    # Initialise variables
    for node in G.nodes:
        d[node] = G.degree[node]
        dd[node] = G.degree[node]
        t[node] = 0
    

    while True:
        # Copy seed set
        oldSeedSet = seedSet.copy()
        #Sort Dictionary buy degree
        dd = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for k, v in dd.items():
            # If node already in seed set, move to next one
            if(k in seedSet):
                continue
            
            nodeCost = costs[k]

            # If the new node can fit in the budget, add it
            if overallCost+nodeCost <= n:

                overallCost += nodeCost

                seedSet.append(k)

                for neighbour in G.neighbors(k):
                    if neighbour not in seedSet:
                        # Discount degree
                        t[neighbour] += 1
                        dd[neighbour] = d[neighbour] - 2*t[neighbour] - (d[neighbour]-t[neighbour])*t[neighbour]*p
                break
        
        # Exit conditions
        if overallCost == n or oldSeedSet == seedSet:
            return seedSet
        


if __name__ == '__main__':
    import pickle

    with open("costs/" + "arxiv" + "/pagerank.p", "rb") as fp:
        data = pickle.load(fp)
    
    with open(r"pickles/arxiv.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    undirected = githubGraph.to_undirected()

    S = degreeDiscountNonUniform(undirected, 0.000027*100, data)

    print(S)
    print(len(S))

