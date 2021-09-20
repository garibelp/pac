import random
import networkx as nx
import pylab

# Function that generate the graph using networkx
def generateGraph(nodes):
    # Simple digraph generated
    G = nx.DiGraph()
    return generateEdges(G, nodes)

# Function that insert the nodes and edges on the graph
def generateEdges(G, nodes):
    for node in range(nodes):
        G.add_node(node + 1)

    # TODO: Update method to randomly generate edges and weight
    # Example edge:
    G.add_edges_from([(1, 2)], weight = random.randint(-10, 10))
    
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
    pos = nx.spring_layout(G)

    # Generate graph draw
    nx.draw(G, pos, **options)

    # Add the edge weight to the draw
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Display image
    pylab.show()

if __name__ == "__main__":
    main()