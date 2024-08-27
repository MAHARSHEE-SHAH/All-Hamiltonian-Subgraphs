import networkx as nx
import itertools
import random

def generate_hamiltonian_circuits(n):
    """Generate exactly (n-1)/2 edge-disjoint Hamiltonian circuits for a complete graph K_n with odd n."""
    if n % 2 == 0 or n < 3:
        raise ValueError("n must be an odd number greater than or equal to 3.")

    def generate_circuit(nodes):
        return [(nodes[i], nodes[(i + 1) % n]) for i in range(n)]

    def rotate(lst, k):
        return lst[k:] + lst[:k]

    def reflect(lst):
        return lst[::-1]

    def normalize_circuit(circuit):
        # Normalize the circuit by sorting edges and considering reflections
        sorted_edges = sorted(tuple(sorted(edge)) for edge in circuit)
        rotations_and_reflections = []
        circuit_tuple = tuple(sorted_edges)
        for i in range(n):
            rotated = rotate(circuit_tuple, i)
            rotations_and_reflections.append(rotated)
            rotated_reflected = reflect(rotated)
            rotations_and_reflections.append(rotated_reflected)
        return tuple(min(rotations_and_reflections))

    nodes = list(range(n))
    all_circuits = set()
    used_edges = set()
    
    def add_circuit(circuit):
        if all(tuple(sorted(edge)) not in used_edges for edge in circuit):
            normalized = normalize_circuit(circuit)
            if normalized not in all_circuits:
                all_circuits.add(normalized)
                used_edges.update(tuple(sorted(edge)) for edge in circuit)

    def generate_all_circuits():
        # Generating all possible circuits
        all_nodes = list(range(n))
        for permutation in itertools.permutations(all_nodes):
            circuit = generate_circuit(permutation)
            add_circuit(circuit)
            if len(all_circuits) >= (n-1)//2:
                break

    generate_all_circuits()
    
    # Convert set of tuples to list of lists
    unique_circuits = [list(circuit) for circuit in all_circuits]
    return unique_circuits[: (n-1)//2]  # Return exactly (n-1)/2 circuits

def save_and_print_hamiltonian_circuits(n, output_txt_path):
    """Save Hamiltonian circuits to a text file and print them in the console."""
    circuits = generate_hamiltonian_circuits(n)
    
    with open(output_txt_path, 'w') as file:
        for i, circuit in enumerate(circuits, 1):
            circuit_string = f"Hamiltonian Circuit {i}: {circuit}"
            print(circuit_string)  # Print to console
            file.write(circuit_string + '\n')  # Save to file
    
    print(f"\nHamiltonian circuits have been saved to {output_txt_path}")

# Example for n = 5 (Complete graph K5)
n = 9
output_txt_path = r"C:\Users\ASUS\Desktop\maharshee\Python\Python Codes\hamiltonian_graph_data.txt"
save_and_print_hamiltonian_circuits(n, output_txt_path)
