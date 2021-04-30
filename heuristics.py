import random 
import collections

def randomSeedset(graph, n, previousSS):

    seedset = previousSS

    while len(seedset) < n:
        node = random.randint(0, len(graph.nodes))
        while node in seedset:
            node = random.randint(0, len(graph.nodes))
        seedset.append(str(node))

    return seedset


def degreeSeedset(graph, n, previousSS):

    seedSet = previousSS
    degreeDict = {}

    for node in graph.nodes:
        # print(len([n for n in graph.neighbors(node)]))
        degreeDict[len([n for n in graph.neighbors(node)])] = node

    od = collections.OrderedDict(sorted(degreeDict.items(), reverse=True))

    for k, v in od.items():

        if(len(seedSet) == n):
            break
        
        if(v not in seedSet):
            print(len([n for n in graph.neighbors(v)]))
            seedSet.append(v)
    
    return seedSet


def singleDegreeDiscount(graph, n, previousSS):
    
    p = 0.1
    seedSet = previousSS
    degreeDict = {}

    #Get degree of each node
    for node in graph.nodes:
        degreeDict[node] = len([n for n in graph.neighbors(node)])
    
    #Sort nodes by degree and add highest one
    while len(seedSet) < n:
        degreeDict = dict(sorted(degreeDict.items(), key=lambda item: item[1], reverse=True))

        for k, v in degreeDict.items():

            if(k not in seedSet):
                print(len([n for n in graph.neighbors(k)]))
                seedSet.append(k)

                for neighbour in graph.neighbors(k):
                    if neighbour not in seedSet:
                        degreeDict[neighbour] -= 1
                break

    return seedSet


def degreeDiscount(graph, n, previousSS):
    p = 0.1
    seedSet = previousSS
    degreeDict = {}
    neighboursSelected = {}

    for node in graph.nodes:
        degreeDict[node] = len([n for n in graph.neighbors(node)]) 
        neighboursSelected[node] = 0
    
    while len(seedSet) < n:
        degreeDict = dict(sorted(degreeDict.items(), key=lambda item: item[1], reverse=True))

        for k, v in degreeDict.items():

            if(k not in seedSet):
                print(len([n for n in graph.neighbors(k)]))
                seedSet.append(k)

                for neighbour in graph.neighbors(k):
                    if neighbour not in seedSet:
                        neighboursSelected[neighbour] += 1
                        neighbourDegree = len([n for n in graph.neighbors(node)]) 
                        degreeDict[neighbour] = neighbourDegree - (2*neighboursSelected[neighbour]) - ((neighbourDegree-neighboursSelected[neighbour])*(neighboursSelected[neighbour]*p))

                break

    return seedSet







