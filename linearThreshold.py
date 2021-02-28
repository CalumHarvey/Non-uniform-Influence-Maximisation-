"""
File containing influence models being used in this simulation
"""

class DiffusionModel:

    def __init__(self, graph):

        self.graph = graph

        self.status = {n: 0 for n in self.graph.nodes}

        self.iterations = 0

        self.available_statuses = {
            "Inactive": 0,
            "Active": 1,
        }
    

    def iterate(self):

