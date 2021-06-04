

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

    for node in G.nodes:
        d[node] = G.degree[node]
        dd[node] = G.degree[node]
        t[node] = 0
    

    while True:

        oldSeedSet = seedSet.copy()

        dd = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for k, v in dd.items():

            if(k in seedSet):
                continue

            nodeCost = costs[k]

            if overallCost+nodeCost <= n:

                print(nodeCost)

                overallCost += nodeCost

                seedSet.append(k)

                for neighbour in G.neighbors(k):
                    if neighbour not in seedSet:
                        t[neighbour] += 1
                        dd[neighbour] = d[neighbour] - 2*t[neighbour] - (d[neighbour]-t[neighbour])*t[neighbour]*p
                break

        if overallCost == n or oldSeedSet == seedSet:
            return seedSet
            
        return seedSet

if __name__ == '__main__':
    import pickle

    with open("costs/" + "github" + "/degree.p", "rb") as fp:
        data = pickle.load(fp)
    
    with open(r"pickles/github.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    undirected = githubGraph.to_undirected()

    S = degreeDiscountNonUniform(undirected, 3000, data)

    print(S)

