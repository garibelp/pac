import numpy as np

class Edge:
    def __init__(self, start: int, end: int, weight: int):
        self.start = start
        self.end = end
        self.weight = weight
    
    def print(self):
        print("({} -> {}): {}".format(self.start, self.end, self.weight))

    def get_values(self):
        return [self.start, self.end, self.weight]

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
    
    def add_node(self, node: int):
        if not node in self.nodes:
            self.nodes.append(node)

    def add_edge(self, start: int, end: int, weight: int):
        edge = Edge(start, end, weight)
        self.add_node(start)
        self.add_node(end)
        self.edges.append(edge)

    def get_nodes(self):
        return np.sort(self.nodes)

    def get_edges(self):
        return self.edges

    def total_nodes(self):
        return len(self.nodes)
    
    def get_edges_from(self, node):
        return [edge for edge in self.edges if edge.end == node]
    
    def get_edges_to(self, node):
        return [edge for edge in self.edges if edge.start == node]

    def print(self):
        print('\nTotal nodes:', self.total_nodes())
        print('Total edges:', len(self.edges), '\n')
        # for n in self.edges:
        #     n.print()