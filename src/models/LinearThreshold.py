import future.utils

__author__ = "Giulio Rossetti"
__license__ = "BSD-2-Clause"
__email__ = "giulio.rossetti@gmail.com"


class LinearThresholdModel():
    """
        Node Parameters to be specified via ModelConfig
       :param threshold: The node threshold. If not specified otherwise a value of 0.1 is assumed for all nodes.
    """

    def __init__(self, graph, seed, threshold=0.5):
        """
             Model Constructor
             :param graph: A networkx graph object
         """
        self.available_statuses = {
            "Susceptible": 0,
            "Infected": 1
        }

        self.graph = graph
        self.nodes = self.graph.nodes
        self.nodeStatuses = {}

        for node in self.nodes:
            if node in seed:
                self.nodeStatuses[node] = 1
            else:
                self.nodeStatuses[node] = 0
        
        self.threshold = threshold

        self.name = "Linear Threshold"


    def iteration(self, node_status=True):
        """
        Execute a single model iteration
        :return: Iteration_id, Incremental node status (dictionary node->status)
        """

        status = self.nodeStatuses.copy()

        for u in self.graph.nodes:
            if self.nodeStatuses[u] == 1:
                continue

            neighbors = list(self.graph.neighbors(u))

            infected = 0
            for v in neighbors:
                infected += self.nodeStatuses[v]

            if len(neighbors) > 0:
                infected_ratio = float(infected)/len(neighbors)
                if infected_ratio >= self.threshold:
                    status[u] = 1

        
        self.nodeStatuses = status.copy()

        removedCount = sum(value == 2 for value in self.nodeStatuses.values())
        infectedCount = sum(value == 1 for value in self.nodeStatuses.values())

        return {"infected" : infectedCount, "removed" : removedCount}