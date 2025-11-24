import numpy as np
import networkx as nx

def geometric_graph(n, rc):
    """
    Generates a Random Geometric Graph (RGG).
    
    Args:
        n (int): Number of nodes.
        rc (float): Connectivity radius.
        
    Returns:
        tuple: (G, positions) where G is the NetworkX graph and 
               positions is a numpy array of coordinates.
    """
    # NetworkX has a built-in optimized function for RGGs using k-d trees
    G = nx.random_geometric_graph(n, rc)
    
    # Extract node positions into a dictionary
    pos_dict = nx.get_node_attributes(G, 'pos')
    
    # Convert positions to a numpy array for easier mathematical operations later
    # The order of nodes is 0, 1, 2, ... n-1
    positions = np.array([pos_dict[i] for i in range(n)])
    
    return G, positions