from scipy.special import comb
import math

def binomial_probability(n, k):
    """
    Calculates the binomial probability for exactly k bits set in an n-bit hash.
    
    Parameters:
        n (int): Total number of bits.
        k (int): Number of bits set to 1.
        
    Returns:
        float: Probability of exactly k bits being set to 1.
    """
    # Binomial probability formula: C(n, k) / 2^n
    return comb(n, k) / (2 ** n)

if __name__ == "__main__":
    # Parameters for a 256-bit hash
    total_bits = 256
    
    # Calculate probabilities for 128 and 100 bits being set to 1
    prob_128 = binomial_probability(total_bits, 128)
    prob_100 = binomial_probability(total_bits, 100)
    
    print(f"Probability of exactly 128 bits set to 1 in a 256-bit hash: {prob_128:.10e}")
    print(f"Probability of exactly 100 bits set to 1 in a 256-bit hash: {prob_100:.10e}")
