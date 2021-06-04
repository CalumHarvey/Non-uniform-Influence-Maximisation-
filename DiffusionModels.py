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
    threshold = 0.6
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

def independentCascade(g, seedSet):
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
    model = IndependentCascadesModel(g)

    # Model Configuration
    config = mc.Configuration()

    #Set intial seed set
    config.add_model_initial_configuration("Infected", seedSet)

    # Setting the edge parameters
    threshold = 0.01
    for e in g.edges():
        config.add_edge_configuration("threshold", e, threshold)

    model.set_initial_status(config)


    # Simulation execution
    while True:
        iterations = model.iteration()
        if iterations["node_count"][1] == 0:
            break
        nodesActive.append(int(iterations["node_count"][2] + iterations["node_count"][1]))

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("IC diffusion.pdf")

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
    nodesActive = [0]
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

    while True:
        iterations = model.iteration()
        # print(iterations["node_count"])
        if iterations["node_count"][1] == 0:
            break
        nodesActive.append(int(iterations["node_count"][2] + iterations["node_count"][1]))


    return nodesActive[-1]
    # return iterations[-1]["node_count"][2]


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
    nodesActive = []
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
    """
    while True:
        iterations = model.iteration()
        # print(iterations["node_count"])
        if iterations["node_count"][1] == 0:
            break
        nodesActive.append(int(iterations["node_count"][2] + iterations["node_count"][1]))
    """
    iterations = model.iteration_bunch(10)
    print(iterations[-1]["node_count"][2])
    input()
    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("WC diffusion.pdf")
    # input()
    return nodesActive[-1]


# g = loadGithub()
# s = [17522, 18369, 21618, 15051, 28102, 9587, 15191, 30153, 30648]
# test(g, s)

# ['17522', '18369', '21618', '15051', '28102', '29587', '15191', '30153', '30648', '28887', '25722', '28154', '35949', '16372', '11948', '8274', '34875', '13115', '12311', '14854', '25137', '4602', '4080', '20521', '25649', '22201', '4816', '25740', '10949', '27649', '32775', '12893', '23711', '18965', '11215', '3026', '33276', '21952', '29906', '25480', '19402', '15423', '5276', '2729', '30660', '19976', '4621', '23820', '21818', '7390', '26403', '32820', '15391', '34722', '11629', '17000', '36906', '10377', '21322', '9921', '6110', '13788', '13438', '4200', '32369', '12721', '18981', '571', '23972', '22887', '9266', '28768', '4881', '35225', '35257', '20640', '22555', '26832', '19844', '28067', '21901', '33594', '29048', '24583', '17056', '13503', '34355', '1508', '12444', '13733', '24679', '10179', '8209', '5580', '1806', '31715', '972', 
# '12071', '17836', '29125']
