import hashlib

def compute_sha256_hash(input_string):
    """
    Computes the SHA-256 hash of a given input string.
    
    Parameters:
        input_string (str): The string to hash.
        
    Returns:
        str: The SHA-256 hash in hexadecimal format.
    """
    sha256_hash = hashlib.sha256(input_string.encode('utf-8')).hexdigest()
    return sha256_hash

if __name__ == "__main__":
    # Prompt the user for input
    user_input = input("Enter the string to compute its SHA-256 hash: ")
    hash_result = compute_sha256_hash(user_input)
    print(f"SHA-256 Hash of '{user_input}': {hash_result}")
