import random
import networkx as nx
import numpy as np
import pylab

# Function that generate the graph using networkx
def generate_graph(nodes):
    # nodes = number of nodes, p = probability of edge generation
    # Generating a directed graph to avoid unconnected nodes
    G = nx.gnp_random_graph(nodes, p = 0.4, directed = True)

    # TODO: Ensure that all nodes to be connected

    return generate_edges_weight(G)

# Function that insert the nodes and edges on the graph
def generate_edges_weight(G):
    # Randomly add weight on all edges of the graph
    for (start, end) in G.edges:
        G.edges[start, end]['weight'] = random.randint(-10, 10)

    return validate_and_update_graph(G)

# Function that check if graph is already correctly set
def validate_and_update_graph(G):
    # TODO: break the negative edge cycles on the graph
    # if (graph has negative cycle):
    #   remove negative cycle    
    return G

def validate_input(message):
    try:
        number = int(input(message))
        if number <= 0:
            raise ValueError()
        return int(number)
    except ValueError:
        # if not a positive int print message and ask for input again
        print("Invalid input (Must be a positive integer)")
        return validate_input(message)

def main():
    # Generate basic graph
    G = generate_graph(validate_input("Enter number of nodes: "))

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