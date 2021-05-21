import random 
import collections

def randomSeedset(graph, n):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    randomly select nodes into the seedSet 

    Return: new seedSet

    """
    seedset = []

    for x in range(n):
        node = random.choice(list(graph.nodes))
        while node in seedset:
            node = random.choice(list(graph.nodes))
        seedset.append(str(node))

    return seedset


def degreeSeedset(graph, n):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    select nodes for the seedSet with the highest degree

    Return: new seedSet

    """

    seedSet = []
    degreeDict = {}
    print(len(graph.nodes))
    for node in graph.nodes:
        #degreeDict[len([n for n in graph.neighbors(node)])] = node
        degreeDict[node] = len([n for n in graph.neighbors(node)])
    print(len(degreeDict))

    od = collections.OrderedDict(sorted(degreeDict.items(), reverse=True, key=lambda item: item[1]))

    for k, v in od.items():

        if(len(seedSet) == n):
            print("seedset size: ", len(seedSet))
            break
        
        if(v not in seedSet):
            #print(len([n for n in graph.neighbors(v)]))
            seedSet.append(str(k))
    print("seedset size2: ", len(seedSet))
    
    return seedSet


def singleDegreeDiscount(graph, n):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    node selection using single degree discount heuristic, first proposed by chen et al

    Return: new seedSet

    """
    
    p = 0.1
    seedSet = []
    degreeDict = {}

    #Get degree of each node
    for node in graph.nodes:
        degreeDict[node] = len([n for n in graph.neighbors(node)])
    
    #Sort nodes by degree and add highest one
    # while len(seedSet) < n:
    degreeDict = dict(sorted(degreeDict.items(), key=lambda item: item[1], reverse=True))

    for k, v in degreeDict.items():

        if(len(seedSet) ==  n):
            break

        if(k not in seedSet):
            #print(len([n for n in graph.neighbors(k)]))
            seedSet.append(str(k))

            for neighbour in graph.neighbors(k):
                if neighbour not in seedSet:
                    degreeDict[neighbour] -= 1

    return seedSet


def degreeDiscount(graph, n):
    """
    Input:
    graph: NetworkX graph object
    n: seedSet size
    previousSS: previous seedSet array

    node selection using degree discount heuristic, first proposed by chen et al

    Return: new seedSet
    """

    p = 0.1
    seedSet = []
    degreeDict = {}
    neighboursSelected = {}

    for node in graph.nodes:
        degreeDict[node] = len([n for n in graph.neighbors(node)]) 
        neighboursSelected[node] = 0
    
    # while len(seedSet) < n:
    degreeDict = dict(sorted(degreeDict.items(), key=lambda item: item[1], reverse=True))

    for k, v in degreeDict.items():

        if(len(seedSet) == n):
            break

        if(k not in seedSet):
            #print(len([n for n in graph.neighbors(k)]))
            seedSet.append(str(k))

            for neighbour in graph.neighbors(k):
                if neighbour not in seedSet:
                    neighboursSelected[neighbour] += 1
                    neighbourDegree = len([n for n in graph.neighbors(node)]) 
                    degreeDict[neighbour] = neighbourDegree - (2*neighboursSelected[neighbour]) - ((neighbourDegree-neighboursSelected[neighbour])*(neighboursSelected[neighbour]*p))


    return seedSet







