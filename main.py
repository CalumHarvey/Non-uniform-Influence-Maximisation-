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


def singleRun(networks, heuristic, model, networkName):
    """
    Input:
    networks: networkX graph object
    heuristic: function used to pick seedSet nodes
    model: network diffusion model object

    Runs a test for a single set of parameters defined in the inputs 

    Return: array of number of infections for each seedSet size

    """

    infections = []

    #network = input("Choose network to use \n 1: amazon \n 2: Github \n")
    network = networks()
    
    #heuristic = input("Choose Heuristic: \n 1: Random \n 2: Degree \n 3: Single Degree \n 4: Degree Discount\n ")

    seedSetSize = 100
    repetitions = 20
    seedSet = []

    for x in range(10, 60, 10):
        seedSet = np.array(heuristic(network, x))
        if networkName == "Github":
            seedSet = seedSet.astype("int")
        outputs = []
        for y in range(repetitions):
            print(y)
            infectedNodes = model(network, seedSet)
            outputs.append(infectedNodes)

            print(infectedNodes)
        
        infections.append(int(np.mean(np.array(outputs))))

    return infections
    

def plotInfection(infections, network, heuristic, model):
    """
    Inputs:
    infections: array of number of infections for each seedSet size
    network: name of network used to gain infections data
    heuristic: name of heuristic used to gain infections data
    model: name of model used to gain infections data

    Plots infections on a graph, saves graph as a png in a folder related to network, heuristic and model name
    """


    yAxis = []
    for x in range(len(infections)):
        yAxis.append(x+1)
    
    plt.plot(yAxis, infections, label=heuristic)
    plt.legend()

    directory = "graphs/uniform/" + network + "/" + model
    if not os.path.exists(directory):
        os.makedirs(directory)

    plt.savefig(directory + "/" + heuristic + '.png')
    plt.clf()

def plotAllHeuristics(data, fileName, heuristics):
    """
    Input:
    data: 2d array of infection data from each heuristic
    fileName: name of file where graph is saved
    heuristics: list of all heuristics, used for legend creation


    Plots results for all heuristics for a specific network and model, then saves graph as png
    """


    yAxis = []
    for x in range(len(data[0])):
        yAxis.append(x+1)

    for x in range(len(data)):
        plt.plot(yAxis, data[x], label=heuristics[x])
    
    plt.legend()

    directory = "graphs/uniform/allHeuristics"
    if not os.path.exists(directory):
        os.makedirs(directory)

    plt.savefig(directory + "/" + fileName + '.png')
    plt.clf()



def main():

    # Empty array for results 
    results = []

    # Arrays for names of networks, heuristics and models
    # ["Amazon", "Github", "Arxiv"]
    networkNames = ["Github", "Arxiv"]
    heuristicNames= ["Random", "Degree", "SingleDiscount", "DegreeDiscount"] # ["Random", "Degree", "SingleDiscount", "DegreeDiscount"]
    diffusionNames = ["LinearThreshold", "IndependentCascade", "WeightedCascade"]  # ["LinearThreshold", "IndependentCascade", "WeightedCascade"] 

    # Arrays for functions relating to networks, heuristics and models
    # [loadAmazon, loadGithub, loadArxiv]
    networks = np.array([loadGithub, loadArxiv])
    heuristics = [randomSeedset, degreeSeedset, singleDegreeDiscount, degreeDiscount] #  [randomSeedset, degreeSeedset, singleDegreeDiscount, degreeDiscount]
    diffusionModels = [linearThreshold, independentCascade, weightedCascade] # [linearThreshold, independentCascade, weightedCascade]

    #For each network...
    for x in range(len(networks)):
        #Write name of network to file
        with open("results.txt", "a") as myfile:
            myfile.write("Network: " + networkNames[x] + "\n")
        #For each model...
        for y in range(len(diffusionModels)):
            #Write name of model to file
            with open("results.txt", "a") as myfile:
                    myfile.write("\tDiffusion Model: " + diffusionNames[y] + "\n")
            results = []
            # For each heuristic...
            for z in range(len(heuristics)):

                # Run single test with set parameters
                infections = singleRun(networks[x], heuristics[z], diffusionModels[y], networkNames[x])

                # Plot infections for single heuristic
                plotInfection(infections, networkNames[x], heuristicNames[z], diffusionNames[y])

                # Append results from single run to array
                results.append(infections)

                # Write single run results to file
                with open("results.txt", "a") as myfile:
                    myfile.write("\t\tHeuristic: " + heuristicNames[z] + "\n\t\t" + str(infections) + "\n")
            
            # Plot all heuristics for single network and model
            plotAllHeuristics(results, networkNames[x] + diffusionNames[y], heuristicNames)

if __name__ == "__main__":
    main()