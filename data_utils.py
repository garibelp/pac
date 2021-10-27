from graph import Graph
import csv

# TODO: Generate graph using data loaded from .csv file
def load_csv_to_graph(path) -> Graph:
    # Initialize graph
    G = Graph()

    with open(path) as csvDataFile:
        # read file as csv file 
        csvReader = csv.reader(csvDataFile, delimiter = ' ')
        for index, row in enumerate(csvReader):
            if index == 0:
                # First index contains total number of nodes and edges
                print('Loading graph with {} nodes and {} edges'.format(row[0], row[1]))
                for i in range(0, int(row[0]) - 1):
                    G.add_node(i)
            else:
                G.add_edge(int(row[0]), int(row[1]), int(row[2]))

    return G

def switch_array_position(array, pos1: int, pos2: int):
    array[pos1], array[pos2] = array[pos2], array[pos1]