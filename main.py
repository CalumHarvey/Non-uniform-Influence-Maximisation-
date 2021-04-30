from heuristics import degreeDiscount, singleDegreeDiscount, degreeSeedset, randomSeedset
from DiffusionModels import loadAmazon, loadGithub, loadArxiv, linearThreshold, weightedCascade, independentCascade
import numpy as np
import matplotlib.pyplot as plt
import os
"""
1. get a network

2. pass network to heuristic with n specified, seedset is returned

3. monte carlo simulation 50 times

    3.1. seedSet is passed to a diffusion model

    3.2. number of infected nodes is output by the diffusion model

5. do this for each seedset size up to x
"""


def singleRun(networks, heuristic, model):

    infections = []

    #network = input("Choose network to use \n 1: amazon \n 2: Github \n")
    network = networks()
    
    #heuristic = input("Choose Heuristic: \n 1: Random \n 2: Degree \n 3: Single Degree \n 4: Degree Discount\n ")

    seedSetSize = 50
    seedSet = []

    for x in range(seedSetSize):
        seedSet = heuristic(network, x+1, seedSet)
        print(seedSet)
        outputs = []
        for y in range(25):
            print(y)
            infectedNodes = model(network, seedSet, 10)
            outputs.append(infectedNodes)

            print(infectedNodes)
        
        infections.append(int(np.mean(np.array(outputs))))

    return infections
    

def plotInfection(infections, network, heuristic, model):
    yAxis = []
    for x in range(len(infections)):
        yAxis.append(x+1)
    
    plt.plot(yAxis, infections, label=heuristic)
    plt.legend()

    directory = "graphs/" + network + "/" + model
    if not os.path.exists(directory):
        os.makedirs(directory)

    plt.savefig(directory + "/" + heuristic + '.png')
    plt.clf()

def plotAllHeuristics(data, fileName, heuristics):
    yAxis = []
    for x in range(len(data[0])):
        yAxis.append(x+1)

    for x in range(len(data)):
        plt.plot(yAxis, data[x], label=heuristics[x])
    
    plt.legend()

    directory = "graphs/allHeuristics"
    if not os.path.exists(directory):
        os.makedirs(directory)

    plt.savefig(directory + "/" + fileName + '.png')
    plt.clf()



def main():

    results = []
    networkNames = ["Amazon", "Github", "Arxiv"]
    heuristicNames= ["Random", "Degree", "SingleDiscount", "DegreeDiscount"]
    diffusionNames = ["LinearThreshold", "IndependentCascade", "WeightedCascade"]
    networks = np.array([loadAmazon, loadGithub, loadArxiv])
    heuristics = [randomSeedset, degreeSeedset, singleDegreeDiscount, degreeDiscount]
    diffusionModels = [linearThreshold, independentCascade, weightedCascade]

    for x in range(len(networks)):
        with open("results.txt", "a") as myfile:
                    myfile.write("Network: " + networkNames[x] + "\n")
        for y in range(len(diffusionModels)):
            with open("results.txt", "a") as myfile:
                    myfile.write("\tDiffusion Model: " + diffusionNames[y] + "\n")
            results = []
            for z in range(len(heuristics)):

                infections = singleRun(networks[x], heuristics[z], diffusionModels[y])
                # infections = singleRun(loadGithub, degreeSeedset, linearThreshold)
                print(infections)

                plotInfection(infections, networkNames[x], heuristicNames[z], diffusionNames[y])

                results.append(infections)
                #output = "Heuristic: " + heuristicNames[z] + "\n" + infections + "\n"

                with open("results.txt", "a") as myfile:
                    myfile.write("\t\tHeuristic: " + heuristicNames[z] + "\n\t\t" + str(infections) + "\n")
            
            plotAllHeuristics(results, networkNames[x] + diffusionNames[y], heuristicNames)
            
    
    print(results)

if __name__ == "__main__":
    main()