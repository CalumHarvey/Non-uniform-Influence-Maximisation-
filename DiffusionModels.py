"""
File containing influence models being used in this simulation
"""
import ndlib.models.epidemics as ep
import ndlib.models.ModelConfig as mc
import networkx as nx
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
import pickle


def loadAmazon():
    with open(r"pickles/amazon.pickle", "rb") as input_file:
        amazonGraph = pickle.load(input_file)
    
    return amazonGraph

def loadGithub():
    with open(r"pickles/github.pickle", "rb") as input_file:
        githubGraph = pickle.load(input_file)
    
    return githubGraph


def linearThreshold(g, seedSet):

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
    iterations = model.iteration_bunch(200)

    trends = model.build_trends(iterations)

    # Visualization
    viz = DiffusionTrend(model, trends)
    viz.plot("diffusion.pdf")

def IndependentCascade(g, seedSet):

    model = ep.IndependentCascadesModel(g)

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
    iterations = model.iteration_bunch(200)

    trends = model.build_trends(iterations)

    # Visualization
    viz = DiffusionTrend(model, trends)
    viz.plot("diffusion.pdf")

def test(g):

    #g = nx.erdos_renyi_graph(1000, 0.1)

    #model = ep.IndependentCascadesModel(g)
    model = ep.IndependentCascadesModel(g)

    # Model Configuration
    config = mc.Configuration()
    config.add_model_parameter('fraction_infected', 0.1)

    # Setting the edge parameters
    threshold = 0.1
    for e in g.edges():
        config.add_edge_configuration("threshold", e, threshold)

    model.set_initial_status(config)

    # Simulation execution
    iterations = model.iteration_bunch(200)

    trends = model.build_trends(iterations)

    # Visualization
    viz = DiffusionTrend(model, trends)
    viz.plot("diffusion.pdf")

graph = loadAmazon()

test(graph)



