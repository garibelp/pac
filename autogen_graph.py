import random
import networkx as nx
import pylab
import matplotlib.pyplot as plt

# Function that generate the graph using networkx
def generate_graph(nodes):
    # nodes = number of nodes, p = probability of edge generation
    # Generating a directed graph to avoid unconnected nodes
    G = nx.gnp_random_graph(nodes, p = 0.4, directed = True)

    generate_edges_weight(G)

    connect_all_nodes(G)

    return remove_negative_cycles(G)

# Randomly add weight on all edges of the graph
def generate_edges_weight(G):
    for (start, end) in G.edges:
        G.edges[start, end]['weight'] = random.randint(-5, 5)
    return G

# Check if graph has any node without edges and add to the graph
def connect_all_nodes(G):
    # TODO: Validate and generate the node
    return G

# Check if graph contains negative cycles and break it
def remove_negative_cycles(G):
    # TODO: Check with Bellman-Ford and break
    return G

def main():
    # Generate basic graph
    G = generate_graph(random.randrange(2, 10))

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
    print("[U, V] : W\n------------\n" + "\n".join("{} : {}".format(k, v) for k, v in labels.items()))


    # Add the edge display information to the draw
    nx.draw_networkx(G, pos, edge_color = weights, edgelist = edges, edge_cmap = plt.cm.Reds,  **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)

    # Display image
    plt.gca().set_facecolor("gray")
    pylab.show()

if __name__ == "__main__":
    main()