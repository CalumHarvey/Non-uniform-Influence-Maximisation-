import random 
import collections

def randomSeedset(graph, n):

    seedset = []

    for x in range(n):
        node = random.randint(0, len(graph.nodes))
        while node in seedset:
            node = random.randint(0, len(graph.nodes))
        seedset.append(node)

    return seedset


def degreeSeedset(graph, n):

    seedSet = []
    degreeDict = {}

    for node in graph.nodes:
        degreeDict[len(graph.neighbors(node))] = node   

    od = collections.OrderedDict(sorted(degreeDict.items())) 

    for k, v in od.items():

        if(len(seedSet) == n):
            break
        
        seedSet.append(v)
    
    return seedSet

def singleDegreeDiscount(graph, n):
    p = 0.1
    seedSet  = []
    degreeDict = {}
    neighboursSelected = {}

    for node in graph.nodes:
        degreeDict[node] = len(graph.neighbors(node))  
        neighboursSelected[node] = 0
    
    for x in range(n):
        degreeDict = sorted(degreeDict, key=degreeDict.get)
        u, d  = next(iter( degreeDict.items()))
        while u in seedSet:
            u, d  = next(iter( degreeDict.items()))
        seedSet.append(u)

        for neighbour in graph.neighbors(u):
            if neighbour not in seedSet:
                degreeDict[neighbour] -= 1
    return seedSet


def degreeDiscount(graph, n):
    p = 0.1
    seedSet  = []
    degreeDict = {}
    neighboursSelected = {}

    for node in graph.nodes:
        degreeDict[node] = len(graph.neighbors(node))  
        neighboursSelected[node] = 0
    
    for x in range(n):
        degreeDict = sorted(degreeDict, key=degreeDict.get)
        u, d  = next(iter( degreeDict.items()))
        while u in seedSet:
            u, d  = next(iter( degreeDict.items()))
        seedSet.append(u)

        for neighbour in graph.neighbors(u):
            if neighbour not in seedSet:
                neighboursSelected[neighbour] += 1
                degreeDict[neighbour] = len(graph.neighbors(neighbour)) - (2*neighboursSelected[neighbour]) - ((len(graph.neighbors(neighbour))-neighboursSelected[neighbour])*(neighboursSelected[neighbour]*p))

    return seedSet







