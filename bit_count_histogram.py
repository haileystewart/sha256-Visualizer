import hashlib
import random
from collections import Counter
import matplotlib.pyplot as plt
import os

def count_1_bits(hex_hash):
    """
    Counts the number of 1-bits in the binary representation of a hexadecimal hash.
    
    Parameters:
        hex_hash (str): The hash value in hexadecimal format.
        
    Returns:
        int: The count of 1-bits in the hash.
    """
    return bin(int(hex_hash, 16)).count('1')

def generate_random_inputs(num_inputs):
    """
    Generates a list of random inputs to hash.
    
    Parameters:
        num_inputs (int): Number of random inputs to generate.
        
    Returns:
        list: A list of random strings.
    """
    return [str(random.getrandbits(256)) for _ in range(num_inputs)]

def generate_histogram(bit_counts, output_path):
    """
    Generates and saves a histogram of 1-bit counts in hash outputs.
    
    Parameters:
        bit_counts (list): List of 1-bit counts.
        output_path (str): Path to save the histogram image.
    """
    histogram = Counter(bit_counts)
    plt.bar(histogram.keys(), histogram.values(), width=1.0)
    plt.title("Histogram of 1-bits in SHA-256 Hash Outputs")
    plt.xlabel("Number of 1-bits")
    plt.ylabel("Frequency")
    plt.grid(axis='y')

    # Save the histogram as a PNG file
    plt.savefig(output_path)
    plt.close()
    print(f"Histogram saved to {output_path}")

if __name__ == "__main__":
    # Number of random inputs to hash
    num_hashes = 10000  # Adjust this value for your performance needs

    print(f"Generating {num_hashes} random inputs and computing SHA-256 hashes...")
    
    random_inputs = generate_random_inputs(num_hashes)
    bit_counts = []

    for input_data in random_inputs:
        hash_value = hashlib.sha256(input_data.encode('utf-8')).hexdigest()
        bit_counts.append(count_1_bits(hash_value))

    print("Hashing complete. Generating histogram...")

    # Ensure the results directory exists
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "histogram.png")

    generate_histogram(bit_counts, output_path)
