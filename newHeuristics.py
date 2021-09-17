
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
        
        if TC >= b or len(sortedCosts) == 0:
            return S



def highestCost(G, b, C):

    S = []
    TC = 0

    sortedCosts = dict(sorted(C.items(), key=lambda item: item[1], reverse=True))

    for k,v in sortedCosts.items():

        if TC+v <= b:

            S.append(k)
            TC += v
        
        if TC == b:
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
    TC = 0
    d = dict()

    for node in G.nodes:
        d[node] = C[node] / G.degree[node]

    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=False))

    for k,v in d.items():

        budgetLeft = b - TC
        nodeCost = C[k]

        if TC+nodeCost <= b:

            S.append(k)
            TC += nodeCost
        
        if TC == b:
            break
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
        dd[node] =  C[node] / d[node]

    while True:

        oldSeedSet = S.copy()

        dd = dict(sorted(dd.items(), key=lambda item: (item[1] is None, item[1]), reverse=False))

        for k, v in dd.items():

            # print(k, v)
            # input()

            if k in S:
                continue

            nodeCost = C[k]
            budgetLeft = b - TC

            if TC+nodeCost <= b:

                TC += nodeCost

                S.append(k)

                costs.append(C[k])
                degrees.append(G.degree[k])

                # print(k)
                # print(v)
                # print(C[k], "/", G.degree[k])
                # print(budgetLeft)
                # input()

                for neighbour in G.neighbors(k):
                    if neighbour not in S and dd[neighbour] is not None:
                        t[neighbour] += 1
                        # print(d[neighbour])
                        # print(t[neighbour])
                        # input()
                        if d[neighbour] - t[neighbour] == 0:
                            dd[neighbour] = 0
                        else:
                            dd[neighbour] = C[neighbour] / (d[neighbour] - t[neighbour])
                break
        # return seedSet

        if TC == b or oldSeedSet == S:
            # print(costs)
            # print(degrees)
            return S



def PICR(G, b, C, p=0.01):

    S = []
    augmentCost = []
    costs = []
    degrees = []
    TC = 0
    d = dict()
    dd = dict()
    t = dict()

    for node in G.nodes:
        t[node] = 0
        d[node] = G.degree[node]
        dd[node] = (1+(d[node]*p)) / C[node]

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
                augmentCost.append(v)
                degrees.append(G.degree[k])

                for neighbour in G.neighbors(k):
                    if neighbour not in S:
                        t[neighbour] += 1
                        dd[neighbour] = (1+((d[neighbour]-t[neighbour])*p)) / C[neighbour]
                break

        if TC == b or oldSeedSet == S:
            return S

def PICRnoprob(G, b, C, p=0.01):

    S = []
    augmentCost = []
    costs = []
    degrees = []
    TC = 0
    d = dict()
    dd = dict()
    t = dict()

    for node in G.nodes:
        t[node] = 0
        d[node] = G.degree[node]
        dd[node] = (1+(d[node])) / C[node]

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
                augmentCost.append(v)
                degrees.append(G.degree[k])

                for neighbour in G.neighbors(k):
                    if neighbour not in S:
                        t[neighbour] += 1
                        dd[neighbour] = (1+((d[neighbour]-t[neighbour]))) / C[neighbour]
                break

        if TC == b or oldSeedSet == S:
            return S

def LowestCost(G, b, C):

    S = []
    TC = 0
    costs = []

    sortedCosts = dict(sorted(C.items(), key=lambda item: item[1], reverse=False))

    for k,v in sortedCosts.items():

        if TC+v <= b:

            S.append(k)
        
        TC += v
        
        if TC >= b:
            break
    return S



def main(data, undirected, average):
    diffusionModels = [linearThreshold, independentCascade, weightedCascade]  


    for model in diffusionModels:

        infections = []

        for x in range(50, 550,50):

            S = LowestCost(undirected, x*average, data)

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

    averagesAM = [5,6,0.0000033]
    averagesGT = [5,6,0.000013]
    averagesAX = [5,4,0.000027]
    # amazon github arxiv
    networkName = "arxiv"

    with open("costs/" + networkName + "/pagerank.p", "rb") as fp: #change "amazon" to "github"
        data3 = pickle.load(fp)

    with open("costs/" + networkName + "/degree.p", "rb") as fp: #change "amazon" to "github"
        data2 = pickle.load(fp)
    
    with open("costs/" + networkName + "/random.p", "rb") as fp: #change "amazon" to "github"
        data = pickle.load(fp)
    
    with open(r"pickles/" + networkName + ".pickle", "rb") as input_file: #change "amazon" to "github"
        githubGraph = pickle.load(input_file)
    
    undirected = githubGraph.to_undirected()

    S = PICR(undirected, averagesAX[2]*500, data3)

    # outputs = []
    # for x in range(10):
    #     lt = weightedCascade(undirected, S)
    #     outputs.append(lt)
    
    # lt = linearThreshold(undirected, S)
    # ic = independentCascade(undirected, S)
    # wc = weightedCascade(undirected, S)
    # print("x:", x)
    # print("seedSet size:", len(S))
    # print("\tResults: ", lt, " ", ic, " ", wc)

    print(S)
    print(len(S))
    # print(int(round(np.mean(np.array(outputs)))))

    # print("Random")
    # main(data, undirected, averagesAX[0]) 
    # print("Degree")
    # main(data2, undirected, averagesAX[1]) 
    # print("Page Rank")
    # main(data3, undirected, averagesAX[2])


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