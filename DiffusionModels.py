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
from newWeightedCascade import NewWeightedCascadeModel

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

    nodesActive = [0]
    model = IndependentCascadesModel(g, seedSet)

    while True:
        iterations = model.iteration()

        nodesActive.append(int(iterations["infected"] + iterations["removed"]))
    
        if iterations["infected"] == 0:
            break

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("WC diffusion.pdf")
    # input()

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

        # print(iterations["node_count"])
        nodesActive.append(int(iterations["infected"] + iterations["removed"]))
        if iterations["infected"] == 0:
            break

    # Visualization
    #viz = DiffusionTrend(model, trends)
    #viz.plot("WC diffusion.pdf")
    # input()
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
    g = loadAmazon()
    s = ['14949', '4429', '33', '10519', '12771', '8', '297', '481', '5737', '9106', '8939', '93', '1241', '5765', '2501', '99', '3661', '244', '2353', '17525', '5913', '18', '80341', '16340', '33399', '13304', '626', '303', '3673', '1964', '31037', '15934', '7303', '9131', '12615', '7153', '61341', '4935', '30171', '10745', '15925', '3589', '1825', '14439', '9119', '1436', '19527', '26010', '342', '517', '56817', '82909', '37780', '302']
    print(test(g, s))

# Random: ['9703379', '9803262', '104002', '103198', '9312311', '9602428', '9403270', '9803244', '211295', '9905555', '11136', '206278', '9501367', '9811227', '5023', '9307369', '9811257', '9606422', '9908336', '209320', '9801301', '12239', '9604430', '8012', '7198', '9311322', '9306287', '9908288', '9404202', '9810542', '9904319', '9506251', '207215', '9608281', '9905502', '9605367', '9403292', '205323', '7195', '204282', '209306', '10106', '9808390', '210259', '9408244', '207204', '211250', '9412327', '9701202', '9906488']

# Degree ['9803315', '9512380', '9804398', '9407339', '9606399', '9807344', '9306320', '201071', '9905221', '9507378', '9408384', '101336', '9604387', '9807216', '9903282', '3154', '9603208', '9803445', '9801271', '9410404', '9806471', '9705442', '9303230', '9209205', '9209232', '9304225', '9506380', '5025', '9302210', '9610451', '9812360', '9508343', '9603249', '9308246', '9704207', '9806404', '9704376', '9811291', '9712301', '9803466', '9606211', '9802290', '9806292', '9508347', '9207214', '9709356', '9309289', '9402253', '9609381', '10338']