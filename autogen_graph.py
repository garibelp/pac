import random
import networkx as nx
import time
import pylab
import matplotlib.pyplot as plt

# Function that generate the graph using networkx
def generate_graph(total_nodes):
    # Generate an empty graph
    G = nx.DiGraph()

    # Generate a DAG
    generate_dag(G, total_nodes)

    # Start adding the edges
    add_extra_edges(G)
    return G

def generate_dag(graph: nx.DiGraph, total_nodes: int):
    # List with all nodes
    available_nodes = list(range(1, total_nodes))

    # Add edges to DAG ensuring that all nodes are added
    for n in range(0, total_nodes):
        if (len(available_nodes)) == 0:
            break
        else:
            child_nodes = add_edges(graph, n, available_nodes, 0)
            # Remove from available list
            del available_nodes[0:child_nodes]

def add_edges(graph: nx.DiGraph, start_node: int, available_nodes: list, min_child: int):
    # Function that will add the edges to the nodes
    def generate_edges_from_list(node_list):
        for n in node_list:
            graph.add_edge(start_node, n, weight = random.randint(-10, 10))
    # retrieve the number of child that the node will have from the available nodes
    child_nodes = random.randint(min_child, len(available_nodes))
    # Add the edges from node to the child
    generate_edges_from_list(available_nodes[0:child_nodes])
    return child_nodes

def add_extra_edges(graph: nx.DiGraph):
    # Add more edges to the DAG
    for node in list(graph.nodes):
        if node == 0:
            # Handle root node
            print('processing root')
        else:
            # Handle other nodes
            print('processing node', node)
            possible_nodes_to_add = retrieve_nodes_without_cycle(graph, 0, node)
            add_edges(graph, node, possible_nodes_to_add, 0)
    return

def retrieve_nodes_without_cycle(graph: nx.DiGraph, node_start: int, node_end: int):
    paths = list((nx.all_simple_paths(graph, node_start, node_end)))
    nodes_with_path = []

    for l in paths:
        unique_elements = list(set(l) - set(nodes_with_path))
        nodes_with_path += unique_elements

    # Return all the nodes that currently doesn't have a path to current node
    total_nodes = list(range(0, graph.number_of_nodes()))
    nodes_without_path = list(set(total_nodes) - set(nodes_with_path))

    # Retrieve nodes that already have a path coming from current node to them
    nodes_connected_from = []
    for s, e in graph.edges(node_end):
        nodes_connected_from.append(e)

    # Return list of nodes that have no path coming from or to the current path
    return list(set(nodes_without_path) - set(nodes_connected_from))


# Function that checks if there is a path between the nodes
def has_existing_path(graph: nx.DiGraph, node_start, node_end):
    return True if len(list((nx.all_simple_paths(graph, node_start, node_end)))) > 0 else False

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
        # 'connectionstyle': "arc3, rad = 0.08"
    }

    # Add nodes positioning
    pos = nx.spring_layout(G)

    # Iterate on edges weight object to extract each edge tuple and weight information
    edges, weights = zip(*labels.items())

    # Add the edge display information to the draw
    nx.draw_networkx(G, pos, edge_color = weights, edgelist = edges, edge_cmap = plt.cm.Reds,  **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels, label_pos = 0.2, font_size = 7)

    # Display image
    plt.gca().set_facecolor("grey")
    pylab.show()

# Add the graph to a .csv file
def write_to_csv(edges):
    # TODO: remove prints and add graph to csv file
    # Print all edges generated

    print("\n[U, V] : W\n------------")
    print("\n".join("{} : {}".format(edge, weight) for edge, weight in edges.items()))

def main():
    # TODO: Generate multiple graphs and save them on a .csv file for the next step of project
    # Number of nodes on graph
    nodes = int(input('--> '))
    
    start_time = time.time()
    
    # Generate basic graph
    G = generate_graph(nodes)
    
    print('\nGraph generated:', G)
    print('Execution duration:', time.time() - start_time, 'seconds')

    # Generate graph draw
    edges = nx.get_edge_attributes(G, 'weight')

    # TODO: Function that add the graph to a .csv file
    write_to_csv(edges)

    # Display graph image
    display_graph(G, edges)

if __name__ == "__main__":
    main()