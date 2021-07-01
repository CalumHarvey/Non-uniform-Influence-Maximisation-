
def averageCost(G, b, C):

    S = []
    costs = []
    TC = 0

    sortedCosts = dict(sorted(C.items(), key=lambda item: item[1], reverse=True))


    while True:

        middle = len(sortedCosts) // 2


        middleNode = list(sortedCosts.keys())[middle]
        middleValue = list(sortedCosts.values())[middle]


        if TC+middleValue <= b:

            S.append(middleNode)
            costs.append(middleValue)

            del sortedCosts[middleNode]

        TC += middleValue
        
        # print(TC, b)
        # print(S)
        # input()

        
        if TC >= b or len(sortedCosts) == 0:
            print(costs)
            return S



def highestCost(G, b, C):

    S = []
    TC = 0

    sortedCosts = dict(sorted(C.items(), key=lambda item: item[1], reverse=True))

    for k,v in sortedCosts.items():

        if TC+v <= b:

            S.append(k)
        
        TC += v
        
        if TC >= b:
            break
    
    return S



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

                overallCost += nodeCost

                seedSet.append(k)

                for neighbour in G.neighbors(k):
                    if neighbour not in seedSet:
                        t[neighbour] += 1
                        dd[neighbour] = (d[neighbour] - 2*t[neighbour] - (d[neighbour]-t[neighbour])*t[neighbour]*p) / costs[neighbour]
                break

        #return seedSet
        

        if overallCost == n or oldSeedSet == seedSet:
            return seedSet



def degreeCostPercentage(G, b, C):

    S = []
    costs = []
    TC = 0
    d = dict()

    for node in G.nodes:
        d[node] = G.degree[node]

    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    for k,v in d.items():

        budgetLeft = b - TC

        if TC+v <= b and v <= budgetLeft * 0.015:

            S.append(k)
            costs.append(v)
        
            TC += v
        
        if TC == b:
            break
    
    # print(costs)
    return S



def degreeCostPercentage2(G, b, C, p=0.01):

    S = []
    costs = []
    degrees = []
    TC = 0
    d = dict()
    dd = dict()
    t = dict()

    for node in G.nodes:
        t[node] = 0
        d[node] = G.degree[node]
        dd[node] = (1+(d[node] - t[node])*p) / C[node]

    while True:

        oldSeedSet = S.copy()

        dd = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for k, v in dd.items():

            if k in S:
                continue

            nodeCost = C[k]
            budgetLeft = b - TC

            if TC+nodeCost <= b:

                TC += nodeCost

                S.append(k)

                costs.append(C[k])
                degrees.append(G.degree[k])

                for neighbour in G.neighbors(k):
                    if neighbour not in S:
                        t[neighbour] += 1
                        dd[neighbour] = (1+(d[neighbour] - t[neighbour])*p) / C[neighbour]
                break
        # return seedSet

        if TC == b or oldSeedSet == S:
            print(costs)
            print(degrees)
            return S



def degreeCostPercentage3(G, b, C, p=0.01):

    TC = 0
    seedSet = []
    costs = []
    dd = dict()  # degree dict
    t = dict()  # adjacent vertices in seedSet
    d = dict()  # degree of each vertice
    nd = dict()

    for node in G.nodes:
        d[node] = int(G.degree[node])
        dd[node] = int(G.degree[node])
        t[node] = 0

    while True:

        oldSeedSet = seedSet.copy()

        nd = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for k, v in nd.items():

            if k in seedSet:
                continue

            nodeCost = C[k]
            budgetLeft = b - TC

            if TC+nodeCost <= b and nodeCost <= budgetLeft * 0.015:

                TC += nodeCost

                seedSet.append(k)

                costs.append(v)

                for neighbour in G.neighbors(k):
                    if neighbour not in seedSet:
                        t[neighbour] += 1
                        dd[neighbour] = (d[neighbour] - 2*t[neighbour] - (d[neighbour]-t[neighbour])*t[neighbour]*p) / C[neighbour]
                break
        # return seedSet

        if TC == b or oldSeedSet == seedSet:
            # print(costs)
            return seedSet




def main(data, undirected, average):
    diffusionModels = [linearThreshold, independentCascade, weightedCascade]  


    for model in diffusionModels:

        infections = []

        for x in range(50, 550,50):

            S = degreeCostPercentage3(undirected, x*average, data)

            outputs = []

            for y in range(10):

                infectedNodes = model(undirected, S)
                outputs.append(infectedNodes)

            
            infections.append(int(round(np.mean(np.array(outputs)))))

        print(infections)

    

if __name__ == '__main__':
    

    import pickle
    from DiffusionModels import loadAmazon, loadGithub, loadArxiv, linearThreshold, weightedCascade, independentCascade
    import numpy as np

    averages = [5, 4, 0.000027]

    with open("costs/" + "arxiv" + "/pagerank.p", "rb") as fp:
        data3 = pickle.load(fp)

    with open("costs/" + "arxiv" + "/degree.p", "rb") as fp:
        data2 = pickle.load(fp)
    
    with open("costs/" + "arxiv" + "/random.p", "rb") as fp:
        data = pickle.load(fp)
    
    with open(r"pickles/arxiv.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    undirected = githubGraph.to_undirected()

    # S = degreeCostPercentage2(undirected, 0.000027*100, data3)

    # infectedNodes = weightedCascade(undirected, S)
    # print(infectedNodes)
    # S = averageCost(undirected, 250, data)

    # print(S)
    # print(len(S))
    print("Random")
    main(data, undirected, 5) 
    print("Degree")
    main(data2, undirected, 4) 
    print("Page Rank")
    main(data3, undirected, 0.000027) 



"""

def degreeCostPercentage2(G, b, C, p=0.01):

    TC = 0
    seedSet = []
    costs = []
    dd = dict()  # degree dict
    t = dict()  # adjacent vertices in seedSet
    d = dict()  # degree of each vertice
    nd = dict()

    for node in G.nodes:
        d[node] = int(G.degree[node])
        dd[node] = int(G.degree[node])
        nd[node] = (dd[node] / C[node]) * d[node]
        # t[node] = 0

    while True:

        oldSeedSet = seedSet.copy()

        nd = dict(sorted(dd.items(), key=lambda item: item[1], reverse=True))

        for k, v in nd.items():

            if k in seedSet:
                continue

            nodeCost = C[k]
            budgetLeft = b - TC

            if TC+nodeCost <= b and nodeCost <= budgetLeft * 0.015:

                TC += nodeCost

                seedSet.append(k)

                costs.append(v)

                for neighbour in G.neighbors(k):
                    if neighbour not in seedSet:
                        # t[neighbour] += 1
                        # dd[neighbour] = (d[neighbour] - 2*t[neighbour] - (d[neighbour]-t[neighbour])*t[neighbour]*p) / C[neighbour]
                        dd[neighbour] -= 1
                        nd[neighbour] = (dd[node] / C[node]) * d[node]
                break
        # return seedSet

        if TC == b or oldSeedSet == seedSet:
            # print(costs)
            return seedSet

"""