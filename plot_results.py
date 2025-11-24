import numpy as np
import matplotlib.pyplot as plt

def plot_results(sent_packets, positions, sink, lambd, rc, save_path=None):
    """
    Generates and saves a scatter plot: Distance vs. Packets Forwarded.
    """
    # Calculate Euclidean distance of every node from the sink
    distances = np.linalg.norm(positions - positions[sink], axis=1)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot all sensor nodes (Blue)
    ax.scatter(distances, sent_packets, alpha=0.7, s=40, c='blue', edgecolors='k', label='Sensor Nodes')
    
    # Highlight the Sink node (Red) at distance 0
    # The Y-value for the sink represents total received packets
    ax.scatter([0], [sent_packets[sink]], c='red', s=100, label='Sink Node', edgecolors='k', zorder=5)
    
    # Formatting the chart
    ax.set_xlabel('Euclidean Distance from Sink')
    ax.set_ylabel('Total Packets Forwarded/Received')
    ax.set_title(f'Network Simulation: rc={rc:.3f}, λ={lambd:.2f}')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Save to file or show
    if save_path:
        plt.savefig(save_path, dpi=100, bbox_inches='tight')
        plt.close(fig) # Close to free memory
    else:
        plt.show()