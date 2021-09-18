import random

class Graph:
    def __init__(self, N, E):
        self.N = N  # Number of nodes
        self.E = E  # Number of edges
        self.edges = []

class Edge:
    def __init__(self, S, E, W):
        self.S = S  # Node start
        self.E = E  # Node end
        self.W = W  # Edge weight

def generateGraph(V, E):
    graph = Graph(V, E)
    # TODO: Logic to generate edges connection for graph
    return graph

def generateEdge(startNode, endNode):
    W = random.randint(-10, 10) # Generate weight
    return Edge(startNode, endNode, W)

def validateInput(message):
    number = input(message)
    try:
        val = int(number)
        if val < 0:
            raise ValueError()
    except ValueError:
        # if not a positive int print message and ask for input again
        print("Invalid input (Must be a positive integer)")
        return validateInput(message)
    return number

def main():
    # User entries for vertex and edge numbers
    n = validateInput("Enter number of nodes: ")
    e = validateInput("Enter number of edges: ")
    
    g = generateGraph(n, e)
    
    # TODO: Plot generated graph
    print("test", g.N, g.E, g.edges)

if __name__ == "__main__":
    main()