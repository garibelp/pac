import random
import networkx as nx
import pylab

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
        G.edges[start, end]['weight'] = random.randint(-10, 10)
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
    G = generate_graph(random.randrange(2, 15))

    # Add display options
    options = {
        'node_color': 'gray',
        'node_size': 1000,
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