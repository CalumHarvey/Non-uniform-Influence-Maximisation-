import random 

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
        degreeDict[graph.neighbors(node)] = node    

    for k, v in sorted(degreeDict.items()):

        if(len(seedSet) == n):
            break
        
        seedSet.append(v)
    
    return seedSet

