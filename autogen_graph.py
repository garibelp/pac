import random
import networkx as nx
import time
import pylab
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import os
import sys

# Function that generate the graph using networkx
def generate_graph(total_nodes, total_edges):
    print('[nodes, edges] : [{}, {}]'.format(total_nodes, total_edges))
    # Generate an empty graph
    G = nx.DiGraph()

    def add_edge(iteration, retry):
        u = random.randint(0, total_nodes - 2)
        v = random.randint(u + 1, total_nodes - 1)
        
        print("[{}] - ({}; {}) - Retry: {}".format(iteration + 1, u, v, retry))

        if G.has_edge(u, v):
            return add_edge(iteration, True)
        
        G.add_edge(u, v, weight = random.randint(-10, 10))
    
    for i in range(0, total_edges):
        print("[{}] Initializing iteration".format(i + 1))
        add_edge(i, False)

    return G


# Function that plots the graph image on screen
def save_image_graph(G, labels, folder, img_name):
    # Add display options
    options = {
        'node_color': 'lightgreen',
        'node_size': 300,
        'width': 1,
        'arrows': True,
        'arrowstyle': '->',
        'arrowsize': 10,
        'with_labels': True,
        'connectionstyle': "arc3, rad = 0.08"
    }

    # Add nodes positioning
    pos = nx.circular_layout(G)

    # Iterate on edges weight object to extract each edge tuple and weight information
    edges, weights = zip(*labels.items())

    # Clear older draws
    plt.clf()

    # Add the edge display information to the draw
    nx.draw_networkx(G, pos, edge_color = weights, edgelist = edges, edge_cmap = plt.cm.Reds,  **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = labels, label_pos = 0.2, font_size = 7)

    # Display image
    plt.gca().set_facecolor("grey")
    pylab.savefig('./data/{}/{}.png'.format(folder, img_name), dpi = 180)
    # pylab.show()


def main():
    start_time = time.time()
    
    # Generate the folder to save the results of this code execution
    # code_start_string = datetime.fromtimestamp(start_time).strftime('%Y-%m-%dT%H:%M:%S')
    
    # Generate folder that will save the code execution results
    # os.makedirs('./data/{}'.format(code_start_string))

    # Number of nodes on this iteration
    nodes = int(sys.argv[1])
    # max_edges = nodes * (nodes - 1) / 2
    # Number of edges on this iteration
    edges = int(sys.argv[2])

    # Source: https://www.pythontutorial.net/python-basics/python-write-csv-file/
    # Open CSV file to start writing
    f = open('./data/data_{}n_{}e.csv'.format(nodes, edges), 'w')

    # Create the CSV writer
    writer = csv.writer(f, delimiter = ' ')

    # Generate basic graph
    G = generate_graph(nodes, edges)
    print('\nGraph generated: {}'.format(G))

    # Generate graph draw
    edges = nx.get_edge_attributes(G, 'weight')

    # Write total number of nodes and edges
    writer.writerow((nodes, len(edges.items())))

    for (edge_start, edge_end), weight in sorted(edges.items()):
        # Write the edges information to file        
        writer.writerow((edge_start, edge_end, weight))

    # Save graph image generated on this iteration
    # save_image_graph(G, edges, code_start_string, 'graph')
    
    G.clear()

    # Close the file
    f.close()

    print('Total execution duration:', time.time() - start_time, 'seconds\n')

if __name__ == "__main__":
    main()