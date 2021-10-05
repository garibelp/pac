from itertools import count
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

def has_negative_cycle(G):
    # TODO: Retrieve negative cycle
    try:
        nx.bellman_ford_predecessor_and_distance(G, 0)
    except nx.NetworkXUnbounded:
        return True
    return False

# Randomly add weight on all edges of the graph
def generate_edges_weight(G):
    # OBS.: Not the most efficient way to generate graph, but works for the purpose
    # Set all edges to weight = 0 at start
    for (start, end) in G.edges:
        G.edges[start, end]['weight'] = 0

    # Start changing the weights and checking if it generates a negative cycle
    for (start, end) in G.edges:
        weight = random.randint(-10, 10)
        G.edges[start, end]['weight'] = weight
        if weight < 0 and has_negative_cycle(G):
            # TODO: Find a better way to break negative cycles
            # Change the value to a positive if a negative cycle happens
            G.edges[start, end]['weight'] = weight * -1
    return G

# Function that plots the graph image on screen
def display_graph(G, labels):
    # Add display options
    options = {
        'node_color': 'lightgreen',
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

    # Iterate on edges weight object to extract each edge tuple and weight information
    edges, weights = zip(*labels.items())

    # Add the edge display information to the draw
    nx.draw_networkx(G, pos, edge_color = weights, edgelist = edges, edge_cmap = plt.cm.Reds,  **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels, label_pos = 0.2, font_size = 7)

    # Display image
    plt.gca().set_facecolor("grey")
    pylab.show()

# Add the graph to a .csv file
def write_to_csv(nodes, edges):
    # TODO: remove prints and add graph to csv file
    # Print all edges generated
    print("\nNumber of nodes:", nodes)
    print("Number of edges:", len(edges.items()))
    print("\n[U, V] : W\n------------")
    print("\n".join("{} : {}".format(edge, weight) for edge, weight in edges.items()))

def main():
    # TODO: Generate multiple graphs and save them on a .csv file for the next step of project

    # Number of nodes on graph
    nodes = int(input('--> '))

    # Generate basic graph
    G = generate_graph(nodes)

    # Generate graph draw
    edges = nx.get_edge_attributes(G, 'weight')

    # Function that add the graph to a .csv file
    write_to_csv(nodes, edges)

    # Display graph image
    display_graph(G, edges)


if __name__ == "__main__":
    main()