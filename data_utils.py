from graph import Graph
import csv

# TODO: Generate graph using data loaded from .csv file
def load_csv_to_graph(path) -> Graph:
    print('File path: "{}"'.format(path))
    # Initialize graph
    G = Graph()
    # with open(path) as csvDataFile:
    #     # read file as csv file 
    #     csvReader = csv.reader(csvDataFile, delimiter = ' ')
    #     for row in csvReader:
    #         print(row[0], row[1], row[2])

    # Test of Graph class created
    G.add_edge(0, 1, -1)
    G.add_edge(0, 2, 1)
    G.add_edge(0, 3, 10)
    G.add_edge(2, 3, -10)
    G.add_edge(1, 3, 10)

    for edge in G.edges_to(0):
        edge.print()

    return G