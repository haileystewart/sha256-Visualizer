import hashlib
import random
import time

def compute_hash_rate(num_hashes):
    """
    Computes the SHA-256 hashes for a given number of inputs and calculates the hash rate.
    
    Parameters:
        num_hashes (int): Number of hashes to compute.
        
    Returns:
        float: Total time taken to compute the hashes (in seconds).
        float: Hash rate (hashes per second).
    """
    start_time = time.time()
    
    for _ in range(num_hashes):
        random_input = str(random.getrandbits(256))
        hashlib.sha256(random_input.encode('utf-8')).hexdigest()
    
    end_time = time.time()
    total_time = end_time - start_time
    hash_rate = num_hashes / total_time
    return total_time, hash_rate

def estimate_attack_time(hash_rate, target_hashes):
    """
    Estimates the time required to compute a specific number of hashes based on the hash rate.
    
    Parameters:
        hash_rate (float): Hashes computed per second.
        target_hashes (int): Number of hashes required for the attack.
        
    Returns:
        float: Estimated time in seconds.
    """
    return target_hashes / hash_rate

if __name__ == "__main__":
    # Input: Number of hashes to compute
    num_hashes = 10000  # Adjust for testing and performance
    
    print(f"Computing {num_hashes} hashes to measure hash rate...")
    
    # Compute hash rate
    total_time, hash_rate = compute_hash_rate(num_hashes)
    
    print(f"\nResults:")
    print(f"Total time to compute {num_hashes} hashes: {total_time:.4f} seconds")
    print(f"Hash rate: {hash_rate:.2f} hashes per second")
    
    # Estimate attack times
    birthday_attack_hashes = 2 ** 64  # Weak collision resistance
    brute_force_attack_hashes = 2 ** 128  # Strong collision resistance
    
    birthday_time = estimate_attack_time(hash_rate, birthday_attack_hashes)
    brute_force_time = estimate_attack_time(hash_rate, brute_force_attack_hashes)
    
    print(f"\nEstimated time for birthday attack (2^64 hashes): {birthday_time / (60 * 60 * 24):.2f} days")
    print(f"Estimated time for brute-force attack (2^128 hashes): {brute_force_time / (60 * 60 * 24):.2e} days")
