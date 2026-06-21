"""
File containing influence models being used in this simulation
"""
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc
import networkx as nx
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
import ndlib.models.CompositeModel as gc
import pickle
import powerlaw

from models import IndependentCascadesModel, WeightedCascadeModel


def loadAmazon():
    """
    Load amazon network from pickle file

    Return: 
    amazonGraph: networkX object of network

    """
    with open(r"pickles/amazon.pickle", "rb") as input_file:
        amazonGraph = pickle.load(input_file)
    
    undirected = amazonGraph.to_undirected()
    
    return undirected

def loadGithub():
    """
    Load github network from pickle file

    Return: 
    githubGraph: networkX object of network

    """
    with open(r"pickles/github.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    undirected = githubGraph.to_undirected()
    
    return undirected

def loadArxiv():
    """
    Load arxiv network from pickle file

    Return: 
    arxivGraph: networkX object of network

    """
    with open(r"pickles/arxiv.pickle", "rb") as input_file:
        arxivGraph = pickle.load(input_file)
    
    undirected = arxivGraph.to_undirected()
    
    return undirected


def linearThreshold(g, seedSet):
    """
    Inputs:
    g: NetworkX graph object
    seedSet: list of nodes in the seedSet
    iterations: number of iterations to be performed 

    Performs linearThreshold model simulations with a specific seedSet using NDlib library functions

    Return:
    number of nodes activate after all iterations have been completed
    """
    nodesActive = [0]
    model = ep.ThresholdModel(g)

    config = mc.Configuration()

    #Set intial seed set
    config.add_model_initial_configuration("Infected", seedSet)

    #Set threshold of each node
    threshold = 0.5
    for i in g.nodes():
        config.add_node_configuration("threshold", i, threshold)

    model.set_initial_status(config)

    # Simulation execution
    previousCount = 0
    while True:
        iterations = model.iteration()
        if iterations["node_count"][1] == previousCount:
            break
        nodesActive.append(iterations["node_count"][1])
        previousCount = iterations["node_count"][1]

    return nodesActive[-1]


def independentCascade(g, seedSet):

    nodesActive = [0]
    # Initialise Model
    model = IndependentCascadesModel(g, seedSet)

    while True:
        # One iteration
        iterations = model.iteration()

        # Add total overall infected node count to array
        nodesActive.append(int(iterations["infected"] + iterations["removed"]))

        #If the number of new infections is 0...
        if iterations["infected"] == 0:
            # Break out of loop
            break

    # Return last overall infected node count
    return nodesActive[-1]




def weightedCascade(g, seedSet):
    """
    Inputs:
    g: NetworkX graph object
    seedSet: list of nodes in the seedSet
    iterations: number of iterations to be performed 

    Performs Weighted Cascade model simulations with a specific seedSet using NDlib library functions

    Return:
    number of nodes activate after all iterations have been completed
    """

    nodesActive = []
    model = WeightedCascadeModel(g.to_directed(), seedSet)
    firstIteration = True

    while True:
        iterations = model.iteration()
        nodesActive.append(int(iterations["infected"] + iterations["removed"]))
        if iterations["infected"] == 0:
            break
    return nodesActive[-1]



#config.add_model_parameter('fraction_infected', 0.1)

def test(g, seedSet):
    """
    Inputs:
    g: NetworkX graph object
    seedSet: list of nodes in the seedSet
    iterations: number of iterations to be performed 

    Performs independent Cascade model simulations with a specific seedSet using NDlib library functions

    Return:
    number of nodes activate after all iterations have been completed
    """
    nodesActive = [0]
    model = ep.ThresholdModel(g)

    config = mc.Configuration()

    #Set intial seed set
    config.add_model_initial_configuration("Infected", seedSet)

    #Set threshold of each node
    threshold = 0.5
    for i in g.nodes():
        config.add_node_configuration("threshold", i, threshold)

    model.set_initial_status(config)

    # Simulation execution
    previousCount = 0
    while True:
        iterations = model.iteration()
        # print(iterations["node_count"])
        if iterations["node_count"][1] == previousCount:
            break
        nodesActive.append(iterations["node_count"][1])
        previousCount = iterations["node_count"][1]

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("LT diffusion.pdf")

    return nodesActive[-1]

if __name__ == "__main__":
    # %%
    import matplotlib.pyplot as plt
    import pickle
    import powerlaw


    with open(r"pickles/github.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    G = githubGraph.to_undirected()

    degrees = sorted([d for n, d in G.degree()], reverse=True)

    fit = powerlaw.Fit(degrees, xmin=1)
    fig2 = fit.plot_pdf(color='b', linewidth=2)
    fit.power_law.plot_pdf(color='g', linestyle='--', ax=fig2)
    plt.xlabel("Node Degree")
    plt.ylabel("Fraction of Nodes")
    plt.show()
# %%
