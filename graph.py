class Edge:
    def __init__(self, start: int, end: int, weight: int):
        self.start = start
        self.end = end
        self.weight = weight
    
    def print(self):
        print("({} -> {}): {}".format(self.start, self.end, self.weight))

class Graph:
    def __init__(self):
        self.edges = []
    
    def add_edge(self, start: int, end: int, weight: int):
        edge = Edge(start, end, weight)
        self.edges.append(edge)

    def edges_to(self, node):
        return [edge for edge in self.edges if edge.start == node]

    def edges_from(self, node):
        return [edge for edge in self.edges if edge.end == node]

    def print(self):
        print('\nGraph edges:')
        for n in self.edges:
            n.print()