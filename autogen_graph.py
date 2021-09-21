import random
import networkx as nx
from networkx.algorithms.components.connected import is_connected
import pylab

# Function that generate the graph using networkx
def generateGraph(nodes):
    # nodes = number of nodes, p = probability of edge generation
    G = nx.gnp_random_graph(nodes, p = 0.5)

    # TODO: Ensure that all nodes to be connected

    return generateEdgesWeight(G, nodes)

# Function that insert the nodes and edges on the graph
def generateEdgesWeight(G, nodes):
    for (start, end) in G.edges:
        G.edges[start, end]['weight'] = random.randint(-10, 10)

    return validateAndUpdateGraph(G)

# Function that check if graph is already correctly set
def validateAndUpdateGraph(G):
    # TODO: connect missing nodes on graph
    if (nx.is_connected(G) == False):
        print("Is not connected")

    # TODO: break the negative edge cycles on the graph
    # if (graph has negative cycle):
    #   remove negative cycle
    
    return G

def validateInput(message):
    try:
        number = int(input(message))
        if number <= 0:
            raise ValueError()
        return int(number)
    except ValueError:
        # if not a positive int print message and ask for input again
        print("Invalid input (Must be a positive integer)")
        return validateInput(message)

def main():
    # Generate basic graph
    G = generateGraph(validateInput("Enter number of nodes: "))

    # Add display options
    options = {
        'node_color': 'gray',
        'node_size': 500,
        'width': 1,
        'arrows': True,
        'arrowstyle': '-|>',
        'arrowsize': 15,
        'with_labels': True,
    }

    # Add nodes positioning
    pos = nx.circular_layout(G)

    # Generate graph draw
    nx.draw(G, pos, **options)

    # Add the edge weight to the draw
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Display image
    pylab.show()

if __name__ == "__main__":
    main()