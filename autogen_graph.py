import random
import networkx as nx
import numpy as np
import pylab
import matplotlib.pyplot as plt

# Function that generate the graph using networkx
def generate_graph(nodes):
    # nodes = number of nodes, create_using = Type of graph to be used
    # Generating a directed complete graph to avoid unconnected nodes
    G = nx.complete_graph(nodes, create_using=nx.DiGraph())

    return generate_edges_weight(G)

def retrieve_negative_cycles(G):
    # TODO: Retrieve negative cycle
    return None

# Randomly add weight on all edges of the graph
def generate_edges_weight(G):
    # OBS.: Not the most efficient way to generate graph, but works for the purpose
    # Set all edges to weight = 0 at start
    for (start, end) in G.edges:
        G.edges[start, end]['weight'] = 0

    # Start changing the weights and checking if it generates a negative cycle
    for (start, end) in G.edges:
        weight = random.randint(-50, 50)
        G.edges[start, end]['weight'] = weight
        if weight < 0:
            neg_cycle = retrieve_negative_cycles(G)
            if neg_cycle is not None:
                # TODO: Change the value to a positive if a negative cycle happens
                print('TODO:' + neg_cycle)
    return G

def main():
    # Generate basic graph
    G = generate_graph(int(input('--> ')))

    # Add display options
    options = {
        'node_color': 'lightblue',
        'node_size': 1000,
        'width': 1,
        'arrows': True,
        'arrowstyle': '->',
        'arrowsize': 15,
        'with_labels': True,
        'connectionstyle': "arc3, rad = 0.08"
    }

    # Add nodes positioning
    pos = nx.spring_layout(G, k = 5)

    # Generate graph draw
    labels = nx.get_edge_attributes(G, 'weight')
    
    # Iterate on edges weight object to extract each edge tuple and weight information
    edges, weights = zip(*labels.items())

    # Print all edges generated
    print("\n[U, V] : W\n------------\n" + "\n".join("{} : {}".format(k, v) for k, v in labels.items()))


    # Add the edge display information to the draw
    nx.draw_networkx(G, pos, edge_color = weights, edgelist = edges, edge_cmap = plt.cm.Reds,  **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels, label_pos = 0.2, font_size = 7)

    # Display image
    plt.gca().set_facecolor("grey")
    pylab.show()

if __name__ == "__main__":
    main()