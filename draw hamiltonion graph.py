import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_pdf import PdfPages
import re

# File locations
input_txt_path = r"C:\Users\ASUS\Desktop\maharshee\Python\Python Codes\hamiltonian_graph_data.txt"
output_pdf_path = r"C:\Users\ASUS\Desktop\maharshee\Python\Python Codes\hamiltonian_subgraphs.pdf"

def draw_complete_graph(n):
    """Draw and save the complete graph K_n."""
    G = nx.complete_graph(n)
    
    # Fix the position of the vertices
    pos = nx.circular_layout(G)
    
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=700, font_size=14)
    plt.title(f'Complete Graph K_{n}')
    plt.show()

def read_hamiltonian_circuits(file_path):
    """Read and parse Hamiltonian circuits from the text file."""
    circuits = []
    with open(file_path, 'r') as file:
        data = file.read()
        matches = re.findall(r'Hamiltonian Circuit \d+: \[(.*?)\]', data)
        for match in matches:
            # Parse edges
            edges_str = match.replace('), (', '),(').replace('(', '').replace(')', '')
            edges_list = edges_str.split(',')
            edges = [(int(edges_list[i]), int(edges_list[i+1])) for i in range(0, len(edges_list), 2)]
            circuits.append(edges)
    return circuits

def save_hamiltonian_circuits_to_pdf(circuits, output_pdf_path, n):
    """Draw and save all Hamiltonian circuits and the complete graph to a PDF file."""
    G = nx.complete_graph(n)
    pos = nx.circular_layout(G)  # Fixed positions for vertices

    with PdfPages(output_pdf_path) as pdf:
        # Draw the complete graph
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=700, font_size=14)
        plt.title(f'Complete Graph K_{n}')
        pdf.savefig()
        plt.close()
        
        # Draw each Hamiltonian circuit
        for i, edges in enumerate(circuits, 1):
            plt.figure(figsize=(8, 6))
            subgraph = nx.Graph()
            subgraph.add_edges_from(edges)
            
            nx.draw(subgraph, pos, with_labels=True, node_color='skyblue', edge_color='black', node_size=500, font_size=12)
            plt.title(f'Hamiltonian Circuit {i}')
            
            pdf.savefig()
            plt.close()

    print(f"Hamiltonian circuits and the complete graph have been saved to {output_pdf_path}")

# Example usage for n = 5
n = 9

# Read the Hamiltonian circuits from the file
circuits = read_hamiltonian_circuits(input_txt_path)

# Save the Hamiltonian circuits and the complete graph to a PDF file
save_hamiltonian_circuits_to_pdf(circuits, output_pdf_path, n)
