from ndlib.models import DiffusionModel
import future.utils
import numpy as np
import random
import networkx

class WeightedCascadeModel:
    """
        Edge Parameters to be specified via ModelConfig
        :param threshold: The edge threshold. As default a value of 0.1 is assumed for all edges.
    """

    def __init__(self, directedGraph, seed):
        """
             Model Constructor
             :param graph: A networkx graph object
         """
        self.available_statuses = {
            0 : "Susceptible",
            1 : "Infected",
            2 : "Removed"
        }

        self.undirectedGraph = directedGraph.to_undirected()
        self.graph = directedGraph
        self.nodes = self.graph.nodes
        self.nodeStatuses = {}

        for node in self.nodes:
            if node in seed:
                self.nodeStatuses[node] = 1
            else:
                self.nodeStatuses[node] = 0

        self.name = "Weighted Cascades"

        np.random.seed(None)



    def iteration(self):
        """
        Execute a single model iteration
        :return: Iteration_id, Incremental node status (dictionary node->status)
        """

        status = self.nodeStatuses.copy()

        for u in self.nodes:
            if self.nodeStatuses[u] != 1:
                continue

            neighbors = list(self.graph.neighbors(u))  # neighbors and successors (in DiGraph) produce the same result

            if len(neighbors) > 0:
                temp = 1/ self.undirectedGraph.degree[u]
                threshold = ("%.2f" % temp)

                for v in neighbors:
                    if self.nodeStatuses[v] == 0:
                        
                        temp = np.random.random_sample()
                        flip = ("%.2f" % temp)
 
                        if flip <= threshold:
                            status[v] = 1


            status[u] = 2
        
        self.nodeStatuses = status.copy()

        removedCount = sum(value == 2 for value in self.nodeStatuses.values())
        infectedCount = sum(value == 1 for value in self.nodeStatuses.values())

        return {"infected" : infectedCount, "removed" : removedCount}