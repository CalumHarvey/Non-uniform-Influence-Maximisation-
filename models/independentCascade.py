from ndlib.models import DiffusionModel
import future.utils
import numpy as np
import random
import networkx

class IndependentCascadesModel:
    """
        Edge Parameters to be specified via ModelConfig
        :param threshold: The edge threshold. As default a value of 0.1 is assumed for all edges.
    """

    def __init__(self, G, seed, p=0.01):
        """
             Model Constructor
             :param graph: A networkx graph object
         """
        self.available_statuses = {
            0 : "Susceptible",
            1 : "Infected",
            2 : "Removed"
        }

        # Initialise graph, nodes and node statuses
        self.graph = G
        self.nodes = self.graph.nodes
        self.nodeStatuses = {}

        # Set initial statuses, setting seed nodes to infected
        for node in self.nodes:
            if node in seed:
                self.nodeStatuses[node] = 1
            else:
                self.nodeStatuses[node] = 0

        # Set probability of propagation
        self.threshold = p

        # Initialise randomness seed
        np.random.seed(None)



    def iteration(self):
        """
        Execute a single model iteration
        :return: Iteration_id, Incremental node status (dictionary: node->status)
        """
        # Create copy of node statuses
        status = self.nodeStatuses.copy()

        # For each node...
        for u in self.nodes:
            
            # If inactive, do nothing
            if self.nodeStatuses[u] != 1:
                continue

            # Get neighbours of node u
            neighbors = list(self.graph.neighbors(u))  

            if len(neighbors) > 0:

                threshold = self.threshold

                # For each neighbour...
                for v in neighbors:
                    # If inactive...
                    if self.nodeStatuses[v] == 0:
                        
                        # Activate with probability p
                        temp = np.random.random_sample()
                        flip = float("%.2f" % temp)
 
                        if flip <= threshold:
                            status[v] = 1

            # Set node status to removed after all attempts to infect
            status[u] = 2
        
        self.nodeStatuses = status.copy()

        # Update counts
        removedCount = sum(value == 2 for value in self.nodeStatuses.values())
        infectedCount = sum(value == 1 for value in self.nodeStatuses.values())

        return {"infected" : infectedCount, "removed" : removedCount}