"""
File containing influence models being used in this simulation
"""
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc
import networkx as nx
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
import ndlib.models.CompositeModel as gc
import pickle

from independentCascade import IndependentCascadesModel
from weightedCascade import WeightedCascadeModel

def loadAmazon():
    """
    Load amazon network from pickle file

    Return: 
    amazonGraph: networkX object of network

    """
    with open(r"pickles/amazon.pickle", "rb") as input_file:
        amazonGraph = pickle.load(input_file)
    
    return amazonGraph

def loadGithub():
    """
    Load github network from pickle file

    Return: 
    githubGraph: networkX object of network

    """
    with open(r"pickles/github.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    return githubGraph

def loadArxiv():
    """
    Load arxiv network from pickle file

    Return: 
    arxivGraph: networkX object of network

    """
    with open(r"pickles/arxiv.pickle", "rb") as input_file:
        arxivGraph = pickle.load(input_file)
    
    return arxivGraph


def linearThreshold(g, seedSet, iterations):
    """
    Inputs:
    g: NetworkX graph object
    seedSet: list of nodes in the seedSet
    iterations: number of iterations to be performed 

    Performs linearThreshold model simulations with a specific seedSet using NDlib library functions

    Return:
    number of nodes activate after all iterations have been completed
    """

    model = ep.ThresholdModel(g)

    config = mc.Configuration()

    #Set intial seed set
    config.add_model_initial_configuration("Infected", seedSet)

    #Set threshold of each node
    threshold = 0.2
    for i in g.nodes():
        config.add_node_configuration("threshold", i, threshold)

    model.set_initial_status(config)

    # Simulation execution
    iterations = model.iteration_bunch(iterations)

    trends = model.build_trends(iterations)

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("LT diffusion.pdf")

    return trends[0]["trends"]["node_count"][1][-1]

def independentCascade(g, seedSet, iterations):
    """
    Inputs:
    g: NetworkX graph object
    seedSet: list of nodes in the seedSet
    iterations: number of iterations to be performed 

    Performs independent Cascade model simulations with a specific seedSet using NDlib library functions

    Return:
    number of nodes activate after all iterations have been completed
    """

    model = IndependentCascadesModel(g)

    # Model Configuration
    config = mc.Configuration()

    #Set intial seed set
    config.add_model_initial_configuration("Infected", seedSet)

    # Setting the edge parameters
    threshold = 0.1
    for e in g.edges():
        config.add_edge_configuration("threshold", e, threshold)

    model.set_initial_status(config)

    # Simulation execution
    iterations = model.iteration_bunch(iterations)

    trends = model.build_trends(iterations)

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("IC diffusion.pdf")

    return trends[0]["trends"]["node_count"][1][-1]

def weightedCascade(g, seedSet, iterations):
    """
    Inputs:
    g: NetworkX graph object
    seedSet: list of nodes in the seedSet
    iterations: number of iterations to be performed 

    Performs Weighted Cascade model simulations with a specific seedSet using NDlib library functions

    Return:
    number of nodes activate after all iterations have been completed
    """

    model = WeightedCascadeModel(g)

    # Model Configuration
    config = mc.Configuration()

    #Set intial seed set
    config.add_model_initial_configuration("Infected", seedSet)

    # Setting the edge parameters
    threshold = 0.1
    #for e in g.edges():
    #    config.add_edge_configuration("threshold", e, threshold)

    model.set_initial_status(config)

    # Simulation execution
    iterations = model.iteration_bunch(iterations)

    trends = model.build_trends(iterations)

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("WC diffusion.pdf")

    return trends[0]["trends"]["node_count"][1][-1]


#config.add_model_parameter('fraction_infected', 0.1)

def test(g, seedSet):

    model = ep.ThresholdModel(g)

    config = mc.Configuration()

    #Set intial seed set
    config.add_model_initial_configuration("Infected", seedSet)

    #Set threshold of each node
    threshold = 0.25
    for i in g.nodes():
        config.add_node_configuration("threshold", i, threshold)

    model.set_initial_status(config)

    # Simulation execution
    iterations = model.iteration_bunch(1)

    trends = model.build_trends(iterations)

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("LT diffusion.pdf")
    print(trends)
    return trends[0]["trends"]["node_count"][1][-1]


